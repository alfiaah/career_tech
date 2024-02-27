from __future__ import division
from math import sqrt
from flask import Flask, render_template, request, jsonify
from collections import Counter
from flask import Flask, request
from predict import Predictor
from model import Model
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import json
from bson import json_util
from PyPDF2 import PdfFileReader
from flask import *
from database import *
import uuid

from functions import *


user=Blueprint('user',__name__)

@user.route('/userhome',methods=['get','post'])
def userhome():
	data={}
	q="select * from team inner join teammember using(team_id) WHERE user_id='%s'"%(session['id'])
	res=select(q)
	if res:
		data['team']=res
	else:
		data['team']="team"
	q="select * from user WHERE user_id='%s'"%(session['id'])
	data['user']=select(q)
	return render_template("userhome.html",data=data)


@user.route('/usersendcomplaint',methods=['get','post'])
def usersendcomplaint():
	data={}

	if 'submit' in request.form:
		comp=request.form['comp']
		q="INSERT INTO `complaint`(`user_id`,`user_type`,`complaint`,`reply`,`date`) VALUES ('%s','user','%s','pending',CURDATE())"%(session['id'],comp)
		insert(q)
		flash('COMPLAINT DELIVERED')
		return redirect(url_for('user.usersendcomplaint'))
	q="SELECT * FROM `complaint` WHERE `user_id`='%s' AND `user_type`='user'"%(session['id'])
	data['complaint']=select(q)
	return render_template("usersendcomplaint.html",data=data)






@user.route('/userviewjob',methods=['get','post'])
def userviewjob():
		data={}
		# print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
			
		from datetime import datetime
		cd=datetime.today().strftime('%Y-%m-%d')
		print(cd)
		
		# q="SELECT *,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user` FROM `application` INNER JOIN `job` USING (`job_id`) INNER JOIN `company` USING (`company_id`) INNER JOIN `user` USING (`user_id`) ORDER BY `application_id`DESC"
		q="SELECT * FROM `job` INNER JOIN `company` USING (`company_id`) "
		res=select(q)
		
		if res:
			data['job']=res
			for i in res:
				print(i['last_date'])
				print(i['job_id'])


		return render_template("userviewjob.html",data=data)
	


@user.route('/usersendapplication',methods=['get','post'])
def usersendapplication():
	data={}
	data['sec']=10
	data['min']=0
	sid=session['sid']
	examid=request.args['examid']



	def next(nextid,last):
		
		nid=nextid
		last=last
		q="select * from questions where question_id='%s' and exam_id='%s'"%(nid,examid)
		res=select(q)
		if res:
			q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,nid)
			added=select(q)	
			print("added",added)		
			data['added']=added
			q="SELECT * FROM `questionanswer` INNER JOIN `questions` USING(`question_id`) WHERE `questionanswer`.`question_id`='%s'"%(res[0]['question_id'])
			res=select(q)
			data['next']=res
		else:
			nid=int(nid)+1
			if nid>int(last):
				pass
			else:
				next(nid,last)
	# q="SELECT * FROM questions INNER JOIN `questionanswer` USING(`question_id`) WHERE `questions`.`exam_id`='%s'"%(exam_id)
	q="SELECT `question_id` FROM `questions`  order by question_id"
	
	qid=select(q)	

	if qid:
		
		qone=qid[0]['question_id']
		print(qone)
		data['qone']=qone
		last=qid[-1]['question_id']
		data['last']=last
		q="SELECT * FROM `questionanswer` INNER JOIN `questions` USING(`question_id`) WHERE `questionanswer`.`question_id`='%s'"%(qone)
		data['qno']=1
		data['1q']=select(q)
		q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,qone)
		added=select(q)	
		print(added)		
		data['added']=added

		
	if 'action' in request.args:
		data['qno']=request.args['qno']
		data['qno']=int(data['qno'])+1
		action=request.args['action']
		nextid=request.args['nid']
		next(nextid,last)
	else:
		action=None
	if 'action2' in request.args:
		data['qno']=request.args['qno']
		data['qno']=int(data['qno'])-1
		action=request.args['action2']
		preid=request.args['pid']
		print(preid,qone)
		print("gyh")
	else:
		action=None
	if 'submit' in request.form:
		anss=request.form['anss']

		print("...................."+anss)
		
		q="insert into answers values(NULL,'%s','%s','%s')"%(anss,sid,res[0]['maximum_mark'])
		insert(q)
		return redirect(url_for('student.usersendapplication'))

	if 'nxtsubmit' in request.form:
		anss=request.form['anss']

		
			
		q="insert into answers values(NULL,'%s','%s','%s')"%(anss,sid,res[0]['maximum_mark'])
		insert(q)
		return redirect(url_for('student.usersendapplication',action='next',nid=nextid))

				
	
	if 'complete' in request.form:
		q="SELECT SUM(mark_awarded) FROM answers WHERE student_id='%s' AND qstansr_id IN(SELECT qstansr_id FROM questionanswer WHERE question_id IN (SELECT question_id FROM questions WHERE exam_id='%s'))"%(sid,examid)
		res=select(q)
		print(res)
		if res:
			result=res[0]['SUM(mark_awarded)']
			q="insert into result values(NULL,'%s','%s','%s')"%(examid,sid,result)
			insert(q)
			q="insert into participation values(NULL,'%s','%s')"%(examid,sid)
			insert(q)
		return redirect(url_for('student.student_viewexamshedules'))
	return render_template('userapp.html',data=data)


# @user.route('/usersendapplication',methods=['get','post'])
# def usersendapplication():
# 		data={}

# 		id=session['id']		
# 		# q="SELECT *,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user` FROM `application` INNER JOIN `job` USING (`job_id`) INNER JOIN `company` USING (`company_id`) INNER JOIN `user` USING (`user_id`) ORDER BY `application_id`DESC"
# 		if "submit" in request.form:

# 			re=request.files['re']
# 			path='static/uploads/'+str(uuid.uuid4())+re.filename
# 			re.save(path)
# 			print(path)
# 			splitpath=path.split('.')
# 			types=splitpath[1]
# 			print(types)
# 			if types=='txt':
# 				value=txtreader(path)
# 			if types=='docx':
# 				value=docreader(path)
# 			if types=='pdf':
# 				value=pdfreader(path)
# 			print(value)
# 			prediction =  predictor.predict([value])


			
# 			# p=request.form['p']
# 			q="insert into application values(null,'%s',curdate(),'%s','')"%(id,path)
# 			insert(q)
# 			flash('send successfully')
# 			return redirect(url_for('user.usersendapplication'))
# 		return render_template("usersendapplication.html",data=data)







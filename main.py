from flask import *
from public import public
from admin import admin
from company import company
# from user import user
from api import api



# /////////////////////////////////
# from math import sqrt
# from flask import Flask, render_template, request, jsonify
# from __future__ import division
# from collections import Counter
from flask import Flask, request
# from predict import Predictor
# from model import Model
# import pickle
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import json
# from bson import json_util
from PyPDF2 import PdfFileReader
from flask import *
from database import *
import uuid

from functions import *



# /////////////////////////////////////////

# import os
# from flask_cors import CORS
# from difflib import SequenceMatcher
# from flask import Flask, request, jsonify

# import joblib
# from flask_restful import reqparse
# from bson.json_util import dumps



# ////////////////////////////////////////

# M = Model()
# predictor = Predictor()

app=Flask(__name__)
app.secret_key='j'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(company,url_prefix='/company')
# app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(api,url_prefix='/api')

# app.run(debug=True,port=5111,host="192.168.43.9	4")
# CORS(app)
# parse = reqparse.RequestParser()

# model = joblib.load('model.pkl')
# prediction = model.predict([[9,1,9,3,4,5,9]])[0]
# print(prediction)

@app.route('/userhome',methods=['get','post'])
def userhome():
	data={}
	q="select * from team inner join teammember using(team_id) inner join user using(user_id) WHERE teammember.user_id='%s'"%(session['id'])
	res=select(q)
	print(res)


	if res:
		data['team']=res
		q="select * from teammember inner join user using(user_id) WHERE team_id='%s'"%(data['team'][0]['team_id'])
		res=select(q)
		if res:
			data['member']=res

	else:
		data['team']="team"
	q="select * from user WHERE user_id='%s'"%(session['id'])
	data['user']=select(q)

	q="select * from application WHERE user_id='%s'"%(session['id'])
	res=select(q)
	if res:
		data['per']=res[0]['personality']
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		mail=request.form['mail']
		q="update user set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where user_id='%s'"%(fname,lname,place,phone,mail,session['id'])
		update(q)
		return redirect(url_for('userhome'))
	return render_template("userhome.html",data=data)
	
# @app.route('/my_team',methods=['get','post'])
# def my_team():
# 	data={}
# 	q="select * from team inner join teammember using(team_id) inner join user using(user_id) WHERE teammember.user_id='%s'"%(session['id'])
# 	res=select(q)
# 	print(res)

# 	if res:
# 		data['team']=res
# 		q="select * from teammember inner join user using(user_id) WHERE team_id='%s'"%(data['team'][0]['team_id'])
# 		res=select(q)
# 		if res:
# 			data['member']=res

# 	else:
# 		data['team']="team"

# 	return render_template("my_team.html",data=data)


@app.route('/usersendcomplaint',methods=['get','post'])
def usersendcomplaint():
	data={}

	if 'submit' in request.form:
		comp=request.form['comp']
		q="INSERT INTO `complaint`(`user_id`,`user_type`,`complaint`,`reply`,`date`) VALUES ('%s','user','%s','status pending',CURDATE())"%(session['id'],comp)
		insert(q)
		flash('COMPLAINT DELIVERED')
		return redirect(url_for('usersendcomplaint'))
	q="SELECT * FROM `complaint` WHERE `user_id`='%s' AND `user_type`='user'"%(session['id'])
	data['complaint']=select(q)
	return render_template("usersendcomplaint.html",data=data)




@app.route('/userviewjob',methods=['get','post'])
def userviewjob():
	data = {}

	# Returns the current local date
	from datetime import datetime
	cd=datetime.today().strftime('%Y-%m-%d')
	print(cd)
	print(type(cd))


	q = "SELECT * FROM `job` INNER JOIN `company` USING (`company_id`) where last_date >= '%s'"%(cd)
	print(q)
	data['job'] = select(q)
	

	return render_template("userviewjob.html", data=data)

	



@app.route('/usersendapplication',methods=['get','post'])
def usersendapplication():
	if "job_id" in request.args:
		session['job_id']=jid=request.args['job_id']
		session['company_id']=request.args['company_id']
	data={}
	
	
	sid=session['id']
	
	q="select * from application WHERE user_id='%s' and job_id='%s'"%(sid,session['job_id'])
	res=select(q)
	print(id)
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	if res:
		flash("YOU ALREADY REQUESTED")	
		return redirect(url_for('userviewjob'))	

	# q="SELECT `question_id` FROM `questions`  order by question_id"
	# qpos=int(request.args['qpos'])
	# print(qpos)
	# qid=select(q)
	# if qpos==0:
	# 	q="delete from answers WHERE user_id='%s'"%(sid)	
	# 	delete(q)

	# if qid:
	# 	if qpos< len(qid):
	# 		print("######################")
	# 		ques=qid[qpos]['question_id']
	# 		print(ques)
	# 		data['ques']=ques
	# 		last=qid[-1]['question_id']
	# 		data['last']=last
	# 		q="SELECT * FROM `questionanswer` INNER JOIN `questions` USING(`question_id`) WHERE `questionanswer`.`question_id`='%s'"%(ques)
	# 		data['qno']=qpos+1
	# 		data['qans']=select(q)
	# 	else:	
	# 		print("888888888888888888888888")
	# 		data['app']='hello'

	# if 'submit' in request.form:
	# 	ans=request.form['ans']

	# 	print("...................."+ans)
		
	# 	q="insert into answers values(NULL,'%s','%s')"%(session['id'],ans)
	# 	insert(q)
	

	# 	qpos=request.form['nextqno']
	# 	print(ques)	

	# 	return redirect(url_for('usersendapplication',qpos=qpos))

	if "send" in request.form:
		age=request.form['age']
		gender=request.form['gender']
		re=request.files['re']
		skill=request.form['skill']
		path='static/uploads/'+str(uuid.uuid4())+re.filename
		re.save(path)
		print(path)
		splitpath=path.split('.')
		types=splitpath[1]
		print(types)
		value=""
		if types=='txt':
			value=txtreader(path)
		if types=='docx':
			value=docreader(path)
		if types=='pdf':
			value=pdfreader(path)
		print(value)
		# prediction =  predictor.predict([value])
		# print(prediction['pred_sOPN'])
		# print(prediction['pred_sCON'])
		# print(prediction['pred_sEXT'])
		# print(prediction['pred_sAGR'])
		# print(prediction['pred_sNEU'])

		# parm1 = int(gender)
		# parm2 = int(age)
		# parm3 = int(prediction['pred_sOPN'])
		# parm4 = int(prediction['pred_sCON'])
		# parm5 = int(prediction['pred_sEXT'])
		# parm6 = int(prediction['pred_sEXT'])
		# parm7 = int(prediction['pred_sNEU'])

		# prediction = model.predict([[parm1, parm2, parm3, parm4,parm5, parm6, parm7]])[0]

		# print(prediction)
		q="SELECT SUM(mark) FROM `answers` WHERE user_id='%s'"%(session['id'])
		print(q)
		res=select(q)
		point=res[0]['SUM(mark)']

		
		# p=request.form['p']
		q="insert into application values(null,'%s',curdate(),'%s',0,'%s','%s','%s','%s','pending')"%(session['id'],path,skill,point,session['job_id'],session['company_id'])
		insert(q)
		flash('send successfully')
		return redirect(url_for('userhome'))

	# if 'nxtsubmit' in request.form:
	# 	anss=request.form['anss']

		
			
	# 	q="insert into answers values(NULL,'%s','%s','%s')"%(ans,sid,res[0]['maximum_mark'])
	# 	insert(q)
	# 	return redirect(url_for('student.usersendapplication',action='next',nid=nid))

	return render_template('userapp.html',data=data)

@app.route('/userviewtest',methods=['get','post'])
def userviewtest():
	if "cid" in request.args:
		session['com_id']=request.args['cid']
	data={}
	uid=session['id']
	# qty="SELECT * FROM `test_type`"
	qty="SELECT * FROM `test_type` WHERE `test_type_id` NOT IN(SELECT `test_type_id` FROM `answer` INNER JOIN `user` USING(`user_id`) INNER JOIN `company` USING(`company_id`) WHERE `company_id`='%s' AND `user_id`='%s' )"%(session['com_id'],uid)
	# qty="SELECT * FROM `test_type` WHERE  `test_type_id` not IN (SELECT `test_type_id` FROM `answer` where user_id='%s')"%(uid)
	# print(qty)
	# qty="SELECT * FROM `test_type` INNER JOIN `online_test` USING(`test_type_id`) WHERE  `test_type_id` NOT IN (SELECT `test_type_id` FROM `answer`  INNER JOIN `online_test` USING (`test_type_id`) WHERE user_id='%s' AND `company_id`='%s')  GROUP BY `test_type_id` "%(uid,session['com_id'])
	print(qty)
	# qty="SELECT * FROM `test_type` INNER JOIN `online_test` USING(`test_type_id`) where company_id='%s'"%(session['com_id'])
	val=select(qty)
	# if val:
	# 	flash("already attend")

	# s="select * from test_type"
	data['res']=val
	if 'action' in request.args:
		session['test_typ_id']=id=request.args['id']
		data={}

		qry="select * from online_test where test_type_id='%s' and company_id='%s'"%(id,session['com_id'])
		# print(qry)
		data['res1']=select(qry)
		if 'submit' in request.form:
			j=1
			a=0
			counter = 0
			for i in data['res1']:
				counter += 1
				radio=request.form["ans"+str(j)]
				if i['correct_option']==radio:
					a=a+1
					
				j=j+1
			print(a,counter)
		
           
			qry="insert into answer values(null,'%s','%s','%s','%s',curdate(),'attend','%s')"%(session['test_typ_id'],uid,a,counter,session['com_id'])
			session['ansid']=insert(qry)
			return redirect(url_for('viewscore'))


	return render_template("userviewtest.html",data=data)

@app.route('/viewscore')
def viewscore():
	data={}
	qry="select mark_awarded,grand_total from answer where answer_id='%s'"%(session['ansid'])
	data['res']=select(qry)
	return render_template("userviewscore.html",data=data)

@app.route('/userapplication')
def userapplication():
	data={}
	qry="select * from application inner join company using(company_id) where user_id='%s'"%(session['id'])
	data['res']=select(qry)
	return render_template("userapplication.html",data=data)
@app.route('/userviewcompany')
def userviewcompany():
	data={}
	qry="select * from company"
	data['res']=select(qry)
	return render_template("userviewcompany.html",data=data)


# @user.route('/userattendexam',methods=['get','post'])
# def userattendexam():
# 	data={}
# 	testid=request.args['typeid']
# 	qry="select * from online_test where test_type_id='%s'"%(testid)
# 	data['res']=select(qry)
# 	return render_template("userattendexam.html",data=data)




# @app.route('/usersendcomplaint',methods=['get','post'])
# def usersendcomplaint():
# 	data={}

# 	if 'submit' in request.form:
# 		comp=request.form['comp']
# 		q="INSERT INTO `complaint`(`user_id`,`user_type`,`complaint`,`reply`,`date`) VALUES ('%s','user','%s','pending',CURDATE())"%(session['id'],comp)
# 		insert(q)
# 		flash('COMPLAINT DELIVERED')
# 		return redirect(url_for('user.usersendcomplaint'))
# 	q="SELECT * FROM `complaint` WHERE `user_id`='%s' AND `user_type`='user'"%(session['id'])
# 	data['complaint']=select(q)
# 	return render_template("usersendcomplaint.html",data=data)




# @app.route('/usersendapplication',methods=['get','post'])
# def usersendapplication():
# 		data={}
		
# 		id=session['id']
# 		q="select * from application WHERE user_id='%s'"%(id)
# 		res=select(q)
# 		print(id)
# 		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# 		if res:
# 			flash("YOU ALREADY REQUESTED")	
# 			return redirect(url_for('my_team'))	
# 		# q="SELECT *,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user` FROM `application` INNER JOIN `job` USING (`job_id`) INNER JOIN `company` USING (`company_id`) INNER JOIN `user` USING (`user_id`) ORDER BY `application_id`DESC"
# 		else:
# 			if "submit" in request.form:
# 				age=request.form['age']
# 				gender=request.form['gender']
# 				re=request.files['re']
# 				skill=request.form['skill']
# 				path='static/uploads/'+str(uuid.uuid4())+re.filename
# 				re.save(path)
# 				print(path)
# 				splitpath=path.split('.')
# 				types=splitpath[1]
# 				print(types)
# 				value=""
# 				if types=='txt':
# 					value=txtreader(path)
# 				if types=='docx':
# 					value=docreader(path)
# 				if types=='pdf':
# 					value=pdfreader(path)
# 				print(value)
# 				prediction =  predictor.predict([value])
# 				print(prediction['pred_sOPN'])
# 				print(prediction['pred_sCON'])
# 				print(prediction['pred_sEXT'])
# 				print(prediction['pred_sAGR'])
# 				print(prediction['pred_sNEU'])

# 				parm1 = int(gender)
# 				parm2 = int(age)
# 				parm3 = int(prediction['pred_sOPN'])
# 				parm4 = int(prediction['pred_sCON'])
# 				parm5 = int(prediction['pred_sEXT'])
# 				parm6 = int(prediction['pred_sEXT'])
# 				parm7 = int(prediction['pred_sNEU'])

# 				prediction = model.predict([[parm1, parm2, parm3, parm4,parm5, parm6, parm7]])[0]

# 				print(prediction)
	          
				
# 				# p=request.form['p']
# 				q="insert into application values(null,'%s',curdate(),'%s','%s','%s')"%(id,path,prediction,skill)
# 				insert(q)
# 				flash('send successfully')
# 				return redirect(url_for('userhome'))
# 		return render_template("usersendapplication.html",data=data)




app.run(debug=True,port=5330,host="0.0.0.0")
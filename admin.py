from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)

@admin.route('/admin_home',methods=['get','post'])
def admin_home():
	if not session.get("lid") is None:
		data={}
		return render_template("admin_home.html",data=data)
	else:
		return redirect(url_for('public.login'))





@admin.route('/admin_Manage_company',methods=['get','post'])
def admin_Manage_company():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `company`"
		data['company']=select(q)
		if 'submit' in request.form:
			company=request.form['company']
			place=request.form['place']
			phno=request.form['phno']
			email=request.form['email']
			uname=request.form['uname']
			pwd=request.form['pwd']
			q="SELECT * FROM `login` WHERE `username`='%s'"%(uname)
			res=select(q)
			if res:
				flash('USERNAME ALREADY EXIST')
				return redirect(url_for("admin.admin_Manage_company"))
			else:
				q="INSERT INTO `login`(`username`,`password`,`usertype`) VALUES ('%s','%s','company')"%(uname,pwd)
				id=insert(q)
				q="INSERT INTO `company`(`login_id`,`company`,`place`,`phone`,`email`) VALUES ('%s','%s','%s','%s','%s')"%(id,company,place,phno,email)
				insert(q)
				flash('REGISTERED')
				return redirect(url_for("admin.admin_Manage_company"))
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="DELETE FROM company WHERE login_id='%s'"%(id)
			delete(q)
			q="DELETE FROM login WHERE login_id='%s'"%(id)
			delete(q)
			flash('COMPANY DETAILS DELETED')
			return redirect(url_for('admin.admin_Manage_company'))
		if action=='update':
			q="SELECT * FROM company WHERE login_id='%s'"%(id)
			data['com_up']=select(q)
		if 'updatez' in request.form:
			company=request.form['company']
			place=request.form['place']
			phno=request.form['phno']
			email=request.form['email']
			
			q="UPDATE `company` SET `company`='%s',`place`='%s',`phone`='%s',`email`='%s'  WHERE login_id='%s'"%(company,place,phno,email,id)

			update(q)
			flash('COMPANY DETAILS UPDATED')
			return redirect(url_for('admin.admin_Manage_company'))
		return render_template("admin_Manage_company.html",data=data)
	else:
		return redirect(url_for('public.login'))



@admin.route('/admin_view_job')
def admin_view_job():
	data={}
	cmid=request.args['id']
	s="select * from job where company_id='%s'"%(cmid)
	data['job']=select(s)
	return render_template("admin_view_job.html",data=data)
@admin.route('/admin_manage_team_members',methods=['get','post'])
def admin_manage_team_members():
	if not session.get("lid") is None:
		data={} 	
		tid=request.args['tid']
		q="select * from user"
		res=select(q)
		data['s']=res

		q="select * from teammember inner join user using(user_id) inner join application using(user_id) where team_id='%s'"%(tid)
		res=select(q)
		print(res)
		data['us']=res
		print(res)
		
		q="select * from team where team_id='%s'"%(tid)
		res=select(q)
		if res:
			team=int(res[0]['no_of_members'])
			print(team)

			q="select * from teammember where team_id='%s'"%(tid)
			res=select(q)
			if res:
				l=len(res)
				print(l)
				if int(l)>=int(team):
					flash("already filled")
					return redirect(url_for('admin.admin_Manage_team'))

		if 'submit' in request.form:
		
			user_id=request.form['user']
			q="SELECT * from teammember where team_id='%s' and user_id='%s'"%(tid,user_id)
			res=select(q)
			if res:
				flash("User is already added") 
			else:
				q="INSERT INTO `teammember` VALUES(null,'%s','%s')"%(user_id,tid)
				insert(q)
				flash('ADDED')
				return redirect(url_for('admin.admin_manage_team_members',tid=tid))
		return render_template("admin_manage_team_members.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_view_team_members',methods=['get','post'])
def admin_view_team_members():
	if not session.get("lid") is None:
		data={}
		tid=request.args['tid']


		q="select * from teammember inner join user using(user_id) inner join application using (user_id) where team_id='%s' group by user_id"%(tid)
		res=select(q)
		print(res)
		data['us']=res
		return render_template("admin_view_team_members.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_View_resume',methods=['get','post'])
def admin_View_resume():
	if not session.get("lid") is None:
		data={}
		q="SELECT *,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user` FROM `application`  INNER JOIN `user` USING (`user_id`) group by user_id ORDER BY `application_id`DESC "
		data['resume']=select(q)
		return render_template("admin_View_resume.html",data=data)
	else:
		return redirect(url_for('public.login'))





@admin.route('/admin_Sent_personality',methods=['get','post'])
def admin_Sent_personality():
	if not session.get("lid") is None:
		data={}
		return render_template("admin_Sent_personality.html",data=data)
	else:
		return redirect(url_for('public.login'))
	
@admin.route('/admin_manage_testtype',methods=['get','post'])
def admin_manage_testtype():
	data={}
	s="select * from test_type"
	data['test']=select(s)

	if 'submit' in request.form:
		test=request.form['test']
		qry="insert into test_type values(null,'%s')"%(test)
		insert(qry)
		flash("Test type added")
		return redirect(url_for('admin.admin_manage_testtype'))

	if 'action' in request.args:
		action=request.args['action']
		tid=request.args['tid']
	else:
		action=None
	if action=="update":
		s="select * from test_type where test_type_id='%s'"%(tid)
		data['edit']=select(s)
		if 'edit' in request.form:
			test=request.form['test']
			qry="update test_type set type='%s' where test_type_id='%s'"%(tid)
			insert(qry)
			flash("Test type added")
			return redirect(url_for('admin.admin_manage_testtype'))
		
	if action=="delete":
			q="delete from test_type where test_type_id='%s'"%(tid)
			delete(q)
			flash("Test type removed")
			return redirect(url_for('admin.admin_manage_testtype'))

	return render_template("admin_manage_testtype.html",data=data)





@admin.route('/admin_View_complaint',methods=['get','post'])
def admin_View_complaint():
	if not session.get("lid") is None:
		data={}
		q="(SELECT CONCAT(`user`.`fname`,' ',`user`.`lname`,'(user)') AS `user`,`complaint`,`reply`,`date`,`complaint_id` FROM `complaint` INNER JOIN `user` USING (`user_id`) WHERE `user_type`='user') UNION (SELECT concat (`company`.`company`,'(company)') AS `user`,`complaint`,`reply`,`date`,`complaint_id` FROM `complaint` INNER JOIN `company` ON (`complaint`.`user_id`=`company`.`company_id`) WHERE `user_type`='company' ORDER BY `reply` DESC) ORDER BY `complaint_id` DESC"
		data['complaint']=res=select(q)
		for i in range (1,len(res)+1):
			print(i)
			if 'submit'+str(i) in request.form:
				print('hell')
				reply=request.form['reply'+str(i)]
				id=request.form['id'+str(i)]
				q="UPDATE `complaint` SET `reply`='%s' WHERE `complaint_id`='%s'"%(reply,id)
				update(q)
				flash('REPLY DELIVERED')
				return redirect(url_for('admin.admin_View_complaint'))
		return render_template("admin_View_complaint.html",data=data)
	else:
		return redirect(url_for('public.login'))



# @admin.route('/admin_managequest',methods=['get','post'])
# def admin_managequest():
# 	data={}
# 	q="select * from questions"	
# 	res=select(q)
# 	l=len(res)
# 	# if int(l)>=5:
# 	# 	data["filled"]="hello"
# 	if 'submit' in request.form:
# 		quest=request.form['quest']
		
# 		q="insert into questions values(NULL,'%s')"%(quest)
# 		insert(q)
# 		return redirect(url_for('admin.admin_managequest'))
# 	q="select * from questions"
# 	res=select(q)
# 	data['quest']=res
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		qid=request.args['qid']
# 		quest=request.args['quest']
# 	else:
# 		action=None
# 	if action=='delete':
# 		q="delete from questions where question_id='%s'"%(qid)
# 		delete(q)
# 		q="delete from questionanswer where question_id='%s'"%(qid)
# 		delete(q)
# 		return redirect(url_for('admin.admin_managequest'))
# 	return render_template('admin_managequest.html',data=data)

# @admin.route('/admin_addop',methods=['get','post'])
# def admin_addop():
# 	data={}

# 	quest=request.args['quest']
# 	qid=request.args['qid']
# 	if 'submit' in request.form:
# 		option=request.form['option']
# 		mark=request.form['mark'] 
# 		q="insert into questionanswer values(NULL,'%s','%s','%s')"%(qid,option,mark)
# 		insert(q)
# 		return redirect(url_for('admin.admin_addop',quest=quest,qid=qid))
# 	q="select * from questionanswer where question_id='%s'"%(qid)
# 	res=select(q)
# 	data['option']=res
# 	l=[1,2,3,4,5]
# 	mark=[]
# 	if res:
# 		for  i in res:
# 			mark=mark+[i['mark']]
# 	print(mark)
# 	for i in mark:
# 		i=int(i)
# 		if i in l:
# 			l.remove(i)
# 	data['l']=l
# 	print(l)
# 	if 'action' in request.args:
# 		oid=request.args['oid']
# 		q="delete from questionanswer where qstansr_id='%s'"%(oid)
# 		delete(q)
# 		return redirect(url_for('admin.admin_addop',quest=quest,qid=qid))
# 	return render_template('admin_addop.html',quest=quest,qid=qid,data=data)



# @admin.route('/admin_home',methods=['get','post'])
# def admin_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("admin_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))





# @admin.route('/admin_home',methods=['get','post'])
# def admin_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("admin_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))






from flask import *
from database import *
import uuid
company=Blueprint('company',__name__)

@company.route('/company_home',methods=['get','post'])
def company_home():
	if not session.get("lid") is None:
		data={}
		qry="select * from company where company_id='%s'"%(session['cpnyid'])
		data['res']=select(qry)
		if 'submit' in request.form:
			name=request.form['cname']
			place=request.form['place']
			phone=request.form['phone']
			mail=request.form['email']
			q="update company set company='%s',place='%s',phone='%s',email='%s' where company_id='%s'"%(name,place,phone,mail,session['cpnyid'])
			update(q)
			return redirect(url_for('company.company_home'))
		return render_template("company_home.html",data=data)
	else:
		return redirect(url_for('public.login'))

# @company.route('/company_Manage_team',methods=['get','post'])
# def company_Manage_team():
# 	if not session.get("lid") is None:
# 		data={}
		
# 		q="SELECT * FROM `team` where company_id='%s'"%(session['cpnyid'])
# 		data['team']=select(q)
		
# 		if 'submit' in request.form:
# 			team=request.form['team']
# 			member=request.form['member']
# 			skill=request.form['skill']
# 			# job=request.form['job']
# 			q="INSERT INTO `team` VALUES (null,'%s','%s','%s','%s')"%(team,member,skill,session['id'])
# 			id=insert(q)
# 			flash('added')
# 			return redirect(url_for("company.company_Manage_team"))
# 		if 'action' in request.args:
# 			action=request.args['action']
# 			id=request.args['id']
# 		else:
# 			action=None
# 		if action=='delete':
# 			q="DELETE FROM team WHERE team_id='%s'"%(id)
# 			delete(q)
# 			q="DELETE FROM teammember WHERE team_id='%s'"%(id)
# 			delete(q)
# 			flash('TEAM DELETED')
# 			return redirect(url_for('company.company_Manage_team'))

# 		if action=="add_member":

# 			q="select * from team where team_id='%s'"%(id)
# 			res=select(q)
# 			skill=res[0]['skill']
# 			print(skill)
			
			
# 			if res:
# 				team=int(res[0]['no_of_members'])
# 				print(team)

# 				q="select * from teammember where team_id='%s'"%(id)
# 				res=select(q)
# 				if res:
# 					l=len(res)
# 					print(l)
# 					if int(l)>=int(team):
# 						flash("already filled")
# 						return redirect(url_for('company.company_Manage_team'))
# 					# if int(l)<=int(team) and int(l)>4:
# 					elif int(l)<=int(team):
# 						q1="select user_id from teammember"
# 						q2=select(q1)
# 						print(q1)
# 						print("***************************************")
# 						q="select * from user inner join application using(user_id) where user_id not in('%s') and application.skill='%s' and application.company_id='%s' order by FIELD(personality,'responsible','dependable','serious','lively','extraverted') "%(q1,skill,session['id'])
# 						print(q,"pppppppppppp")
# 						res=select(q)
# 						print(res)
# 						print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# 						if res:
# 							personality=res[0]['personality']
							
# 							q="select * from `user` inner join `application` using(user_id) where user_id not in('%s') and application.skill='%s' and personality='%s' order by mark desc"%(q1,skill,personality)
# 							print(q)
# 							res=select(q)
# 							uid=res[0]['user_id']

# 							print(uid)
# 							q="SELECT * from teammember where  user_id='%s'"%(uid)
# 							res=select(q)
# 							if res:
# 								flash("User is already added") 
# 								return redirect(url_for('company.company_Manage_team'))
# 							else:
# 								q="insert into teammember values(null,'%s','%s')"%(uid,id)
# 								insert(q)
# 								print(q)
# 								flash("members added")
# 								return redirect(url_for('company.company_Manage_team'))
# 						else:
# 							flash("No User Available")
# 							return redirect(url_for('company.company_Manage_team'))
# 					else:
# 						q1="select user_id from teammember"
# 						q="SELECT personality FROM `application` INNER JOIN `user` USING(user_id) INNER JOIN `teammember` USING(user_id) where team_id='%s' "%(id)
# 						print(q)
# 						r=select(q)
# 						print(r)
# 						q="select * from user inner join application using(user_id) where personality not in (%s) and user_id not in(%s) and skill='%s' order by FIELD(personality,'responsible','dependable','serious','lively','extraverted')"%(q,q1,skill)
# 						print(q)
# 						res=select(q)
# 						print("++++++++++++++++++++++++++++++++")
# 						print(res)
# 						if res:
# 							personality=res[0]['personality']
							
# 							q="select * from user inner join application using(user_id) where user_id not in(%s) and application.skill='%s' and personality='%s' order by mark desc"%(q1,skill,personality)
# 							print(q)
# 							res=select(q)
						
# 							uid=res[0]['user_id']
# 							print(uid)
# 							q="SELECT * from teammember where  user_id='%s'"%(uid)
# 							res=select(q)
# 							if res:
# 								flash("User is already added") 
# 								return redirect(url_for('company.company_Manage_team'))
# 							else:
# 								q="insert into teammember values(null,'%s','%s')"%(uid,id)
# 								insert(q)
# 								print(q)
# 								flash("members added")
# 								return redirect(url_for('company.company_Manage_team'))
# 						else:
# 							flash("No User Available")
# 							return redirect(url_for('company.company_Manage_team'))



# 				else:


# 					q1="select user_id from teammember"
					
# 					q="select * from user inner join application using(user_id) where user_id not in(%s) and skill='%s' "%(q1,skill)
# 					print(q)
# 					res=select(q)
# 					print(res)
# 					if res:
# 						personality=res[0]['personality']
							
# 						q="select * from user inner join application using(user_id) where user_id not in(%s) and application.skill='%s' and personality='%s' order by mark desc"%(q1,skill,personality)
# 						print(q)
# 						res=select(q)
# 						uid=res[0]['user_id']
# 						print(uid)
# 						q="SELECT * from teammember where  user_id='%s'"%(uid)
# 						res=select(q)
# 						if res:
# 							flash("User is already added") 
# 						else:
# 							q="insert into teammember values(null,'%s','%s')"%(uid,id)
# 							insert(q)
# 							print(q)
# 							flash("members added")
# 					else:
# 						flash("No User Available")
# 						return redirect(url_for('company.company_Manage_team'))

					
# 		if action=='update':
# 			q="SELECT * FROM team WHERE team_id='%s'"%(id)
# 			data['com_up']=select(q)
# 		if 'updatez' in request.form:
# 			team=request.form['team']
# 			member=request.form['member']
			
# 			q="UPDATE `team` SET `team`='%s',`no_of_members`='%s'  WHERE team_id='%s'"%(team,member,id)

# 			update(q)
# 			flash('team DETAILS UPDATED')
# 			return redirect(url_for('company.company_Manage_team'))
# 		return render_template("company_Manage_team.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))


# @company.route('/company_view_team_members',methods=['get','post'])
# def company_view_team_members():
# 	if not session.get("lid") is None:
# 		data={}
# 		tid=request.args['tid']


# 		q="select * from teammember inner join user using(user_id) inner join application using (user_id) where team_id='%s' group by user_id"%(tid)
# 		res=select(q)
# 		print(res)
# 		data['us']=res
# 		return render_template("company_view_team_members.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))


@company.route('/company_Manage_job',methods=['get','post'])
def company_Manage_job():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM job WHERE `company_id`='%s'"%(session['cpnyid'])
		data['job']=select(q)
		if 'submit' in request.form:
			job=request.form['job']
			det=request.form['det']
			date=request.form['date']
			q="INSERT INTO `job`(`company_id`,`job`,`details`,`last_date`) VALUES ('%s','%s','%s','%s')"%(session['id'],job,det,date)
			insert(q)
			flash('JOB DETAILS ADDED')
			return redirect(url_for('company.company_Manage_job'))
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="DELETE FROM job WHERE job_id='%s'"%(id)
			delete(q)
			
			flash('JOB DETAILS DELETED')
			return redirect(url_for('company.company_Manage_job'))
		if action=='update':
			q="SELECT * FROM job WHERE job_id='%s'"%(id)
			data['job_up']=select(q)
		if 'updatez' in request.form:
			job=request.form['job']
			det=request.form['det']
			date=request.form['date']
			q="UPDATE `job` SET `job`='%s',`details`='%s',`last_date`='%s'  WHERE job_id='%s'"%(job,det,date,id)
			
			update(q)
			flash('JOB DETAILS UPDATED')
			return redirect(url_for('company.company_Manage_job'))
		return render_template("company_Manage_job.html",data=data)
	else:
		return redirect(url_for('public.login'))





@company.route('/company_View_application',methods=['get','post'])
def company_View_application():
	if not session.get("lid") is None: 
		data={}
		jid=request.args['jid']
		data['jid']=jid
		print(jid)
		# q="SELECT *,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user` FROM `application` INNER JOIN `job` ON application.company_id=job.company_id INNER JOIN `company` ON application.company_id=company.company_id INNER JOIN `user` ON application.`user_id`=`user`.`user_id` WHERE job.job_id='%s' ORDER BY `application_id`DESC"%(jid)
		# q="SELECT *,`test_type`.`type` AS testtype,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user`,answer.mark_awarded AS mark FROM `application` INNER JOIN `job` USING(job_id)  INNER JOIN `company` ON company.company_id=application.company_id INNER JOIN `user` USING(user_id) INNER JOIN answer USING (user_id) INNER JOIN `test_type` USING(`test_type_id`)  WHERE job_id='%s' group by test_type_id ORDER BY `application_id`  DESC"%(jid)
# 		q="""SELECT *,`test_type`.`type` AS testtype,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user`,answer.mark_awarded AS mark 
# FROM `application` INNER JOIN `job` USING(job_id)  INNER JOIN `company` ON company.company_id=application.company_id 
# INNER JOIN `user` USING(user_id) INNER JOIN answer USING (user_id) INNER JOIN `test_type` USING(`test_type_id`) 
#  WHERE job_id='%s' and company.company_id='%s' ORDER BY `application_id`  DESC"""%(jid,session['cpnyid'])
		q="""SELECT *,`test_type`.`type` AS testtype,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS `user`,answer.mark_awarded AS mark 
FROM `application` INNER JOIN `job` USING(job_id)  INNER JOIN `company` ON company.company_id=application.company_id 
INNER JOIN `user` USING(user_id) INNER JOIN answer USING (user_id) INNER JOIN `test_type` USING(`test_type_id`) 
 WHERE job_id='%s' and application.company_id='%s' group by application_id ORDER BY `application_id`  DESC"""%(jid,session['cpnyid'])
		print(q)
		data['resume']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			applicatoion_id=request.args['applicatoion_id']
		else:
			action=None
		if action=='accept':
			q="UPDATE `application` SET `application_status`='You Are Selected' WHERE `application_id`='%s'"%(applicatoion_id)
			update(q)
			return redirect(url_for('company.company_View_application',jid=jid))
		if action=='reject':
			q="UPDATE `application` SET `application_status`='You Are Rejected' WHERE `application_id`='%s'"%(applicatoion_id)
			update(q)
			return redirect(url_for('company.company_View_application',jid=jid))
	
  
		return render_template("company_View_application.html",data=data,)
	else:
		return redirect(url_for('public.login'))



@company.route('/com_view_test_user_mark',methods=['get','post'])
def com_view_test_user_mark():
	if not session.get("lid") is None:
		data={}
		uid=request.args['uid']
		com_id=session['cpnyid']
		jid=request.args['jbid']

		qq="""SELECT * FROM `answer` INNER JOIN `test_type` USING(`test_type_id`) WHERE `company_id`='%s' AND `user_id`='%s'"""%(com_id,uid)
		print(qq)
		res=select(qq)
		if res:
			data['resume']=res

		return render_template("com_view_test_user_mark.html",data=data)
	else:
		return redirect(url_for('public.login'))






@company.route('/company_View_resume',methods=['get','post'])
def company_View_resume():
	if not session.get("lid") is None:
		data={}
		return render_template("company_View_resume.html",data=data)
	else:
		return redirect(url_for('public.login'))





@company.route('/company_Sent_complaint',methods=['get','post'])
def company_Sent_complaint():
	if not session.get("lid") is None:
		data={}
		if 'submit' in request.form:
			comp=request.form['comp']
			q="INSERT INTO `complaint`(`user_id`,`user_type`,`complaint`,`reply`,`date`) VALUES ('%s','company','%s','status pending',CURDATE())"%(session['id'],comp)
			insert(q)
			flash('COMPLAINT DELIVERED')
			return redirect(url_for('company.company_Sent_complaint'))
		q="SELECT * FROM `complaint` WHERE `user_id`='%s' AND `user_type`='company'"%(session['id'])
		data['complaint']=select(q)
		return render_template("company_Sent_complaint.html",data=data)
	else:
		return redirect(url_for('public.login'))





# @company.route('/company_home',methods=['get','post'])
# def company_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("company_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))





# @company.route('/company_home',methods=['get','post'])
# def company_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("company_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))




@company.route('/company_addtest',methods=['get','post'])
def company_addtest():
    data={}
    cid=session['id']
    s="select * from test_type"
    data['res']=select(s)
    if 'submit' in request.form:
        type=request.form['testtype']
        qstn=request.form['question']
        opt1=request.form['option1']
        opt2=request.form['option2']
        opt3=request.form['option3']
        copt=request.form['coption']
        qry="insert into online_test values(null,'%s','%s','%s','%s','%s','%s','%s')"%(type,qstn,opt1,opt2,opt3,copt,cid)
        insert(qry)

    qq="select * from online_test inner join test_type using(test_type_id) where company_id='%s'"%(cid)
    res=select(qq)
    data['test']=res
    return render_template("company_addtest.html",data=data)

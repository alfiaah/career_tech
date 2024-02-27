from flask import *
from flask import *
from database import *
# import demjson
# from predict import predict
import uuid
# import cv2
# import io
import requests
from functions import *



api=Blueprint('api',__name__)

@api.route('/login')
def login():
	data={}
	
	username = request.args['username']
	password = request.args['password']
	q="SELECT * from login where username='%s' and password='%s'" % (username,password)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='login'
	return str(data)


@api.route('/userregister')
def userregister():
	data={}

	uname = request.args['uname']
	passs = request.args['pass']
	fname = request.args['fname']
	lname = request.args['lname']
	email = request.args['email']
	place = request.args['place']
	phone = request.args['phone']

	q="insert into login values(null,'%s','%s','user')" %(uname,passs)
	id=insert(q)
	q="insert into user values(null,'%s','%s','%s','%s','%s','%s')" %(id,fname,lname,phone,email,place) 
	insert(q)
	
	data['status']  = 'success'
	
	data['method']='userregister'
	return str(data)


@api.route('/UserViewJobs')
def UserViewJobs():
	data={}
	
	q="SELECT * from job"
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='UserViewJobs'
	return str(data)

@api.route('/UserViewcompany')
def UserViewcompany():
	data={}
	
	cid = request.args['cid']
	q="SELECT * from company where company_id='%s'" %(cid)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='UserViewcompany'
	return str(data)



@api.route('/UserViewrequests')
def UserViewrequests():
	data={}
	
	lid = request.args['lid']
	q="SELECT * from application inner join job using(job_id)  where user_id=(select user_id from user where login_id='%s')" %(lid)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='UserViewrequests'
	return str(data)




@api.route('/userviewcomplaint',methods=['get','post'])
def userviewcomplaint():
	data={}
	
	lid = request.args['lid']
	q="SELECT * from complaint where user_id=(select user_id from user where login_id='%s')" %(lid)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='userviewcomplaint'
	return str(data)

@api.route('/usersendcomplaint')
def usersendcomplaint():
	data={}

	lid = request.args['lid']
	comp = request.args['comp']

	q="insert into complaint values(null,(select user_id from user where login_id='%s'),'user','%s','pending',curdate())" %(lid,comp) 
	insert(q)
	
	data['status']  = 'success'
	
	data['method']='usersendcomplaint'
	return str(data)










# ////////////////////////////for Prediction



@api.route('/studentadduploadassignments/',methods=['get','post'])
def studentadduploadassignments():
	data={}
	
	
	logid = request.form['logid']
	aid = request.form['aid']
	image = request.files['image']

	q="select * from application where user_id=(select user_id from user where login_id='%s') and job_id='%s'" %(logid,aid)
	print(q)
	res=select(q)
	if res:
		data['val']="exist"
	else:
	

		path='static/uploads/'+str(uuid.uuid4())+image.filename
		image.save(path)
		print(path)
		
		# fn=secure_filename(image.filename)
		# image.save('./static/temp/'+fn)
		# with open('./static/temp/'+fn, "rb") as imageFile:
		

		splitpath=path.split('.')
		types=splitpath[1]
		print(types)
		if types=='txt':
			value=txtreader(path)
		if types=='docx':
			value=docreader(path)
		if types=='pdf':
			value=pdfreader(path)

		print(value)

		personality_type = predict(value)
		print(personality_type)

		
		
		q = "insert into application values(null,'%s',(select user_id from user where login_id='%s'),curdate(),'%s','%s')" % (aid,logid,path,personality_type)
		
		print(q)
		insert(q)
		
	
	data['status'] ="success"

	data['method']="studentadduploadassignments"
	returnstr(data)







# //////////////////////////////////////////
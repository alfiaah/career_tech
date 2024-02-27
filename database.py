import mysql.connector

password=''
database='career_techs_new'
port=3306

def select(q):
	cnx=mysql.connector.connect(user='root',host='localhost',password=password,database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	result=cur.fetchall()
	cnx.close()
	cur.close()
	return result

def delete(q):
	cnx=mysql.connector.connect(user='root',host='localhost',password=password,database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cnx.close()
	cur.close()
	return result

def update(q):
	cnx=mysql.connector.connect(user='root',host='localhost',password=password,database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cnx.close()
	cur.close()
	return result

def insert(q):
	cnx=mysql.connector.connect(user='root',host='localhost',password=password,database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.lastrowid
	cur.close()
	cnx.close()
	return result

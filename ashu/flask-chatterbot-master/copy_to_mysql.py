# -*- coding: utf-8 -*-
import sqlite3
import MySQLdb

sqlite_file = 'db.sqlite3'    # name of the sqlite database file
table_name = 'response'   # name of the table to be queried
id_column = 'id'
insertedRecords = 0
column_2 = 'text'
column_3 = 'statement_text'

#opening a file
#file=open('count.txt', 'r')
#count=file.readline()
#print("total number of records in database: "+ count)
#file.close()

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
db = MySQLdb.connect("163.25.101.53","root","admin","mytest" )
db.set_character_set('utf8')

#selecting data from sqlite
cur = conn.cursor()
mysqlcursor = db.cursor()
mysqlcursor.execute('SET NAMES utf8;')
mysqlcursor.execute('SET CHARACTER SET utf8;')
mysqlcursor.execute('SET character_set_connection=utf8;')

#cur.execute("SELECT * FROM response where id>?",int(count))
cur.execute("SELECT * FROM response")
rows = cur.fetchall()

for row in rows:
    (id, question, created_at, occurance, response) = tuple(row)
 #   id = int(count)+id
   # insertedRecords++
    print("id:" + str(id))
    print("question: " + question)
    print("answer: " + response)
    print()
    mysqlcursor.execute("""INSERT INTO RESPONSE VALUES (%s,%s,%s,%s)""",(id, question, response,occurance))

db.commit()
conn.close()

#count = int(count)+insertedRecords
#file1=open('count.txt', 'w')
#file1.write(count)
#file1.close()


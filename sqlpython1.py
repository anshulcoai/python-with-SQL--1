import mysql.connector

db={'host':'localhost', 'user':'root', 'password':'Anshul123456789@','database':'database_1'}
conn=mysql.connector.connect(**db)

myOutput=conn.cursor()
myOutput.execute('show tables')

print(conn)
result=myOutput.fetchall()

for i in result:
    print(i)
conn.close    

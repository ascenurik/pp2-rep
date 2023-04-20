# Obtaining data from SQL 

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="510149361Karim",
)

sql = "select * from phonebooks" 

cursor = conn.cursor() 
cursor.execute(sql) 
conn.commit()

contacts = cursor.fetchall()
for contact in contacts:
    print(contact)

cursor.close() 
conn.close()
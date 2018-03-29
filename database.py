import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("create table IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Tim', 123456, 'tim@gmail.com')")
db.execute("INSERT INTO contacts VALUES ('Marios', 654321, 'marios@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
#prints a list of all tuples that cursor object returns
# lst = cursor.fetchall()
# for result_set in lst:
#     print (result_set)
#     print ("_" * 20)
#prints empty list if cursor has been run through already
#print (cursor.fetchall())
print (cursor.fetchone())

print (cursor.fetchone())

print (cursor.fetchone())
for name, phone, email in cursor:
    print (name, phone, email, sep="-")
    print ("*" * 40)

cursor.close()
#if you fail to commit the changes they will be lost wehn you close the connection
db.commit()
db.close()
#querying the database with python




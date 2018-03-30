import sqlite3

db = sqlite3.connect("contacts.sqlite")
name = input("Please enter a name: ")

select_sql = "SELECT * FROM contacts WHERE name LIKE ?"
cursor = db.cursor()
result = cursor.execute(select_sql, (name,))
for row in result:
    print (row)
    print ("-"*20)
cursor.close()    
db.close()
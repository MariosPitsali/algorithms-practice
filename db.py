import sqlite3

db = sqlite3.connect("contacts.sqlite")

select_sql = "SELECT * FROM contacts"

for row in db.execute(select_sql):
    print (row)
    print ("-"*20)
    
db.close()
import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email='anotherupdate@update.com' WHERE contacts.phone= 654321"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
update_cursor.connection.commit()
print ("{} rows updated".format(update_cursor.rowcount))
for name,phone,email in db.execute("SELECT * FROM contacts"):
    print (name)
    print (phone)
    print (email)
    print ("-"*10)
    
db.close()
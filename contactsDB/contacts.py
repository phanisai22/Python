import sqlite3

db = sqlite3.connect("contacts.sqlite")
# db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT NOT NULL, phone INTEGER, email TEXT)")
# db.execute("INSERT INTO contacts(name, phone, email) VALUES('tony', 8247484098, 'tonystark@gmail.com')")
# db.execute("INSERT INTO contacts VALUES('phani sai', 9032203312, 'phanisai@gmail.com' )")
#
# cursor = db.cursor()
# cursor.execute("SELECT * FROM contacts")
#
# print("Name  | Phone No. | Email")
# for name, number, email in cursor:
#     print(name+" | "+str(number)+" | "+email)
#
# cursor.close()
#
# db.commit()
# it is important to commit the changes after adding data to the database .
# Not to loose the data after testing the program once .

# ===============================================================================================

# new_email = 'theRandomEmail@gmail.com'
# # update_sql = "UPDATE contacts SET email={} WHERE phone={}".format(new_email, 9032203312)
# update_cursor = db.cursor()
# number = input('Enter the phone number : ')
# update_cursor.execute("UPDATE contacts SET email='theRandomEmail@gmail.com' WHERE phone={}".format(number))
#
# print("{} rows has been updated .".format(update_cursor.rowcount))
#
# print()
# print("are the connections are same : {}".format(update_cursor.connection == db))
# print()
#
# update_cursor.connection.commit()
# update_cursor.close()
#
# print("Name  | Phone No. | Email")
# for name, number, email in db.execute("SELECT * FROM contacts"):
#     print(name+" | "+str(number)+" | "+email)

# =================================================================================================

name = input("enter the name to print his row : ")
cursor = db.cursor()
execute_statement = "SELECT * FROM contacts WHERE name=?"
cursor.execute(execute_statement, (name, ))

for name_, number, email in cursor:
    print(name_, number, email)

cursor.close()

db.close()

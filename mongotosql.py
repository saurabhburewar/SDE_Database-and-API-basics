import pymongo
import mysql.connector

# Creating a mongodb client
mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Creating connection to MySQL database
sqlconn = mysql.connector.connect(
    host="localhost", user="root", password="Saurabh@sql", database="librarydb")

# Creating table in MySQL
sqlcursor = sqlconn.cursor()
# sqlcursor.execute("drop table if exists books")
sqlcursor.execute("create table books (isbn varchar(16), accession_no varchar(16), title varchar(255), author varchar(255), publisher varchar(255), edition varchar(16), year_of_publication varchar(8), category varchar(16), total_number_of_pages varchar(8), price varchar(8))")


# Getting our Mongo database
dblist = mongoclient.list_database_names()
if "LibraryDB" not in dblist:
    print('Cannot find "LibraryDB" database...')

db = mongoclient["LibraryDB"]

# Getting collection from Mongo database
collist = db.list_collection_names()
if "Books" not in dblist:
    print('Cannot find "Books" collection in the database...')

col = db["Books"]

# Getting all documents in the collection in Mongo and adding them to MySQL table
doclist = []
for doc in col.find():
    doclist.append(doc)
    sqlvalues = []
    for key in doc:
        if key != "_id":
            sqlvalues.append(doc[key])

    sqlvalues = tuple(sqlvalues)
    sqltable = "insert into books (isbn, accession_no, title, author, publisher, edition, year_of_publication, category, total_number_of_pages, price) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sqlcursor.execute(sqltable, sqlvalues)
    sqlconn.commit()

# Printing the MySQL table entries
sqlcursor.execute("select * from books")
sqlresult = sqlcursor.fetchall()

print("\nSQL Database:")
for x in sqlresult:
    print(x)

# Start listening to changes in MongoDB database
print("\nListening to changes in MongoDB database...")
with col.watch() as stream:
    for change in stream:
        print("Change detected in Mongo:\n", change)
        if change['operationType'] == 'insert':
            dockey = change['documentKey']
            doc = col.find_one(dockey)
            sqlvalues = []
            for key in doc:
                if key != "_id":
                    sqlvalues.append(doc[key])

            sqlvalues = tuple(sqlvalues)
            sqltable = "insert into books (isbn, accession_no, title, author, publisher, edition, year_of_publication, category, total_number_of_pages, price) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            sqlcursor.execute(sqltable, sqlvalues)
            sqlconn.commit()

            sqlcursor.execute("select * from books")
            sqlresult = sqlcursor.fetchall()

            print("\nSQL database updated:")
            for x in sqlresult:
                print(x)

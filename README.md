# SDE_Database-and-API-basics

## MongoDB to MySQL

This program transfers data from MongoDB database to an SQL table. If left running in the background, it also detects the changes in MongoDB database and updates the SQL table accordingly.
- Setup and get the Mongo server and MySQL server running.
- Create the database in Mongo and add documents in the collection using Mongo shell.
- Also, create a new database 'librarydb' to connect to in MySQL.
- Then, run
```
python mongotosql.py
```
- Keep this program running. Now, you can test by opening the Mongo shell and adding documents.


## Wrapper script

A script that performs simple checks for referential integrity in CassendraDB.

- Setup Cassandra and run the server.
- Now, run
```
python prepareCassandra.py
```
- This will prepare the tables with some data.
- Now, run
```
python refint.py
```
- While it is running, to remove an entry from Books table, run
```
python removeCass.py
```
- This script enforces referential integrity.


## API

A simple API program using flask and OpenCV which takes an image from client and detects faces.

- Run
```
python server.py
```
- Now, you can open the url given in 'client.py' in a browser window. Here, upload the images to see the result.

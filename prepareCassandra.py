from cassandra.cluster import Cluster


cluster = Cluster(['127.0.0.1'], port=9042)
cqlcursor = cluster.connect()
# cqlcursor.execute(
#     "CREATE KEYSPACE library WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1}")
cqlcursor.execute('USE library')

cqlcursor.execute("DROP TABLE Books")
cqlcursor.execute("DROP TABLE Readers")

cqlcursor.execute(
    "CREATE TABLE Books(isbn text, accession_no text PRIMARY KEY, title text, author text, publisher text)")

cqlcursor.execute(
    "CREATE TABLE Readers(reader_id text PRIMARY KEY, accession_no text, issue_date text, return_date text)")

print(cluster.metadata.keyspaces['library'].tables)


book_list = [{"ISBN": "9780132350884", "Accession_No": "010820090011", "Title": "Clean Code: A Handbook of Agile Software Craftsmanship", "Author": "Robert C. Martin", "Publisher": "Prentice Hall, 2009"},
             {"ISBN": "9780134757704", "Accession_No": "201120180005", "Title": "Refactoring: Improving the Design of Existing Code",
                 "Author": "Martin Fowler", "Publisher": "Addison-Wesley Professional, 2018"},
             {"ISBN": "9780201544336", "Accession_No": "010219990014",
              "Title": "The C Book, Featuring the ANSI C Standard", "Author": "Michael Francis Banahan", "Publisher": "Addison-Wesley Publishing Company"},
             {"ISBN": "9781530051120", "Accession_No": "090420160022", "Title": "Python for Everybody: Exploring Data Using Python 3",
                 "Author": "Charles R. Severance", "Publisher": "Charles Severance"},
             {"ISBN": "9781449355692", "Accession_No": "120620130016", "Title": "Learning Python: Powerful Object-Oriented Programming", "Author": "Mark Lutz", "Publisher": "O'Reilly Media"}]

reader_list = [{"reader_id": "12349870", "Accession_No": "010820090011", "Issue_date": "01/07/2021", "Return_date": "01/09/2021"},
               {"reader_id": "67345635", "Accession_No": "201120180005",
                   "Issue_date": "24/09/2021", "Return_date": "01/12/2021"},
               {"reader_id": "56924356", "Accession_No": "010219990014",
                   "Issue_date": "01/05/2021", "Return_date": "01/07/2021"},
               {"reader_id": "56723456", "Accession_No": "090420160022",
                   "Issue_date": "13/07/2021", "Return_date": "11/10/2021"},
               {"reader_id": "23645677", "Accession_No": "120620130016", "Issue_date": "13/04/2021", "Return_date": "23/06/2021"}]

for book in book_list:
    cqltable = "INSERT INTO Books(isbn, accession_no, title, author, publisher) VALUES (%s, %s, %s, %s, %s)"
    cqlvalues = (book["ISBN"], book["Accession_No"],
                 book["Title"], book["Author"], book["Publisher"])
    cqlcursor.execute(cqltable, cqlvalues)

for reader in reader_list:
    cqltable = "INSERT INTO Readers(reader_id, accession_no, issue_date, return_date) VALUES (%s, %s, %s, %s)"
    cqlvalues = (reader["reader_id"], reader["Accession_No"],
                 reader["Issue_date"], reader["Return_date"])
    cqlcursor.execute(cqltable, cqlvalues)


rows = cqlcursor.execute("SELECT * FROM Books")
for x in rows:
    print(x)

rows = cqlcursor.execute("SELECT * FROM Readers")
for x in rows:
    print(x)

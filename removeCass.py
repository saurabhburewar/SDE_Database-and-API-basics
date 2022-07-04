from cassandra.cluster import Cluster


cluster = Cluster(['127.0.0.1'], port=9042)
cqlcursor = cluster.connect()

cqlcursor.execute('USE library')

key = "120620130016"
key1 = "'{}'".format(key)

cqlcursor.execute(
    "DELETE FROM Books WHERE accession_no = %s", (key1,))

rows = cqlcursor.execute("SELECT * FROM Books")
for x in rows:
    print(x)

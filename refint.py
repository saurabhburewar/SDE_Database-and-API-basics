from cassandra.cluster import Cluster
import time


cluster = Cluster(['127.0.0.1'], port=9042)
cqlcursor = cluster.connect()
# cqlcursor.execute(
#     "CREATE KEYSPACE library WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1}")
cqlcursor.execute('USE library')

keys = []
rows = cqlcursor.execute("SELECT * FROM Books")
countobj = cqlcursor.execute("SELECT COUNT(*) FROM Books")
for x in countobj:
    count = x[0]

print("Initial count - ", count)

for x in rows:
    keys.append(x[0])

try:
    while 1:
        cobj = cqlcursor.execute("SELECT COUNT(*) FROM Books")
        for x in cobj:
            c = x[0]
        print("Count now - ", c)

        if c < count:
            new_keys = []
            new_rows = cqlcursor.execute("SELECT * FROM Books")
            for x in new_rows:
                new_keys.append(x[0])

            keydiff = [item for item in keys if item not in new_keys]
            for key in keydiff:
                key1 = "'{}'".format(key)
                cqlcursor.execute(
                    "DELETE FROM Readers WHERE accession_no = %s", (key1,))

            count = c
            keys = new_keys

        time.sleep(5)

except KeyboardInterrupt:
    exit(0)


print(cluster.metadata.keyspaces['library'].tables)

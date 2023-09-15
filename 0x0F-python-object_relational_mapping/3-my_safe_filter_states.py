#!/usr/bin/python3
import MySQLdb
import sys

argv = sys.argv

try:
    db_con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
except Exception:
    print("can't connect to database")
    sys.exit(0)
states = db_con.cursor()
query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
states.execute(query, (argv[4],))
rows = states.fetchall()
for row in rows:
    print(row)
states.close()
db_con.close()

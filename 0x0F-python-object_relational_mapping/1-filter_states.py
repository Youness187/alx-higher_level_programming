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
states.execute("SELECT id, name FROM states ORDER BY id")
rows = states.fetchall()
for row in rows:
    if "N" == row[1][0]:
        print(row)
states.close()
db_con.close()

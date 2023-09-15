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
query = "SELECT c.name FROM cities AS c JOIN states AS s\
         ON c.state_id=s.id WHERE s.name LIKE %s ORDER BY c.state_id"
states.execute(query, (argv[4],))
rows = states.fetchall()
for row in rows:
    print(row[0], end=("\n" if row == rows[-1] else ", "))
states.close()
db_con.close()

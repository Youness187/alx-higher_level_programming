#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
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
        sys.exit(0)
    states = db_con.cursor()
    states.execute("SELECT * FROM states ORDER BY id")
    rows = states.fetchall()
    for row in rows:
        print(row)
    states.close()
    db_con.close()

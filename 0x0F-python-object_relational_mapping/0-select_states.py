#!/usr/bin/python3
import MySQLdb
from sys import argv


def get_all_state():
    """lists all states from the database"""
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
        return 0
    states = db_con.cursor()
    states.execute("SELECT * FROM states ORDER BY id")
    rows = states.fetchall()
    for row in rows:
        print(row)
    states.close()
    db_con.close()


get_all_state()

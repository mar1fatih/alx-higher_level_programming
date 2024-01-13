#!/usr/bin/python3
""" lists all states with a name starting with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3], port='3306')
    cur = db.cursor()
    cur.execute("SELECT * 
    FROM states 
    WHERE UPPER(SUBSTRING(state_name FROM 1 FOR 1)) = 'N';")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

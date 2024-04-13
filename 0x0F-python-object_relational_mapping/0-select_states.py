#!/usr/bin/python3
"""script that lists all states from the database `hbtn_0e_0_usa`"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    dn_conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    commands = dn_conn.cursor()
    commands.execute("SELECT * FROM states ORDER BY id ASC")
    usa = commands.fetchall()
    for state in usa:
        print(state)
    commands.close()
    dn_conn.close()

#!/usr/bin/python3

import MySQLdb
import sys

args = sys.argv
database_connection = MySQLdb.connect(host='localhost', port=3306, user= args[1], passwd=args[2], db=args[3])
cur = database_connection.cursor()
cur.execute("SELECT C.name FROM cities C JOIN states S ON C.state_id = S.id WHERE S.name = (%s) ORDER BY C.id", (args[4],))
for name in cur.fetchall() :
    print(name)
cur.close()
database_connection.close()

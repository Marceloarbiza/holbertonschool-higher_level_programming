#!/usr/bin/python3

import MySQLdb
import sys

args = sys.argv
myConection = MySQLdb.connect(host='localhost', port=3306, user= args[1], passwd=args[2], db=args[3])
cur = myConection.cursor()
cur.execute( "SELECT * FROM states ORDER BY states.id" )
for row in cur.fetchall() :
    print(row)
cur.close()
myConection.close()

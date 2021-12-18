#!/usr/bin/python3
""" Write a script that takes in an argument and displays """


if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    database_connection = MySQLdb.connect(host='localhost', port=3306,
                                               user=args[1], passwd=args[2],
                                               db=args[3])
    cur = database_connection.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY '{}'\
                ORDER BY states.id".format(args[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    database_connection.close()

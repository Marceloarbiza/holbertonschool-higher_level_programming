#!/usr/bin/python3
""" Write a script that takes in the name of a state """


if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    database_connection = MySQLdb.connect(host='localhost', port=3306,
                                               user=args[1], passwd=args[2],
                                               db=args[3])
    cur = database_connection.cursor()
    cur.execute("SELECT C.name FROM cities C JOIN states S ON C.state_id\
                = S.id WHERE S.name = (%s) ORDER BY C.id", (args[4],))
    rows = cur.fetchall()
    i = len(rows)
    for j in range(i - 1):
        print(f"{rows[j][0]}, ", end="")
    if (i != 0):
        print(f"{rows[j + 1][0]}")
    else:
        print()
    cur.close()
    database_connection.close()

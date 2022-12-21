import MySQLdb
con=MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="oPOx028ar",
    db="app")

cur=con.cursor()

cur.execute("""
            DELETE FROM user
            """)


con.commit()

con.close()

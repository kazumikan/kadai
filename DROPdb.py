import MySQLdb
con=MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="oPOx028ar",
    db="app")

cur=con.cursor()

cur.execute("""
            DROP TABLE schedule
            """)


con.commit()

con.close()

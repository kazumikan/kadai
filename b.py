from flask import Flask, render_template, request
import MySQLdb
import html
con=MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="oPOx028ar",
    db="app")

app = Flask(__name__)

@app.route("/")
def test_page():
    return """here is test_page<br>
                <a href=\"home\">start_test</a>"""

@app.route("/home")
def home_page():
    return """this is home<br>
                <a href=\"add\">add_test_in_usertable</a><br>
                <a href=\"delete_test\">delete_test_in_usertable</a><br>
                <a href=\"close_connect\">end_test</a>"""

@app.route("/add")
def add():
    return render_template("add_test.html",title="add_test")

@app.route("/add_test")
def add_test():
    username = request.args.get("username")
    post = request.args.get("post")
    password = request.args.get("password")
    cur=con.cursor()
    sql=("""INSERT INTO user
                (name, post, password)
                VALUES (%s, %s, %s )
                """)
    data=[(username,post,password)]
    cur.executemany(sql,data)
    con.commit()
    return """complete delete test<br>please check MySQL<br>
                <a href=\"home\">home</a>"""

@app.route("/delete_test")
def delete_test():
    cur=con.cursor()
    cur.execute("""DELETE FROM user""")
    con.commit()
    return """complete delete test<br>please check MySQL<br>
                <a href=\"home\">home</a>"""

@app.route("/close_connect")
def close_connect():
    con.close()
    return """test end<br>please close page"""

if __name__ == "__main__":
    app.run(debug=True)
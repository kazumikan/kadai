from flask import Flask, render_template, request, session, redirect, jsonify
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from datetime import timedelta
import secrets
import MySQLdb
import html
import dicttoxml

app = Flask(__name__)
app.secret_key=secrets.token_urlsafe(16)
app.permanent_session_lifetime=timedelta(minutes=60)

def connect():
    con=MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="oPOx028ar",
        db="app",
        use_unicode=True,
        charset="utf8")
    return con

@app.after_request
def apply_caching(response):
        response.headers["X-Frame-Options"]="SAMEORIGIN"
        return response

@app.route("/")
def test_page():
    return redirect("test_home")

@app.route("/test_home")
def home_page():
    return """予定管理アプリ<br>
                <a href=\"make\">アカウント作成</a><br>
                <a href=\"login\">ログイン</a><br>"""

@app.route("/make", methods = ["GET", "POST"])
def make():
    if request.method == "GET":
        return render_template("make.html")
    elif request.method == "POST":
        name = request.form["name"]
        post = request.form["post"]
        email = request.form["email"]
        password = request.form["password"]
        hashpass = gph(password)
        con=connect()
        cur=con.cursor()
        cur.execute("""
                    SELECT * FROM user WHERE email=%(email)s
                    """,{"email":email})
        data=[]
        for row in cur:
            data.append(row)
        if len(data)!=0:
            return render_template("make.html", msg = "既に存在するメールアドレスです")
        cur.execute("""INSERT INTO user
                    (name, post, email, password)
                    VALUES (%(name)s, %(post)s, %(email)s, %(password)s)
                    """,{"name":name, "post":post, "email":email, "password":hashpass})
        con.commit()
        con.close()
        return """アカウント作成完了<br>
                    <a href=\"test_home\">home</a>"""

@app.route("/login")
def add():
    return render_template("login_test.html",title="login_test")

@app.route("/login_test", methods = ["GET", "POST"])
def login_test():
    if request.method == "GET":
        session.clear()
        return render_template("login_test.html", title="login_test", retern_hoeme="<a href=\"test_home\">home</a>")
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        con=connect()
        cur=con.cursor()
        cur.execute("""SELECT password,name,email,userid from user
                        WHERE email=%(email)s""",{"email":email})
        con.close()
        data=[]
        for row in cur:
            data.append([row[0],row[1],row[2],row[3]])
        if len(data)==0:
            return render_template("login_test.html",msg="メールアドレスが違います", retern_home="<a href=\"test_home\">home</a>")
        if cph(data[0][0],password):
            session["name"]=data[0][1]
            session["email"]=data[0][2]
            session["userid"]=data[0][3]
            return redirect("home")
        else:
            return render_template("login_test.html",msg="パスワードが違います", retern_home="<a href=\"test_home\">home</a>")

@app.route("/home")
def home():
    if "name" in session:
        return render_template("success.html",name=html.escape(session["name"]),email=html.escape(session["email"]) ,url="<a href=\"add_schedule\">スケジュール追加</a><br>", url2="<a href=\"check_schedule\">スケジュール確認</a><br>", url3="<a href=\"test_get_api\">API取得</a><br>")
    else: return redirect("login_test")

@app.route("/add_schedule", methods = ["GET", "POST"])
def add_schedule():
    if request.method == "GET" and "name" in session:
        return render_template("add_schedule.html")
    elif request.method == "POST":
        title = request.form["title"]
        startday = request.form["startday"]
        starttime = request.form["starttime"]
        endtime = request.form["endtime"]
        memo = request.form["memo"]
        userid=html.escape(str(session["userid"]))
        con=connect()
        cur=con.cursor()
        cur.execute("""INSERT INTO schedule
                    (title, memo,userid,startday,starttime,endtime)
                    VALUES (%(title)s, %(memo)s, %(userid)s, %(startday)s, %(starttime)s, %(endtime)s)
                    """,{"title":title, "memo":memo, "userid":userid, "startday":startday, "starttime":starttime, "endtime":endtime})
        con.commit()
        con.close()
        return """スケジュール追加完了<br>
                    <a href=\"home\">home</a>"""

@app.route("/check_schedule")
def check_schedule():
    if "name" in session:
        uid=html.escape(str(session["userid"]))
        userid=int(uid)
        con=connect()
        cur=con.cursor()
        cur.execute("""SELECT title,startday from schedule WHERE userid=%(userid)s order by startday asc
                    """,{"userid":userid})
        data=[]
        titledata=[]
        sqldata=[]
        eventdata=[]
        day=list()
        for row in cur:
            day=html.escape(str(row[1])).split('-')
            data.append(day[2])
            eventdata.append(html.escape(row[0]))
        i=0
        for time in range(31):
            time=time+1
            if format(time,"0=2")==data[i]:
                titledata.append(eventdata[i])
                i=i+1
            elif format(time,"0=2")!=data[i]:
                titledata.append(" ")
            time=time-1

        day1=str(titledata[0])
        day2=str(titledata[1])
        day3=str(titledata[2])
        day4=str(titledata[3])
        day5=str(titledata[4])
        day6=str(titledata[5])
        day7=str(titledata[6])
        day8=str(titledata[7])
        day9=str(titledata[8])
        day10=str(titledata[9])
        day11=str(titledata[10])
        day12=str(titledata[11])
        day13=str(titledata[12])
        day14=str(titledata[13])
        day15=str(titledata[14])
        day16=str(titledata[15])
        day17=str(titledata[16])
        day18=str(titledata[17])
        day19=str(titledata[18])
        day20=str(titledata[19])
        day21=str(titledata[20])
        day22=str(titledata[21])
        day23=str(titledata[22])
        day24=str(titledata[23])
        day25=str(titledata[24])
        day26=str(titledata[25])
        day27=str(titledata[26])
        day28=str(titledata[27])
        day29=str(titledata[28])
        day30=str(titledata[29])
        day31=str(titledata[30])
    return render_template("check_schedule.html",day1=day1,day2=day2,day3=day3,day4=day4,day5=day5,day6=day6,day7=day7,day8=day8,day9=day9,day10=day10,day11=day11,day12=day12,day13=day13,day14=day14,day15=day15,day16=day16,day17=day17,day18=day18,day19=day19,day20=day20,day21=day21,day22=day22,day23=day23,day24=day24,day25=day25,day26=day26,day27=day27,day28=day28,day29=day29,day30=day30,day31=day31)

@app.route("/test_get_api")
def test_get_api():
    return render_template("search.html")

@app.route("/result")
def result():
    if "name" in session:
        form=request.args.get("format")
        month=request.args.get("month")
        userid=html.escape(str(session["userid"]))
        con=connect()
        cur=con.cursor()
        cur.execute("""SELECT title,startday,scheduleid from schedule where userid=%(userid)s AND startday like %(month)s
                    """,{"userid":userid,"month":"%"+month+"%"})

    res = "<title>検索結果</title>"
    for row in cur:
        res = res + "<table border=\"1\">\n"
        res = res + "\t<tr><td><a href=\"api?id=" + html.escape(str(row[2])) + "&"
        res = res + "format=" + html.escape(form) + "\">" + html.escape(str(row[0])) +"</a></td></tr>\n"
        res = res + "\t<tr><td><pre>" + html.escape(str(row[1])) + "</pre></td></tr>"
        res = res + "</table>"
    con.close()
    return render_template("result.html",res=res)

@app.route("/api")
def api():
    num = request.args.get("id")
    form = request.args.get("format")
    con = connect()
    cur=con.cursor()
    cur.execute("""
                SELECT memo,startday,starttime,endtime FROM schedule where scheduleid=%(id)s""",{"id":num})
    cur2=con.cursor()
    cur2.execute("""SELECT title from schedule where scheduleid=%(id)s""",{"id":num})
    res={}
    for row2 in cur2:
        res["title"]=html.escape(str(row2[0]))
    tmpa=[]
    for row in cur:
        tmpd={}
        tmpd["memo"]=html.escape(str(row[0]))
        tmpd["startday"]=html.escape(str(row[1]))
        tmpd["starttime"]=html.escape(str(row[2]))
        tmpd["endrime"]=html.escape(str(row[3]))
        tmpa.append(tmpd)
    res["content"]=tmpa
    if form == "XML":
        xml=dicttoxml.dicttoxml(res)
        resp=app.make_response(xml)
        resp.mimetype="text/xml"
        return resp
    else:
        return jsonify(res) 

if __name__ == "__main__":
    app.run(host="0.0.0.0")
from flask import Flask,render_template,request
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from wtforms import StringField,SubmitField
from wtforms import RadioField
from wtforms.validators import Required
from wtforms.validators import Optional
import pymysql


choices = [
      ('Man','Man'),
      ('Woman','Woman'),
]
class NameForm(Form):
    uid = StringField('uid',validators=[Required()])
    name = StringField('name',validators=[Optional()])
    school = StringField('school',validators=[Optional()]) 
    major = StringField('major',validators=[Optional()])
    sex = RadioField('sex',validators=[Required()],choices=choices)
    registdate = StringField('registdate',validators=[Optional()])
    lastdate = StringField('lastdate',validators=[Optional()])
    submit = SubmitField('submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sean Cheung'
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    name = ''
    uid = ''
    school = ''
    major = ''
    sex = ''
    registdate = ''
    lastdate = ''
    nameForm = NameForm()

    if nameForm.validate_on_submit():
        name = nameForm.name.data
        uid = nameForm.uid.data
        school = nameForm.school.data
        major = nameForm.major.data
        sex = nameForm.sex.data
        registdate = nameForm.registdate.data
        lastdate = nameForm.lastdate.data
        if(name == None): 
            name=''
        if(uid == None):
            uid= ''
        if(school == None):
            school = ''
        if(major == None):
            major = ''
        if(sex == None):
            sex = ''
        if(registdate == None):
            registdate = ''
        if(lastdate == None):
            lastdate = ''
        mstr="insert into member (uid,name,school,major,sex,registdate,lastdate) values('"+uid+"','"+name+"','"+school+"','"+major+"','"+sex+"','"+registdate+"','"+lastdate+"')"
        try:
            conn = pymysql.connect(host='localhost',user='root',password='1',db='test',charset='utf8')
            cur=conn.cursor()
            cur.execute(mstr)
            conn.commit()
            cur.close()
            conn.close()
        except Exception:print("except")
    return render_template('index.html',form=nameForm)


@app.route('/show',methods=['GET','POST'])
def show():
    try:
        conn=pymysql.connect(host='localhost',user='root',password='1',db='test',charset='utf8')
        cur=conn.cursor()
        cur.execute('select * from member')
        data=cur.fetchall()
        response = "<html>\n"
        response += "<title>Data in the db</title>\n"
        response += "<body>\n"
        response += "<a href='./'>add member</a>"
        response += "<table>\n"
        for i in range(len(data)):
            response += "<tr>\n"
            for j in range(len(data[0])):
                response += "<td>"+data[i][j]+"</td>\n"
            response += "<td><a href='./edit?uid="+data[i][0]+"'>  edit</a></td>\n"
            response += "</tr><br>\n"
        response += "</table>\n"
        response += "</html>"
        cur.close()
        conn.close()
    except Exception:print("except")
    return response

@app.route('/edit',methods=['GET','POST'])
def edit():
    getuid=request.args.get('uid',)
    response=""
    uid=''
    name=''
    school=''
    major=''
    sex=''
    registdate=''
    lastate=''
    data = None
    try:
        conn = pymysql.connect(host='localhost',user='root',password='1',db='test',charset='utf8')
        cur=conn.cursor()
        cur.execute("select * from member where uid='"+getuid+"'")
        data=cur.fetchone()
        cur.close()
        conn.close()
    except Exception:print("except")
    
    uid=data[0]
    name=data[1]
    school=data[2]
    major=data[3]
    sex=data[4]
    registdate=data[5]
    lastdate=data[6]
    nameForm = NameForm(uid=uid,name=name,school=school,major=major,sex=sex,registdate=registdate,lastdate=lastdate)
    if nameForm.validate_on_submit():
        name = nameForm.name.data
        uid = nameForm.uid.data
        school = nameForm.school.data
        major = nameForm.major.data
        sex = nameForm.sex.data
        registdate = nameForm.registdate.data
        lastdate = nameForm.lastdate.data
        try:
            conn = pymysql.connect(host='localhost',user='root',password='1',db='test',charset='utf8')
            cur=conn.cursor()
            msql="update member set name='"+name+"',school='"+school+"',major='"+major+"',sex='"+sex+"',registdate='"+registdate+"',lastdate='"+lastdate+"' where uid='"+uid+"'"
            cur.execute(msql)
            conn.commit()
            cur.close()
            conn.close()
        except Exception:print("except")
    return render_template('index.html',form=nameForm)
    

if __name__=='__main__':
    app.run(debug=True)



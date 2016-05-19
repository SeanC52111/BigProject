from flask import Flask,render_template
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from wtforms import StringField,SubmitField
from wtforms.validators import Required
import pymysql

class NameForm(Form):
    uid = StringField('uid',validators=[Required()])
    name = StringField('name',validators=[Required()])
    school = StringField('school',validators=[Required()]) 
    major = StringField('major',validators=[Required()])
    sex = StringField('sex',validators=[Required()])
    registdate = StringField('registdate',validators=[Required()])
    lastdate = StringField('lastdate',validators=[Required()])
    submit = SubmitField('submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sean Cheung'
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    uid = None
    school = None
    major = None
    sex = None
    registdate = None
    lastdate = None
    nameForm = NameForm()

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
            cur.execute("insert into member (uid,name,school,major,sex,registdate,lastdate) values('"+uid+"','"+name+"','"+school+"','"+major+"','"+sex+"','"+registdate+"','"+lastdate+"')")
            conn.commit()
            cur.close()
            conn.close()
        except Exception:print("except")
    return render_template('index.html',form=nameForm,name=name)



if __name__=='__main__':
    app.run(debug=True)



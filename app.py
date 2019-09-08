from datetime import timedelta

from flask import render_template
from flask import Flask
from flask import request
import pymysql
import traceback


db=pymysql.connect("localhost","root","hy19980318","web")

app = Flask(__name__)
if __name__=='__main__':
    app.run(debug=False)
app.send_file_max_age_default = timedelta(seconds=1)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signin')
def signin_op():
    cursor=db.cursor()
    sql="select * from manager where manager_ID="+request.args.get('user')+" and manager_psd="+request.args.get('password')+" "
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        print(len(results))
        if len(results)==1:
            return render_template('index.html')
        else:
            return 'sign falied'
        db.commit()

    except:
        traceback.print_exc()
        db.rollback()

@app.route('/mainframe_f')
def mainframe_op():
    return render_template('index.html')


@app.route('/oldtable_f')
def oldtable_show_op():
    cursor=db.cursor()
    sql="select * from older"
    cursor.execute(sql)
    show=cursor.fetchall()
    print(show)

    return render_template('old_table.html',s=show)

@app.route('/deleteold_f')
def deleteoldid():
    cursor=db.cursor()
    sql="delete from older where old_ID="+request.args.get('old_delete_id')+" "
    cursor.execute(sql)
    db.commit()
    return render_template('index.html')

@app.route('/alterold_f')
def alterold():
    cursor=db.cursor()
    sql="update older set old_name="+request.args.get('old_change_name')+",old_sex="+request.args.get('old_change_sex')+",old_age="+request.args.get('old_change_age')+",old_address="+request.args.get('old_change_add')+",old_phone="+request.args.get('old_change_phone')+" where old_ID="+request.args.get('old_change_id')+" "
    cursor.execute(sql)
    db.commit()
    return render_template('index.html')

@app.route('/login_f')
def login_op():
    return render_template('login.html')

@app.route('/basicinf_f')
def basicinf_op():
    return render_template('basic_inf.html')





@app.route('/worker_f')
def worker_op():
    cursor = db.cursor()
    sql = "select * from worker"
    cursor.execute(sql)
    wokerinf = cursor.fetchall()
    return render_template('worker_table.html',workerinf=wokerinf)

@app.route('/changeworker_f')
def changeworker_op():
    cursor=db.cursor()
    sql = "update worker set worker_name=" + request.args.get('worker_change_name') + ",worker_sex=" + request.args.get(
        'worker_change_sex') + ",worker_age=" + request.args.get('worker_change_age') + ",worker_address=" + request.args.get(
        'worker_change_add') + ",worker_phone=" + request.args.get('worker_change_phone') + " where worker_ID=" + request.args.get(
        'worker_change_id') + " "
    cursor.execute(sql)
    db.commit()
    return render_template('index.html')

@app.route('/deleteworker_f')
def deleworker_f():
    cursor=db.cursor()
    sql="delete from worker where worker_ID="+request.args.get('worker_delete_id')+" "
    cursor.execute(sql)
    db.commit()
    return render_template('index.html')

@app.route('/volunteer_f')
def volunteer_op():
    cursor = db.cursor()
    sql = "select * from volunteer"
    cursor.execute(sql)
    volunteerinf = cursor.fetchall()
    return render_template('volunteer_table.html',volunteerinf=volunteerinf)

@app.route('/changevoluinf')
def changevolunteer_op():
    cursor = db.cursor()
    sql = "update volunteer set volunteer_name=" + request.args.get('volunteer_change_name') + ",volunteer_sex=" + request.args.get(
        'volunteer_change_sex') + ",volunteer_age=" + request.args.get(
        'volunteer_change_age') + ",volunteer_phone=" + request.args.get(
        'volunteer_change_phone') + " where volunteer_ID=" + request.args.get(
        'volunteer_change_id') + " "
    cursor.execute(sql)
    db.commit()
    return render_template('index.html')

@app.route('/deletevolunteer_f')
def deletevolunteer_op():
    cursor=db.cursor()
    sql="delete from volunteer where volunteer_ID="+request.args.get('volu_delete_id')+" "
    cursor.execute(sql)
    db.commit()
    return render_template('index.html')
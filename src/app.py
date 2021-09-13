from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from appConfig import Config

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = Config[0]["Host"]
app.config['MYSQL_USER'] = Config[0]["User"]
app.config['MYSQL_PASSWORD'] = Config[0]["Password"]
app.config['MYSQL_DB'] = Config[0]["DB"]
mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios;')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html')
@app.route('/ih')
def HI():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios;')
    data = cur.fetchall()
    cur.close()
    return render_template('hi.html')

if __name__ == "__main__":
    app.run(port=5000,debug=True)
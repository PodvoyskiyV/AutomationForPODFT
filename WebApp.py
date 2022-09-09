import datetime
import mysql.connector
from Python import variables as var
from flask import Flask, render_template, redirect, url_for  # pip install flask

app = Flask(__name__)


def db_connection_func():
    start_db_connection_func = datetime.datetime.now()

    my_db = mysql.connector.connect(
        host="localhost",
        user=f"{var.username_db}",
        password=f"{var.password_db}",
        database="PodFT"
    )

    my_cursor = my_db.cursor()

    end_db_connection_func = datetime.datetime.now()
    print(f'db_connection_func ended in {end_db_connection_func - start_db_connection_func}')

    return my_cursor, my_db


def mrott(my_db, my_cursor):
    mrot_data_for_front = []
    my_cursor.execute("SELECT * FROM mrot")
    data = my_cursor.fetchall()
    for row in data:
        mrot_data_for_front.append({
            'card': row[0],
            'count': row[1],
            'ammount': row[2],
            'block': row[3],
            'abs': row[4]})
    print(mrot_data_for_front[0])


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/mrot")
def mrot():
    return render_template("mrot.html")


@app.route("/octo")
def octo():
    return render_template("octo.html")


@app.route("/p2p")
def p2p():
    return render_template("p2p.html")


cursor, db = db_connection_func()
mrott(db, cursor)
app.run(host="0.0.0.0", port=80)
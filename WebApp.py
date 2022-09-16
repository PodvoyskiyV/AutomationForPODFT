import datetime
import json
import mysql.connector
from Python import variables as var
from flask import Flask, render_template, redirect, url_for, request  # pip install flask

app = Flask(__name__)
start_date = end_date = var.today
flag = ''


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


def mrot_data(my_cursor):
    mrot_month = []
    my_cursor.execute("SELECT * FROM mrot LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        mrot_month.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2],
            'block': row[3],
            'abs': row[4]})

    mrot_dynamics = []
    my_cursor.execute("SELECT * FROM mrot LIMIT 10")
    data = my_cursor.fetchall()
    for row in data:
        mrot_dynamics.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2],
            'block': row[3],
            'abs': row[4]})

    return mrot_month, mrot_dynamics


def octo_data(my_cursor, start, end):
    octo_sender_week = []
    my_cursor.execute("SELECT * FROM card_sender_octo_week")
    data = my_cursor.fetchall()
    for row in data:
        octo_sender_week.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_sender_month = []
    my_cursor.execute("SELECT * FROM card_sender_octo_month")
    data = my_cursor.fetchall()
    for row in data:
        octo_sender_month.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_sender_search = []
    my_cursor.execute("SELECT masked_card_number, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT masked_card_number, created_date, amount FROM Initial_Data_OCTO "
                      f"WHERE created_date BETWEEN '{start}' AND '{end}') "
                      "X GROUP BY masked_card_number ORDER BY count DESC, amount DESC;")
    data = my_cursor.fetchall()
    for row in data:
        octo_sender_search.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_receiver_week = []
    my_cursor.execute("SELECT * FROM number_receiver_octo_week")
    data = my_cursor.fetchall()
    for row in data:
        octo_receiver_week.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_receiver_month = []
    my_cursor.execute("SELECT * FROM number_receiver_octo_month")
    data = my_cursor.fetchall()
    for row in data:
        octo_receiver_month.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_receiver_search = []
    my_cursor.execute("SELECT dest_tool_id, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT dest_tool_id, created_date, amount FROM Initial_Data_OCTO "
                      f"WHERE created_date BETWEEN '{start}' AND '{end}') "
                      "X GROUP BY dest_tool_id ORDER BY amount DESC, count DESC;")
    data = my_cursor.fetchall()
    for row in data:
        octo_receiver_search.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2]})

    return octo_sender_week, octo_sender_month, octo_sender_search, octo_receiver_week, octo_receiver_month, \
           octo_receiver_search


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/mrot")
def mrot():
    month, dynamics = mrot_data(cursor)
    return render_template("mrot.html", month=json.dumps(month), dynamics=json.dumps(dynamics))


@app.route("/dates")
def dates():
    global start_date, end_date, flag
    start_date = request.args["start_date"]
    end_date = request.args["end_date"]
    flag = request.args["flag"]
    print(flag, 'date')
    return "OK"


@app.route("/octo")
def octo():
    global flag
    sender_week, sender_month, sender_search, receiver_week, receiver_month, receiver_search = octo_data(cursor, start_date, end_date)
    print(flag)

    if flag == 'sender':
        tab = 'sender'
    elif flag == 'receiver':
        tab = 'receiver'
    else:
        tab = ''
    flag = ''
    print(tab)
    print('height')

    return render_template("octo.html", sender_week=json.dumps(sender_week), sender_month=json.dumps(sender_month),
                           sender_search=json.dumps(sender_search), receiver_week=json.dumps(receiver_week),
                           receiver_month=json.dumps(receiver_month), receiver_search=json.dumps(receiver_search),
                           tab=json.dumps(tab))


@app.route("/p2p")
def p2p():
    try:
        start_date = request.args["start_date"]
        end_date = request.args["end_date"]
    except:
        start_date = end_date = var.today
    return render_template("p2p.html")


cursor, db = db_connection_func()
app.run(host="0.0.0.0", port=80)

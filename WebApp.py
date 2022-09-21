import datetime
import json
import mysql.connector
from Python import variables as var
from flask import Flask, render_template, redirect, url_for, request  # pip install flask

app = Flask(__name__)
start_date = end_date = var.today
flag_octo = ''
flag_p2p = ''


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
    my_cursor.execute("SELECT * FROM mrot_month LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        mrot_month.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2],
            'block': row[3],
            'abs': row[4]})

    mrot_week = []
    my_cursor.execute("SELECT * FROM mrot_week LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        mrot_week.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2],
            'abs': row[3]})

    mrot_day = []
    my_cursor.execute("SELECT * FROM mrot_day LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        mrot_day.append({
            'card': row[0],
            'count': row[1],
            'amount': row[2],
            'abs': row[3]})

    return mrot_month, mrot_week, mrot_day


def octo_data(my_cursor, start, end):
    octo_sender_week = []
    my_cursor.execute("SELECT * FROM card_sender_octo_week")
    data = my_cursor.fetchall()
    for row in data:
        octo_sender_week.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_sender_month = []
    my_cursor.execute("SELECT * FROM card_sender_octo_month")
    data = my_cursor.fetchall()
    for row in data:
        octo_sender_month.append({
            'id': row[0],
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
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_receiver_week = []
    my_cursor.execute("SELECT * FROM number_receiver_octo_week")
    data = my_cursor.fetchall()
    for row in data:
        octo_receiver_week.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_receiver_month = []
    my_cursor.execute("SELECT * FROM number_receiver_octo_month")
    data = my_cursor.fetchall()
    for row in data:
        octo_receiver_month.append({
            'id': row[0],
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
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    return octo_sender_week, octo_sender_month, octo_sender_search, octo_receiver_week, octo_receiver_month, \
           octo_receiver_search


def p2p_data(my_cursor, start, end):
    p2p_country_week = []
    my_cursor.execute("SELECT * FROM country_p2p_week")
    data = my_cursor.fetchall()
    for row in data:
        p2p_country_week.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    p2p_country_month = []
    my_cursor.execute("SELECT * FROM country_p2p_month")
    data = my_cursor.fetchall()
    for row in data:
        p2p_country_month.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    p2p_country_search = []
    my_cursor.execute("SELECT country, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT country, time_id, amount FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{end}') "
                      "X GROUP BY country ORDER BY count DESC, amount DESC;")
    data = my_cursor.fetchall()
    for row in data:
        p2p_country_search.append({
            'id': row[0],
            'count': row[1],
            'amount': round(float(row[2]), 2)})

    p2p_pinfl_week = []
    my_cursor.execute("SELECT * FROM pinfl_receiver_week")
    data = my_cursor.fetchall()
    for row in data:
        p2p_pinfl_week.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    p2p_pinfl_month = []
    my_cursor.execute("SELECT * FROM pinfl_receiver_month")
    data = my_cursor.fetchall()
    for row in data:
        p2p_pinfl_month.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    p2p_pinfl_search = []
    my_cursor.execute("SELECT pinfl, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT pinfl, time_id, amount FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{end}') "
                      "X GROUP BY pinfl ORDER BY count DESC, amount DESC;")
    data = my_cursor.fetchall()
    for row in data:
        p2p_pinfl_search.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    p2p_tt_week = []
    my_cursor.execute("SELECT * FROM trans_gran_to_tt_week")
    data = my_cursor.fetchall()
    for row in data:
        p2p_tt_week.append({
            'id': float(row[0]),
            'count': row[1]})

    p2p_tt_month = []
    my_cursor.execute("SELECT * FROM trans_gran_to_tt_month")
    data = my_cursor.fetchall()
    for row in data:
        p2p_tt_month.append({
            'id': float(row[0]),
            'count': row[1]})

    p2p_tt_search = []
    my_cursor.execute("SELECT pos_code, COUNT(*) count FROM "
                      "(SELECT DISTINCT pos_code, time_id FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{end}') "
                      "X GROUP BY pos_code ORDER BY count DESC;")
    data = my_cursor.fetchall()
    for row in data:
        p2p_tt_search.append({
            'id': float(row[0]),
            'count': row[1]})

    return p2p_country_week, p2p_country_month, p2p_country_search, p2p_pinfl_week, p2p_pinfl_month, p2p_pinfl_search, \
           p2p_tt_week, p2p_tt_month, p2p_tt_search


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/mrot")
def mrot():
    month, week, day = mrot_data(cursor)
    return render_template("mrot.html", month=json.dumps(month), week=json.dumps(week), day=json.dumps(day))


@app.route("/dates_octo")
def dates_octo():
    global start_date, end_date, flag_octo
    start_date = request.args["start_date"]
    end_date = request.args["end_date"]
    flag_octo = request.args["flag"]
    return "OK"


@app.route("/octo")
def octo():
    global flag_octo
    sender_week, sender_month, sender_search, receiver_week, receiver_month, receiver_search = octo_data(cursor,
                                                                                                         start_date,
                                                                                                         end_date)

    if flag_octo == 'sender':
        tab_octo = 'sender'
    elif flag_octo == 'receiver':
        tab_octo = 'receiver'
    else:
        tab_octo = ''
    flag_octo = ''

    return render_template("octo.html", sender_week=json.dumps(sender_week), sender_month=json.dumps(sender_month),
                           sender_search=json.dumps(sender_search), receiver_week=json.dumps(receiver_week),
                           receiver_month=json.dumps(receiver_month), receiver_search=json.dumps(receiver_search),
                           tab=json.dumps(tab_octo))


@app.route("/dates_p2p")
def dates_p2p():
    global start_date, end_date, flag_p2p
    start_date = request.args["start_date"]
    end_date = request.args["end_date"]
    flag_p2p = request.args["flag"]
    return "OK"


@app.route("/p2p")
def p2p():
    global flag_p2p
    country_week, country_month, country_search, pinfl_week, pinfl_month, pinfl_search, tt_week, tt_month, tt_search \
        = p2p_data(cursor, start_date, end_date)

    print(flag_p2p, country_search)

    if flag_p2p == 'country':
        tab_p2p = 'country'
    elif flag_p2p == 'pinfl':
        tab_p2p = 'pinfl'
    elif flag_p2p == 'tt':
        tab_p2p = 'tt'
    else:
        tab_p2p = ''
    flag_p2p = ''

    return render_template("p2p.html", country_week=json.dumps(country_week), country_month=json.dumps(country_month),
                           country_search=json.dumps(country_search), pinfl_week=json.dumps(pinfl_week),
                           pinfl_month=json.dumps(pinfl_month), pinfl_search=json.dumps(pinfl_search),
                           tt_week=json.dumps(tt_week), tt_month=json.dumps(tt_month),
                           tt_search=json.dumps(tt_search), tab=json.dumps(tab_p2p))


cursor, db = db_connection_func()
app.run(host="0.0.0.0", port=80)

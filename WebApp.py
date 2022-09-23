import json
import mysql.connector
from Python import variables as var
from flask import Flask, render_template, redirect, url_for, request  # pip install flask

app = Flask(__name__)
start_date = end_date = var.today
flag_octo = ''
flag_p2p = ''
flag_offshore = ''


def db_connection_func():

    my_db = mysql.connector.connect(
        host="localhost",
        user=f"{var.username_db}",
        password=f"{var.password_db}",
        database="PodFT"
    )

    my_cursor = my_db.cursor()

    return my_cursor, my_db


def mrot_data(my_cursor):
    mrot_month = []
    my_cursor.execute("SELECT * FROM mrot_month LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        mrot_month.append({
            'card': row[0],
            # 'number': row[1],
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
            # 'number': row[1],
            'count': row[1],
            'amount': row[2],
            'abs': row[3]})

    mrot_day = []
    my_cursor.execute("SELECT * FROM mrot_day LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        mrot_day.append({
            'card': row[0],
            # 'number': row[1],
            'count': row[1],
            'amount': row[2],
            'abs': row[3]})

    return mrot_month, mrot_week, mrot_day


def octo_data(my_cursor, start, end):
    octo_sender_week = []
    my_cursor.execute("SELECT * FROM card_sender_octo_week LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        octo_sender_week.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_sender_month = []
    my_cursor.execute("SELECT * FROM card_sender_octo_month LIMIT 100")
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
                      "X GROUP BY masked_card_number ORDER BY count DESC, amount DESC LIMIT 100;")
    data = my_cursor.fetchall()
    for row in data:
        octo_sender_search.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_receiver_week = []
    my_cursor.execute("SELECT * FROM number_receiver_octo_week LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        octo_receiver_week.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    octo_receiver_month = []
    my_cursor.execute("SELECT * FROM number_receiver_octo_month LIMIT 100")
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
                      "X GROUP BY dest_tool_id ORDER BY amount DESC, count DESC LIMIT 100;")
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
    my_cursor.execute("SELECT * FROM country_p2p_week LIMIT 100")
    data = my_cursor.fetchall()
    for i in range(len(data)):
        if data[i][0] == 'United Kingdom of Great Britain and Northern Ireland':
            data[i] = list(data[i])
            data[i][0] = 'United Kingdom'
            data[i] = tuple(data[i])
        p2p_country_week.append({
            'id': data[i][0],
            'count': data[i][1],
            'amount': data[i][2]})

    p2p_country_month = []
    my_cursor.execute("SELECT * FROM country_p2p_month LIMIT 100")
    data = my_cursor.fetchall()
    count = 0
    for i in range(len(data)):
        if data[i][0] == 'United Kingdom of Great Britain and Northern Ireland':
            data[i] = list(data[i])
            data[i][0] = 'United Kingdom'
            data[i] = tuple(data[i])
        p2p_country_month.append({
            'id': data[i][0],
            'count': data[i][1],
            'amount': data[i][2]})
        count += data[i][1]

    p2p_data_for_charts_month = {
        'labels': "Countries",
        'datasets': [{
            'label': [data[0][0]],
            'backgroundColor': "rgba(255,221,50,0.2)",
            'borderColor': "rgba(255,221,50,1)",
            'data': [{
                'x': data[0][2],
                'y': data[0][1],
                'r': round(5 + 20 / count * data[0][1], 2)
            }]
        }, {
            'label': [data[1][0]],
            'backgroundColor': "rgba(60,186,159,0.2)",
            'borderColor': "rgba(60,186,159,1)",
            'data': [{
                'x': data[1][2],
                'y': data[1][1],
                'r': round(5 + 20 / count * data[1][1], 2)
            }]
        }, {
            'label': [data[2][0]],
            'backgroundColor': "rgba(0,0,0,0.2)",
            'borderColor': "#000",
            'data': [{
                'x': data[2][2],
                'y': data[2][1],
                'r': round(5 + 20 / count * data[2][1], 2)
            }]
        }, {
            'label': [data[3][0]],
            'backgroundColor': "rgba(193,46,12,0.2)",
            'borderColor': "rgba(193,46,12,1)",
            'data': [{
                'x': data[3][2],
                'y': data[3][1],
                'r': round(5 + 20 / count * data[3][1], 2)
            }]
        }, {
            'label': [data[4][0]],
            'backgroundColor': "rgba(255,255,255,0.2)",
            'borderColor': "rgba(255,255,255,1)",
            'data': [{
                'x': data[4][2],
                'y': data[4][1],
                'r': round(5 + 20 / count * data[4][1], 2)
            }]
        }]
    }

    p2p_country_search = []
    my_cursor.execute("SELECT country, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT country, time_id, amount FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{end}') "
                      "X GROUP BY country ORDER BY count DESC, amount DESC LIMIT 100;")
    data = my_cursor.fetchall()
    for i in range(len(data)):
        if data[i][0] == 'United Kingdom of Great Britain and Northern Ireland':
            data[i] = list(data[i])
            data[i][0] = 'United Kingdom'
            data[i] = tuple(data[i])
        p2p_country_search.append({
            'id': data[i][0],
            'count': data[i][1],
            'amount': round(float(data[i][2]), 2)})

    p2p_pinfl_week = []
    my_cursor.execute("SELECT * FROM pinfl_receiver_week LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        p2p_pinfl_week.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    p2p_pinfl_month = []
    my_cursor.execute("SELECT * FROM pinfl_receiver_month LIMIT 100")
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
                      "X GROUP BY pinfl ORDER BY count DESC, amount DESC LIMIT 100;")
    data = my_cursor.fetchall()
    for row in data:
        p2p_pinfl_search.append({
            'id': row[0],
            'count': row[1],
            'amount': row[2]})

    p2p_tt_week = []
    my_cursor.execute("SELECT * FROM trans_gran_to_tt_week LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        p2p_tt_week.append({
            'id': float(row[0]),
            'count': row[1]})

    p2p_tt_month = []
    my_cursor.execute("SELECT * FROM trans_gran_to_tt_month LIMIT 100")
    data = my_cursor.fetchall()
    for row in data:
        p2p_tt_month.append({
            'id': float(row[0]),
            'count': row[1]})

    p2p_tt_search = []
    my_cursor.execute("SELECT pos_code, COUNT(*) count FROM "
                      "(SELECT DISTINCT pos_code, time_id FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{end}') "
                      "X GROUP BY pos_code ORDER BY count DESC LIMIT 100;")
    data = my_cursor.fetchall()
    for row in data:
        p2p_tt_search.append({
            'id': float(row[0]),
            'count': row[1]})

    return p2p_country_week, p2p_country_month, p2p_country_search, p2p_pinfl_week, p2p_pinfl_month, p2p_pinfl_search, \
           p2p_tt_week, p2p_tt_month, p2p_tt_search, p2p_data_for_charts_month


def offshore_data(my_cursor, start, end):
    offshore_cyprus_week = []
    my_cursor.execute("SELECT * FROM offshore_week;")
    data = my_cursor.fetchall()
    for row in data:
        offshore_cyprus_week.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[2],
            'operation_date': str(row[3]),
            'amount': row[4],
            'country': row[5]})

    offshore_cyprus_month = []
    my_cursor.execute("SELECT * FROM offshore_month;")
    data = my_cursor.fetchall()
    for row in data:
        offshore_cyprus_month.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[2],
            'operation_date': str(row[3]),
            'amount': row[4],
            'country': row[5]})

    offshore_cyprus_search = []
    my_cursor.execute("SELECT fio, birth_date, document_number, time_id, amount, country FROM  Initial_Data_P2P "
                      f"WHERE (time_id BETWEEN '{start}' AND '{end}') AND country='Cyprus' "
                      "AND NOT country='nan' ORDER BY time_id;")
    data = my_cursor.fetchall()
    for row in data:
        offshore_cyprus_search.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[2],
            'operation_date': str(row[3]),
            'amount': row[4],
            'country': row[5]})

    return offshore_cyprus_week, offshore_cyprus_month, offshore_cyprus_search


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route("/index")
def index():
    reconnect_to_db()
    return render_template("index.html")


@app.route("/mrot")
def mrot():
    reconnect_to_db()
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
    reconnect_to_db()
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
    reconnect_to_db()
    global flag_p2p
    country_week, country_month, country_search, pinfl_week, pinfl_month, pinfl_search, tt_week, tt_month, tt_search, \
    p2p_data_for_charts_month = p2p_data(cursor, start_date, end_date)

    if flag_p2p == 'country':
        tab_p2p = 'country'
    elif flag_p2p == 'pinfl':
        tab_p2p = 'pinfl'
    elif flag_p2p == 'tt':
        tab_p2p = 'tt'
    else:
        tab_p2p = ''
    flag_p2p = ''

    return render_template("p2p.html", p2p_data_for_charts_month=json.dumps(p2p_data_for_charts_month),
                           country_week=json.dumps(country_week), country_month=json.dumps(country_month),
                           country_search=json.dumps(country_search), pinfl_week=json.dumps(pinfl_week),
                           pinfl_month=json.dumps(pinfl_month), pinfl_search=json.dumps(pinfl_search),
                           tt_week=json.dumps(tt_week), tt_month=json.dumps(tt_month),
                           tt_search=json.dumps(tt_search), tab=json.dumps(tab_p2p))


@app.route("/dates_offshore")
def dates_offshore():
    global start_date, end_date, flag_offshore
    start_date = request.args["start_date"]
    end_date = request.args["end_date"]
    flag_offshore = request.args["flag"]
    return "OK"


@app.route("/offshore")
def offshore():
    reconnect_to_db()
    global flag_offshore
    cyprus_week, cyprus_month, cyprus_search = offshore_data(cursor, start_date, end_date)

    print(flag_offshore, cyprus_week)

    if flag_offshore == 'cyprus':
        tab_offshore = 'cyprus'
    else:
        tab_offshore = ''
    flag_offshore = ''

    return render_template("offshore.html", cyprus_week=json.dumps(cyprus_week), cyprus_month=json.dumps(cyprus_month),
                           cyprus_search=json.dumps(cyprus_search), tab=json.dumps(tab_offshore))


def reconnect_to_db():
    global cursor, db
    cursor, db = db_connection_func()


cursor, db = db_connection_func()
app.run(host="0.0.0.0", port=80)

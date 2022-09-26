import json
from Python import BackOfWebApp as Back
from flask import Flask, render_template, redirect, url_for, request, send_file  # pip install flask

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route("/index")
def index():
    Back.reconnect_to_db()
    return render_template("index.html")


@app.route("/mrot")
def mrot():
    Back.reconnect_to_db()
    month, week, day = Back.mrot_data(Back.cursor)
    return render_template("mrot.html", month=json.dumps(month), week=json.dumps(week), day=json.dumps(day))


@app.route("/dates_octo")
def dates_octo():
    Back.start_date = request.args["start_date"]
    Back.end_date = request.args["end_date"]
    Back.flag_octo = request.args["flag"]
    return "OK"


@app.route("/octo")
def octo():
    Back.reconnect_to_db()
    sender_week, sender_month, sender_search, receiver_week, receiver_month, receiver_search = \
        Back.octo_data(Back.cursor, Back.start_date, Back.end_date)

    if Back.flag_octo == 'sender':
        tab_octo = 'sender'
    elif Back.flag_octo == 'receiver':
        tab_octo = 'receiver'
    else:
        tab_octo = ''
    Back.flag_octo = ''

    return render_template("octo.html", sender_week=json.dumps(sender_week), sender_month=json.dumps(sender_month),
                           sender_search=json.dumps(sender_search), receiver_week=json.dumps(receiver_week),
                           receiver_month=json.dumps(receiver_month), receiver_search=json.dumps(receiver_search),
                           tab=json.dumps(tab_octo))


@app.route("/dates_p2p")
def dates_p2p():
    Back.start_date = request.args["start_date"]
    Back.end_date = request.args["end_date"]
    Back.flag_p2p = request.args["flag"]
    return "OK"


@app.route("/p2p")
def p2p():
    Back.reconnect_to_db()
    country_week, country_month, country_search, pinfl_week, pinfl_month, pinfl_search, tt_week, tt_month, tt_search, \
        p2p_data_for_charts_month = Back.p2p_data(Back.cursor, Back.start_date, Back.end_date)

    if Back.flag_p2p == 'country':
        tab_p2p = 'country'
    elif Back.flag_p2p == 'pinfl':
        tab_p2p = 'pinfl'
    elif Back.flag_p2p == 'tt':
        tab_p2p = 'tt'
    else:
        tab_p2p = ''
    Back.flag_p2p = ''

    return render_template("p2p.html", p2p_data_for_charts_month=json.dumps(p2p_data_for_charts_month),
                           country_week=json.dumps(country_week), country_month=json.dumps(country_month),
                           country_search=json.dumps(country_search), pinfl_week=json.dumps(pinfl_week),
                           pinfl_month=json.dumps(pinfl_month), pinfl_search=json.dumps(pinfl_search),
                           tt_week=json.dumps(tt_week), tt_month=json.dumps(tt_month),
                           tt_search=json.dumps(tt_search), tab=json.dumps(tab_p2p))


@app.route("/dates_offshore")
def dates_offshore():
    Back.start_date = request.args["start_date"]
    Back.end_date = request.args["end_date"]
    Back.flag_offshore = request.args["flag"]
    return "OK"


@app.route("/offshore")
def offshore():
    Back.reconnect_to_db()
    cyprus_week, cyprus_month, cyprus_search = Back.offshore_data(Back.cursor, Back.start_date, Back.end_date)

    if Back.flag_offshore == 'cyprus':
        tab_offshore = 'cyprus'
    else:
        tab_offshore = ''
    Back.flag_offshore = ''

    return render_template("offshore.html", cyprus_week=json.dumps(cyprus_week), cyprus_month=json.dumps(cyprus_month),
                           cyprus_search=json.dumps(cyprus_search), tab=json.dumps(tab_offshore))


@app.route('/download')
def download():
    flag = request.args['flag']
    path = Back.create_file_func(flag)
    return send_file(path, as_attachment=True)


app.run(host="0.0.0.0", port=80)

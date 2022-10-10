import json
from Python import BackOfWebApp as Back
from flask import Flask, render_template, redirect, url_for, request, send_file  # pip install flask
# from waitress import serve  # pip install waitress

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('login'))


@app.errorhandler(500)
def page_not_found(error):
    return redirect(url_for('login'))


@app.route("/login")
def login():
    Back.reconnect_to_db()
    return render_template("login.html")


@app.route("/dates")
def dates():
    Back.flags_change_func(request.args["start_date"], request.args["end_date"], request.args["flag"])
    return "OK"


@app.route("/index")
def index():
    Back.reconnect_to_db()
    return render_template("index.html")


@app.route("/mrot")
def mrot():
    Back.reconnect_to_db()
    month, week, day = Back.mrot_data(Back.cursor)
    return render_template("mrot.html", month=json.dumps(month), week=json.dumps(week), day=json.dumps(day))


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


@app.route("/bank")
def bank():
    Back.reconnect_to_db()
    offshore_day, offshore_search, questions_day, questions_search, brv_month, brv_day = \
        Back.bank_data(Back.cursor, Back.start_date, Back.end_date)

    if Back.flag_bank == 'offshore':
        tab_bank = 'offshore'
    elif Back.flag_bank == 'questions':
        tab_bank = 'questions'
    elif Back.flag_bank == 'brv':
        tab_bank = 'brv'
    else:
        tab_bank = ''
    Back.flag_bank = ''
    print(tab_bank)

    return render_template("bank.html", offshore_day=json.dumps(offshore_day),
                           offshore_search=json.dumps(offshore_search), questions_day=json.dumps(questions_day),
                           questions_search=json.dumps(questions_search), brv_month=json.dumps(brv_month),
                           brv_day=json.dumps(brv_day), tab=json.dumps(tab_bank))


@app.route('/download_tab')
def download_tab():
    Back.flag_tab = request.args['flag']
    return 'Ok'


@app.route('/download_sort')
def download_sort():
    Back.flag_sort = request.args['flag']
    return 'Ok'


@app.route('/download')
def download():
    Back.choose_table_func()
    return send_file(Back.path, as_attachment=True)


# serve(app, host="0.0.0.0", port=80)
app.run(host="0.0.0.0", port=80)

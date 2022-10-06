import os
import pandas as pd
import mysql.connector
from Python import variables as var

start_date = end_date = var.today
flag_octo = ''
flag_p2p = ''
flag_bank = ''
flag_tab = ''
flag_sort = ''
path = ''


def db_connection_func():

    my_db = mysql.connector.connect(
        host="localhost",
        user=f"{var.username_db}",
        password=f"{var.password_db}",
        database="PodFT"
    )

    my_cursor = my_db.cursor()

    return my_cursor, my_db


def reconnect_to_db():
    global cursor, db
    cursor, db = db_connection_func()


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
                      f"WHERE (time_id BETWEEN '{start}' AND '{end}') AND NOT pinfl='nan') "
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


def bank_data(my_cursor, start, end):
    bank_offshore_day = []
    my_cursor.execute("SELECT * FROM offshore_day;")
    data = my_cursor.fetchall()
    for row in data:
        bank_offshore_day.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[4],
            'operation_date': (str(row[5])[0:10]),
            'amount': row[6],
            'country': row[8]})

    bank_offshore_search = []
    my_cursor.execute("SELECT fio, birth_date, document_number, time_id, amount, country FROM  Initial_Data_P2P "
                      f"WHERE (time_id BETWEEN '{start}' AND '{end}') "
                      "AND country IN (SELECT * FROM offshore_countries) ORDER BY time_id;")
    data = my_cursor.fetchall()
    for row in data:
        bank_offshore_search.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[2],
            'operation_date': (str(row[3])[0:10]),
            'amount': row[4],
            'country': row[5]})

    bank_questions_day = []
    my_cursor.execute("SELECT * FROM questionable_operations_day;")
    data = my_cursor.fetchall()
    for row in data:
        bank_questions_day.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[4],
            'operation_date': (str(row[5])[0:10]),
            'amount': row[6],
            'merchant': row[9],
            'mcc': row[10]})

    bank_questions_search = []
    my_cursor.execute("SELECT fio, birth_date, document_number, time_id, amount, merch_name, mcc "
                      f"FROM  Initial_Data_P2P WHERE (time_id BETWEEN '{start}' AND '{end}') "
                      "AND (mcc='7995' OR mcc='6211') ORDER BY time_id;")
    data = my_cursor.fetchall()
    for row in data:
        bank_questions_search.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[2],
            'operation_date': (str(row[3])[0:10]),
            'amount': row[4],
            'merchant': row[5],
            'mcc': row[6]})

    bank_brv_month = []
    my_cursor.execute("SELECT * FROM brv_month LIMIT 100;")
    data = my_cursor.fetchall()
    for row in data:
        bank_brv_month.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[4],
            'amount': row[5],
            'block': row[6],
            'observation': row[7]})

    bank_brv_day = []
    my_cursor.execute("SELECT * FROM brv_day LIMIT 100;")
    data = my_cursor.fetchall()
    for row in data:
        bank_brv_month.append({
            'person': row[0],
            'birthday': row[1],
            'passport': row[4],
            'amount': row[5],
            'block': row[6],
            'observation': row[7]})

    return bank_offshore_day, bank_offshore_search, bank_questions_day, bank_questions_search, bank_brv_month, \
        bank_brv_day


def choose_table_func():
    page = flag_tab[:flag_tab.find('_')]
    tab = flag_tab[flag_tab.find('_')+1:]
    sort = flag_sort[flag_sort.find('_')+1:]
    if page == 'Mrot':
        if tab == 'Month':
            return create_file_from_table_func(db, 'mrot_month')
        elif tab == 'Week':
            return create_file_from_table_func(db, 'mrot_week')
        elif tab == 'Day':
            return create_file_from_table_func(db, 'mrot_day')
    elif page == 'OCTO':
        if tab == 'Sender':
            if sort == 'Week':
                return create_file_from_table_func(db, 'card_sender_octo_week')
            elif sort == 'Month':
                return create_file_from_table_func(db, 'card_sender_octo_month')
            elif sort == 'From':
                return create_file_from_data_func(db, 'card_sender_octo')
        elif tab == 'Receiver':
            if sort == 'Week':
                return create_file_from_table_func(db, 'number_receiver_octo_week')
            elif sort == 'Month':
                return create_file_from_table_func(db, 'number_receiver_octo_month')
            elif sort == 'From':
                return create_file_from_data_func(db, 'number_receiver_octo')
    elif page == 'P2P':
        if tab == 'Country':
            if sort == 'Week':
                return create_file_from_table_func(db, 'country_p2p_week')
            elif sort == 'Month':
                return create_file_from_table_func(db, 'country_p2p_month')
            elif sort == 'From':
                return create_file_from_data_func(db, 'country_p2p')
        elif tab == 'Pinfl':
            if sort == 'Week':
                return create_file_from_table_func(db, 'pinfl_receiver_week')
            elif sort == 'Month':
                return create_file_from_table_func(db, 'pinfl_receiver_month')
            elif sort == 'From':
                return create_file_from_data_func(db, 'pinfl_receiver')
        elif tab == 'TT':
            if sort == 'Week':
                return create_file_from_table_func(db, 'trans_gran_to_tt_week')
            elif sort == 'Month':
                return create_file_from_table_func(db, 'trans_gran_to_tt_month')
            elif sort == 'From':
                return create_file_from_table_func(db, 'trans_gran_to_tt')
    elif page == 'Bank':
        if tab == 'Offshore':
            if sort == 'Day':
                return create_file_from_table_func(db, 'offshore_day')
            elif sort == 'From':
                return create_file_from_data_func(db, 'offshore')
        elif tab == 'Questions':
            if sort == 'Day':
                return create_file_from_table_func(db, 'questionable_operations_day')
            elif sort == 'From':
                return create_file_from_data_func(db, 'questionable_operations')
        elif tab == 'BRV':
            if sort == 'Month':
                return create_file_from_table_func(db, 'brv_month')
            elif sort == 'Day':
                return create_file_from_table_func(db, 'brv_day')


def create_file_from_table_func(my_db, table_name):
    global path
    if len(path) > 0:
        delete_file(path)

    sql_query = pd.read_sql_query(f'SELECT * FROM {table_name}', my_db)
    df = pd.DataFrame(sql_query)
    df.to_csv(fr'Files/{table_name}.csv', index=False)
    path = f'Files/{table_name}.csv'


def create_file_from_data_func(my_db, table_name):
    global path, start_date, end_date
    if len(path) > 0:
        delete_file(path)

    if table_name == 'card_sender_octo':
        sql_query = pd.read_sql_query("SELECT masked_card_number, COUNT(*) count, SUM(amount) amount FROM "
                                      "(SELECT DISTINCT masked_card_number, created_date, amount "
                                      "FROM Initial_Data_OCTO "
                                      f"WHERE created_date BETWEEN '{start_date}' AND '{end_date}' "
                                      "AND NOT masked_card_number='nan') "
                                      "X GROUP BY masked_card_number ORDER BY count DESC, amount DESC;", my_db)
    elif table_name == 'number_receiver_octo':
        sql_query = pd.read_sql_query("SELECT dest_tool_id, COUNT(*) count, SUM(amount) amount FROM "
                                      "(SELECT DISTINCT dest_tool_id, created_date, amount FROM Initial_Data_OCTO "
                                      f"WHERE created_date BETWEEN '{start_date}' AND '{end_date}' "
                                      "AND NOT dest_tool_id='nan') "
                                      "X GROUP BY dest_tool_id ORDER BY amount DESC, count DESC;", my_db)
    elif table_name == 'country_p2p':
        sql_query = pd.read_sql_query("SELECT country, COUNT(*) count, SUM(amount) amount FROM "
                                      "(SELECT DISTINCT country, time_id, amount FROM Initial_Data_P2P "
                                      f"WHERE time_id BETWEEN '{start_date}' AND '{end_date}' "
                                      "AND NOT country='nan') "
                                      "X GROUP BY country ORDER BY count DESC, amount DESC;", my_db)
    elif table_name == 'pinfl_receiver':
        sql_query = pd.read_sql_query("SELECT pinfl, COUNT(*) count, SUM(amount) amount FROM "
                                      "(SELECT DISTINCT pinfl, time_id, amount FROM Initial_Data_P2P "
                                      f"WHERE time_id BETWEEN '{start_date}' AND '{end_date}' "
                                      "AND NOT pinfl='nan') "
                                      "X GROUP BY pinfl ORDER BY count DESC, amount DESC;", my_db)
    elif table_name == 'trans_gran_to_tt':
        sql_query = pd.read_sql_query("SELECT pos_code, COUNT(*) count FROM "
                                      "(SELECT DISTINCT pos_code, time_id FROM Initial_Data_P2P "
                                      f"WHERE time_id BETWEEN '{start_date}' AND '{end_date}' "
                                      "AND NOT pos_code='nan') "
                                      "X GROUP BY pos_code ORDER BY count DESC;", my_db)
    elif table_name == 'offshore':
        sql_query = pd.read_sql_query("SELECT fio, birth_date, citizenship, registration_address, document_number, "
                                      "time_id, amount, currency, country, merch_name, mcc FROM  Initial_Data_P2P "
                                      f"WHERE (time_id BETWEEN '{start_date}' AND '{end_date}') "
                                      "AND country IN (SELECT * from offshore_countries) ORDER BY time_id;", my_db)
    elif table_name == 'questionable_operations':
        sql_query = pd.read_sql_query("SELECT fio, birth_date, citizenship, registration_address, document_number, "
                                      "time_id, amount, currency, country, merch_name, mcc FROM  Initial_Data_P2P "
                                      f"WHERE (time_id BETWEEN '{start_date}' AND '{end_date}') "
                                      "AND (mcc='7995' OR mcc='6211')"
                                      "ORDER BY time_id;", my_db)
    df = pd.DataFrame(sql_query)
    df.to_csv(fr'Files/{table_name}.csv', index=False)
    path = f'Files/{table_name}.csv'


def delete_file(file):
    os.remove(file)
    return "Ok"


def flags_change_func(start, end, flag):
    for n in (start[:4] + start[5:7] + start[8:] + end[:4] + end[5:7] + end[8:]):
        if n not in '0123456789':
            return "404"

    global start_date, end_date
    if flag == 'offshore' or flag == 'questions' or flag == 'brv':
        global flag_bank
        start_date = start
        end_date = end
        flag_bank = flag
    elif flag == 'tt' or flag == 'pinfl' or flag == 'country':
        global flag_p2p
        start_date = start
        end_date = end
        flag_p2p = flag
    elif flag == 'receiver' or flag == 'sender':
        global flag_octo
        start_date = start
        end_date = end
        flag_octo = flag


cursor, db = db_connection_func()

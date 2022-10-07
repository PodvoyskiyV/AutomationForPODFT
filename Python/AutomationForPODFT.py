import pandas as pd  # pip install pandas
import pyfiglet  # pip install pyfiglet
import mysql.connector  # pip install mysql-connector-python
import datetime
import pysftp  # pip install pysftp
import os
import variables as var
from termcolor import colored  # pip install termcolor

banner = pyfiglet.figlet_format('Pod FT')
print(colored(banner, 'green'))


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


def sftp_connection_func():
    with pysftp.Connection(host=var.hostname_sftp, username=var.username_sftp, password=var.password_sftp) as sftp:
        sftp.get("remoteOCTOFilePath", "localOCTOFilePath")
        sftp.get("remoteP2PFilePath", "localP2PFilePath")


def octo_to_db_func(my_cursor, my_db):
    start_octo_to_db_func = datetime.datetime.now()

    for i in range(len(FullDataOCTO)):
        sql = "INSERT INTO Initial_Data_OCTO (octo_trxn_id, created_date, masked_card_number, amount, currency, " \
              "transaction_status, provider_id, dest_tool_id, customer_id, type_description, schema_id, " \
              "bill_account_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (f"{FullDataOCTO.iloc[i].octo_trxn_id}", f"{FullDataOCTO.iloc[i].created_date[:-6]}",
               f"{FullDataOCTO.iloc[i].masked_card_number}", f"{FullDataOCTO.iloc[i].amount}",
               f"{FullDataOCTO.iloc[i].currency}", f"{FullDataOCTO.iloc[i].transaction_status}",
               f"{FullDataOCTO.iloc[i].provider_id}", f"{FullDataOCTO.iloc[i].dest_tool_id}",
               f"{FullDataOCTO.iloc[i].customer_id}", f"{FullDataOCTO.iloc[i].type_description}",
               f"{FullDataOCTO.iloc[i].schema_id}", f"{FullDataOCTO.iloc[i].bill_account_id}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_octo_to_db_func = datetime.datetime.now()
    print(f'octo_to_db_func ended in {end_octo_to_db_func - start_octo_to_db_func}')


def p2p_to_db_func(my_cursor, my_db):
    start_p2p_to_db_func = datetime.datetime.now()

    for i in range(len(FullDataP2P)):
        sql = "INSERT INTO Initial_Data_P2P (time_id, customer_id, user_id, operation_type, amount, currency_code, " \
              "currency, currency_name, country_code, mcc, merch_name, country, masked_card_number, " \
              "card_status, fio, birth_date, citizenship, registration_address, document_number, doc_type, pinfl, " \
              "pos_code, pos_name) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (f"{FullDataP2P.iloc[i].time_id}", f"{FullDataP2P.iloc[i].customer_id}",
               f"{FullDataP2P.iloc[i].user_id}", f"{FullDataP2P.iloc[i].operation_type}",
               f"{FullDataP2P.iloc[i].amount}", f"{FullDataP2P.iloc[i].currency_code}",
               f"{FullDataP2P.iloc[i].currency}", f"{FullDataP2P.iloc[i].currency_name}",
               f"{FullDataP2P.iloc[i].acq_country_code}", f"{FullDataP2P.iloc[i].acq_mcc}",
               f"{FullDataP2P.iloc[i].acq_merch_name}", f"{FullDataP2P.iloc[i].country}",
               f"{FullDataP2P.iloc[i].masked_card_number}", f"{FullDataP2P.iloc[i].card_status}",
               f"{FullDataP2P.iloc[i].fio}", f"{FullDataP2P.iloc[i].birth_date}",
               f"{FullDataP2P.iloc[i].citizenship}", f"{FullDataP2P.iloc[i].registration_address}",
               f"{FullDataP2P.iloc[i].document_number}", f"{FullDataP2P.iloc[i].doc_type}",
               f"{FullDataP2P.iloc[i].pinfl}", f"{FullDataP2P.iloc[i].pos_code}",
               f"{FullDataP2P.iloc[i].pos_name}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_p2p_to_db_func = datetime.datetime.now()
    print(f'p2p_to_db_func ended in {end_p2p_to_db_func - start_p2p_to_db_func}')


def trans_gran_to_tt_func(my_cursor, my_db, start, table):
    start_trans_gran_to_tt_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE trans_gran_to_tt_{table};")
    my_db.commit()

    my_cursor.execute("SELECT pos_code, COUNT(*) count FROM "
                      "(SELECT DISTINCT pos_code, time_id FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{var.today}' "
                      "AND NOT pos_code='nan') "
                      "X GROUP BY pos_code ORDER BY count DESC;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO trans_gran_to_tt_{table} (pos_code, count) VALUES (%s, %s)"
        val = (f"{row[0]}", f"{row[1]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_trans_gran_tt_func = datetime.datetime.now()
    print(f'trans_gran_to_tt_func ended in {end_trans_gran_tt_func - start_trans_gran_to_tt_func}')


def pinfl_receiver_func(my_cursor, my_db, start, table):
    start_pinfl_receiver_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE pinfl_receiver_{table};")
    my_db.commit()

    my_cursor.execute("SELECT pinfl, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT pinfl, time_id, amount FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{var.today}' "
                      "AND NOT pinfl='nan') "
                      "X GROUP BY pinfl ORDER BY count DESC, amount DESC;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO pinfl_receiver_{table} (pinfl, count, amount) VALUES (%s, %s, %s)"
        val = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_pinfl_receiver_func = datetime.datetime.now()
    print(f'pinfl_receiver_func ended in {end_pinfl_receiver_func - start_pinfl_receiver_func}')


def country_p2p_func(my_cursor, my_db, start, table):
    start_country_p2p_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE country_p2p_{table};")
    my_db.commit()

    my_cursor.execute("SELECT country, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT country, time_id, amount FROM Initial_Data_P2P "
                      f"WHERE time_id BETWEEN '{start}' AND '{var.today}' "
                      "AND NOT country='nan') "
                      "X GROUP BY country ORDER BY count DESC, amount DESC;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO country_p2p_{table} (country, count, amount) VALUES (%s, %s, %s)"
        val = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_country_p2p_func = datetime.datetime.now()
    print(f'country_p2p_func ended in {end_country_p2p_func - start_country_p2p_func}')


def number_receiver_octo_func(my_cursor, my_db, start, table):
    start_number_receiver_octo_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE number_receiver_octo_{table};")
    my_db.commit()

    my_cursor.execute("SELECT dest_tool_id, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT dest_tool_id, created_date, amount FROM Initial_Data_OCTO "
                      f"WHERE created_date BETWEEN '{start}' AND '{var.today}' "
                      "AND NOT dest_tool_id='nan') "
                      "X GROUP BY dest_tool_id ORDER BY amount DESC, count DESC;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO number_receiver_octo_{table} (dest_tool_id, count, amount) VALUES (%s, %s, %s)"
        val = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_number_receiver_octo_func = datetime.datetime.now()
    print(f'number_receiver_octo_func ended in {end_number_receiver_octo_func - start_number_receiver_octo_func}')


def card_sender_octo_func(my_cursor, my_db, start, table):
    start_card_sender_octo_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE card_sender_octo_{table};")
    my_db.commit()

    my_cursor.execute("SELECT masked_card_number, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT masked_card_number, created_date, amount FROM Initial_Data_OCTO "
                      f"WHERE created_date BETWEEN '{start}' AND '{var.today}' "
                      "AND NOT masked_card_number='nan') "
                      "X GROUP BY masked_card_number ORDER BY count DESC, amount DESC;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO card_sender_octo_{table} (masked_card_number, count, amount) VALUES (%s, %s, %s)"
        val = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_card_sender_octo_func = datetime.datetime.now()
    print(f'card_sender_octo_func ended in {end_card_sender_octo_func - start_card_sender_octo_func}')


def mrot_func(my_cursor, my_db, start, t):
    start_mrot_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE mrot_{t};")
    my_db.commit()

    if t == 'month':
        my_cursor.execute("SELECT masked_card_number, COUNT(*) count, SUM(amount) amount, "
                          f"IF(SUM(amount) > {var.mrot_150}, '+', '-') AS block, "
                          f"IF(SUM(amount) < {var.mrot_150} AND SUM(amount) > {var.mrot_150 * 0.9}, '+', '-') "
                          "AS observation  FROM (SELECT DISTINCT masked_card_number, created_date, amount"
                          f" FROM Initial_Data_OCTO WHERE created_date BETWEEN '{start}' AND '{var.today}' "
                          "AND NOT masked_card_number='nan') "
                          "X GROUP BY masked_card_number ORDER BY amount DESC, count DESC;")
        data = my_cursor.fetchall()

        for row in data:
            sql = f"INSERT INTO mrot_{t} (masked_card_number, count, amount, block, observation) " \
                  "VALUES (%s, %s, %s, %s, %s)"
            val = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}", f"{row[4]}")
            my_cursor.execute(sql, val)
            my_db.commit()
    elif t == 'week':
        my_cursor.execute("SELECT masked_card_number, COUNT(*) count, SUM(amount) amount, "
                          f"IF(SUM(amount) > {var.mrot_150 * 0.9 / 30 * 7}, '+', '-') AS observation "
                          "FROM (SELECT DISTINCT masked_card_number, created_date, amount "
                          f"FROM Initial_Data_OCTO WHERE created_date BETWEEN '{start}' AND '{var.today}' "
                          "AND NOT masked_card_number='nan') "
                          "X GROUP BY masked_card_number ORDER BY amount DESC, count DESC;")
        data = my_cursor.fetchall()

        for row in data:
            sql = f"INSERT INTO mrot_{t} (masked_card_number, count, amount, observation) " \
                  "VALUES (%s, %s, %s, %s)"
            val = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}")
            my_cursor.execute(sql, val)
            my_db.commit()
    else:
        my_cursor.execute("SELECT masked_card_number, COUNT(*) count, SUM(amount) amount, "
                          f"IF(SUM(amount) > {var.mrot_150 * 0.9 / 30}, '+', '-') AS observation "
                          "FROM (SELECT DISTINCT masked_card_number, created_date, amount "
                          f"FROM Initial_Data_OCTO WHERE created_date BETWEEN '{start}' AND '{var.today}' "
                          "AND NOT masked_card_number='nan') "
                          "X GROUP BY masked_card_number ORDER BY amount DESC, count DESC;")
        data = my_cursor.fetchall()

        for row in data:
            sql = f"INSERT INTO mrot_{t} (masked_card_number, count, amount, observation) " \
                  "VALUES (%s, %s, %s, %s)"
            val = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}")
            my_cursor.execute(sql, val)
            my_db.commit()

    end_mrot_func = datetime.datetime.now()
    print(f'mrot_func ended in {end_mrot_func - start_mrot_func}')


def offshore_func(my_cursor, my_db, start, table):
    start_offshore_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE offshore_{table};")
    my_db.commit()

    my_cursor.execute("SELECT fio, birth_date, citizenship, registration_address, document_number, time_id, amount, "
                      "currency, country, merch_name, mcc FROM  Initial_Data_P2P "
                      f"WHERE (time_id BETWEEN '{start}' AND '{var.today}') "
                      f"AND country IN (SELECT * FROM offshore_countries) ORDER BY time_id;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO offshore_{table} (person, birthday, citizenship, registration_address, passport, " \
              "operation_date, amount, currency, country, merch_name, mcc) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}", f"{row[4]}", f"{str(row[5])[0:10]}", f"{row[6]}",
               f"{row[7]}", f"{row[8]}", f"{row[9]}", f"{row[10]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_offshore_func = datetime.datetime.now()
    print(f'offshore_func ended in {end_offshore_func - start_offshore_func}')


def questionable_operations_func(my_cursor, my_db, start, table):
    start_questionable_operations_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE questionable_operations_{table};")
    my_db.commit()

    my_cursor.execute("SELECT fio, birth_date, citizenship, registration_address, document_number, time_id, amount, "
                      "currency, country, merch_name, mcc FROM  Initial_Data_P2P "
                      f"WHERE (time_id BETWEEN '{start}' AND '{var.today}') AND (mcc='7995' OR mcc='6211') "
                      # "AND NOT country='Cyprus'"
                      "ORDER BY time_id;")  # AND NOT country='nan'
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO questionable_operations_{table} (person, birthday, citizenship, registration_address, " \
              f"passport, operation_date, amount, currency, country, merch_name, mcc) " \
              f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}", f"{row[4]}", f"{str(row[5])[0:10]}", f"{row[6]}",
               f"{row[7]}", f"{row[8]}", f"{row[9]}", f"{row[10]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_questionable_operations_func = datetime.datetime.now()
    print(f'questionable_operations_func ended in {end_questionable_operations_func - start_questionable_operations_func}')


def brv_func(my_cursor, my_db, start, table):
    start_brv_func = datetime.datetime.now()

    my_cursor.execute(f"TRUNCATE TABLE brv_{table};")
    my_db.commit()

    if table == 'month':
        my_cursor.execute("SELECT fio, birth_date, citizenship, registration_address, document_number, "
                          f"SUM(amount) AS amount, IF(SUM(amount) > {var.brv_500}, '+', '-') AS block, "
                          f"IF(SUM(amount) < {var.brv_500} AND SUM(amount) > {var.brv_500 * 0.9}, '+', '-') "
                          "AS observation FROM (SELECT DISTINCT fio, birth_date, citizenship, registration_address, "
                          "document_number, amount FROM  Initial_Data_P2P "
                          f"WHERE (time_id BETWEEN '{start}' AND '{var.today}') "
                          "AND operation_type='Incoming P2P transfer' ) "
                          "X GROUP BY document_number, fio, birth_date, citizenship, registration_address "
                          "ORDER BY amount DESC;")
        data = my_cursor.fetchall()

        for row in data:
            sql = f"INSERT INTO brv_{table} (person, birthday, citizenship, registration_address, passport, amount, " \
                  "block, observation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}", f"{row[4]}", f"{row[5]}", f"{row[6]}",
                   f"{row[7]}")
            my_cursor.execute(sql, val)
            my_db.commit()

    elif table == 'day':
        my_cursor.execute("SELECT fio, birth_date, citizenship, registration_address, document_number, "
                          f"SUM(amount) AS amount, IF(SUM(amount) > {var.brv_500}, '+', '-') AS block, "
                          f"IF(SUM(amount) < {var.brv_500} AND SUM(amount) > {var.brv_500 * 0.9}, '+', '-') "
                          "AS observation FROM (SELECT DISTINCT fio, birth_date, citizenship, registration_address, "
                          "document_number, amount FROM  Initial_Data_P2P "
                          f"WHERE (time_id BETWEEN '{start}' AND '{var.today}') AND (mcc='6010' OR mcc='6011')) "
                          "X GROUP BY document_number, fio, birth_date, citizenship, registration_address "
                          "ORDER BY amount DESC;")
        data = my_cursor.fetchall()

        for row in data:
            sql = f"INSERT INTO brv_{table} (person, birthday, citizenship, registration_address, passport, amount, " \
                  "block, observation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}", f"{row[4]}", f"{row[5]}", f"{row[6]}",
                   f"{row[7]}")
            my_cursor.execute(sql, val)
            my_db.commit()

    end_brv_func = datetime.datetime.now()
    print(f'brv_func ended in {end_brv_func - start_brv_func}')


def delete_files_func():
    os.remove(f"{FullDataOCTO}")
    os.remove(f"{FullDataP2P}")


try:
    start_program = datetime.datetime.now()
    print(f'Program started at: {start_program} \n')

    FullDataOCTO = pd.read_csv('~/AutomationForPODFT/Python/OCTO 06.10.22.csv', sep=',')
    FullDataP2P = pd.read_csv('~/AutomationForPODFT/Python/p2p 06.10.22.csv', sep=',')

    cursor, db = db_connection_func()

    octo_to_db_func(cursor, db)
    p2p_to_db_func(cursor, db)
    mrot_func(cursor, db, var.yesterday, 'day')
    offshore_func(cursor, db, var.yesterday, 'day')
    questionable_operations_func(cursor, db, var.yesterday, 'day')
    brv_func(cursor, db, var.month_ago, 'month')
    brv_func(cursor, db, var.yesterday, 'day')

    if var.current_week_day == 'Monday':
        trans_gran_to_tt_func(cursor, db, var.week_ago, 'week')
        pinfl_receiver_func(cursor, db, var.week_ago, 'week')
        country_p2p_func(cursor, db, var.week_ago, 'week')
        number_receiver_octo_func(cursor, db, var.week_ago, 'week')
        card_sender_octo_func(cursor, db, var.week_ago, 'week')
        mrot_func(cursor, db, var.week_ago, 'week')
    if var.current_day == '1':
        trans_gran_to_tt_func(cursor, db, f"{var.previous_month}-01", 'month')
        pinfl_receiver_func(cursor, db, f"{var.previous_month}-01", 'month')
        country_p2p_func(cursor, db, f"{var.previous_month}-01", 'month')
        number_receiver_octo_func(cursor, db, f"{var.previous_month}-01", 'month')
        card_sender_octo_func(cursor, db, f"{var.previous_month}-01", 'month')
        mrot_func(cursor, db, f"{var.previous_month}-01", 'month')

    end_program = datetime.datetime.now()
    print(f'\nProgram ended in {end_program - start_program}')
    print(end_program)
except KeyboardInterrupt:
    print("\n Program finished by user !!!!")

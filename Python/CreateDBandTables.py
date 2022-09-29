import mysql.connector
import variables as var


def db_connection():

    my_db = mysql.connector.connect(
        host="localhost",
        user=f"{var.username_db}",
        password=f"{var.password_db}",
        database="PodFT"
    )

    my_cursor = my_db.cursor()

    return my_cursor, my_db


def db_connection_func():

    my_db = mysql.connector.connect(
        host="localhost",
        user=f"{var.username_db}",
        password=f"{var.password_db}"
    )

    my_cursor = my_db.cursor()
    my_cursor.execute("CREATE DATABASE PodFT")
    my_cursor.close()

    my_db = mysql.connector.connect(
        host="localhost",
        user=f"{var.username_db}",
        password=f"{var.password_db}",
        database="PodFT"
    )

    my_cursor = my_db.cursor()

    return my_cursor, my_db


def create_octo_table_func(my_cursor):
    sql = "CREATE TABLE Initial_Data_OCTO (octo_trxn_id VARCHAR(255), created_date TIMESTAMP(3), " \
          "masked_card_number VARCHAR(255), amount DOUBLE(30, 2), currency VARCHAR(255), " \
          "transaction_status VARCHAR(255), provider_id VARCHAR(255), dest_tool_id VARCHAR(255), " \
          "customer_id VARCHAR(255), type_description VARCHAR(255), schema_id VARCHAR(255), " \
          "bill_account_id VARCHAR(255));"

    my_cursor.execute(sql)


def create_p2p_table_func(my_cursor):
    sql = "CREATE TABLE Initial_Data_P2P (time_id TIMESTAMP(3), customer_id VARCHAR(255), user_id VARCHAR(255), " \
          "operation_type VARCHAR(255), amount DOUBLE(30, 2), currency_code VARCHAR(255), currency VARCHAR(255), " \
          "currency_name VARCHAR(255), country_code VARCHAR(255), mcc VARCHAR(255), " \
          "merch_name VARCHAR(255), country VARCHAR(255), masked_card_number VARCHAR(255), " \
          "card_status VARCHAR(255), fio VARCHAR(255), birth_date VARCHAR(255), citizenship VARCHAR(255), " \
          "registration_address VARCHAR(255), document_number VARCHAR(255), doc_type VARCHAR(255), " \
          "pinfl VARCHAR(255), pos_code VARCHAR(255), pos_name VARCHAR(255))"
    my_cursor.execute(sql)


def create_trans_gran_to_tt(my_cursor, t):
    sql = f"CREATE TABLE trans_gran_to_tt_{t} (pos_code VARCHAR(255), count INT(255))"
    my_cursor.execute(sql)


def create_pinfl_receiver(my_cursor, t):
    sql = f"CREATE TABLE pinfl_receiver_{t} (pinfl VARCHAR(255), count INT(255), amount DOUBLE(30, 2))"
    my_cursor.execute(sql)


def create_country_p2p(my_cursor, t):
    sql = f"CREATE TABLE country_p2p_{t} (country VARCHAR(255), count INT(255), amount DOUBLE(30, 2))"
    my_cursor.execute(sql)


def create_number_receiver_octo(my_cursor, t):
    sql = f"CREATE TABLE number_receiver_octo_{t} (dest_tool_id VARCHAR(255), count INT(255), amount DOUBLE(30, 2))"
    my_cursor.execute(sql)


def create_card_sender_octo(my_cursor, t):
    sql = f"CREATE TABLE card_sender_octo_{t} (masked_card_number VARCHAR(255), count INT(255), amount DOUBLE(30, 2))"
    my_cursor.execute(sql)


def create_mrot(my_cursor, t):
    if t == 'month':
        sql = f"CREATE TABLE mrot_{t} (masked_card_number VARCHAR(255), count INT(255), " \
              "amount DOUBLE(30, 2), block VARCHAR(255), observation VARCHAR(255))"
    else:
        sql = f"CREATE TABLE mrot_{t} (masked_card_number VARCHAR(255), count INT(255), " \
              "amount DOUBLE(30, 2), observation VARCHAR(255))"
    my_cursor.execute(sql)


def create_offshore(my_cursor, t):
    sql = f"CREATE TABLE offshore_{t} (person VARCHAR(255), birthday VARCHAR(255), citizenship VARCHAR(255), " \
          "registration_address VARCHAR(255), passport VARCHAR(255), operation_date DATE, amount DOUBLE(30, 2), " \
          "currency VARCHAR(255), country VARCHAR(255), merch_name VARCHAR(255), mcc VARCHAR(255));"
    my_cursor.execute(sql)


def create_brv(my_cursor, t):
    if t == 'month':
        sql = f"CREATE TABLE brv_{t} (person VARCHAR(255), birthday VARCHAR(255), citizenship VARCHAR(255), " \
              "registration_address VARCHAR(255), passport VARCHAR(255), amount DOUBLE(30, 2), block VARCHAR(255), " \
              "observation VARCHAR(255));"
    elif t == 'day':
        sql = f"CREATE TABLE brv_{t} (person VARCHAR(255), birthday VARCHAR(255), citizenship VARCHAR(255), " \
              "registration_address VARCHAR(255), passport VARCHAR(255), amount DOUBLE(30, 2), block VARCHAR(255), " \
              "observation VARCHAR(255));"
    my_cursor.execute(sql)


def create_questionable_operations(my_cursor, t):
    sql = f"CREATE TABLE questionable_operations_{t} (person VARCHAR(255), birthday VARCHAR(255), " \
          "citizenship VARCHAR(255), registration_address VARCHAR(255), passport VARCHAR(255), operation_date DATE, " \
          "amount DOUBLE(30, 2), currency VARCHAR(255), country VARCHAR(255), merch_name VARCHAR(255), " \
          "mcc VARCHAR(255));"
    my_cursor.execute(sql)


cursor, db = db_connection_func()
# cursor, db = db_connection()

create_octo_table_func(cursor)
create_p2p_table_func(cursor)

create_trans_gran_to_tt(cursor, 'week')
create_trans_gran_to_tt(cursor, 'month')
create_pinfl_receiver(cursor, 'week')
create_pinfl_receiver(cursor, 'month')
create_country_p2p(cursor, 'week')
create_country_p2p(cursor, 'month')
create_number_receiver_octo(cursor, 'week')
create_number_receiver_octo(cursor, 'month')
create_card_sender_octo(cursor, 'week')
create_card_sender_octo(cursor, 'month')
create_mrot(cursor, 'day')
create_mrot(cursor, 'week')
create_mrot(cursor, 'month')

create_offshore(cursor, 'day')

create_questionable_operations(cursor, 'day')

create_brv(cursor, 'day')
create_brv(cursor, 'month')


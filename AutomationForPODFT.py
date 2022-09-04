import pandas as pd  # pip install pandas
import pyfiglet  # pip install pyfiglet
import mysql.connector  # pip install mysql-connector-python
import datetime
import variables as var
from termcolor import colored  # pip install termcolor

banner = pyfiglet.figlet_format('Pod FT')
print(colored(banner, 'green'))


def db_connection_func():
    start_db_connection_func = datetime.datetime.now()

    my_db = mysql.connector.connect(
        host="localhost",
        user=f"{var.username}",
        password=f"{var.password}",
        database="PodFT"
    )

    my_cursor = my_db.cursor()

    end_db_connection_func = datetime.datetime.now()
    print(f'db_connection_func ended in {end_db_connection_func - start_db_connection_func}')

    return my_cursor, my_db


def octo_to_db_func(my_cursor, mydb):
    start_octo_to_db_func = datetime.datetime.now()

    for i in range(len(FullDataOCTO)):
        sql = "INSERT INTO Initial_Data_OCTO (octo_trxn_id, created_date, masked_card_number, amount, currency, " \
              "transaction_status, provider_id, dest_tool_id, customer_id, type_description, bill_account_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (f"{FullDataOCTO.iloc[i].octo_trxn_id}", f"{FullDataOCTO.iloc[i].created_date}",
               f"{FullDataOCTO.iloc[i].masked_card_number}", f"{FullDataOCTO.iloc[i].amount}",
               f"{FullDataOCTO.iloc[i].currency}", f"{FullDataOCTO.iloc[i].transaction_status}",
               f"{FullDataOCTO.iloc[i].provider_id}", f"{FullDataOCTO.iloc[i].dest_tool_id}",
               f"{FullDataOCTO.iloc[i].customer_id}", f"{FullDataOCTO.iloc[i].type_description}",
               f"{FullDataOCTO.iloc[i].bill_account_id}")
        my_cursor.execute(sql, val)
        mydb.commit()

    my_cursor.close()

    end_octo_to_db_func = datetime.datetime.now()
    print(f'octo_to_db_func ended in {end_octo_to_db_func - start_octo_to_db_func}')


def p2p_to_db_func(my_cursor, mydb):
    start_p2p_to_db_func = datetime.datetime.now()

    for i in range(len(FullDataP2P)):
        sql = "INSERT INTO Initial_Data_P2P (time_id, customer_id, user_id, operation_type, amount, currency, " \
              "country, masked_card_number, card_status, fio, birth_date, citizenship, " \
              "registration_address, document_number, doc_type, pinfl, pos_code, pos_name) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (f"{FullDataP2P.iloc[i].time_id}", f"{FullDataP2P.iloc[i].customer_id}",
               f"{FullDataP2P.iloc[i].user_id}", f"{FullDataP2P.iloc[i].operation_type}",
               f"{FullDataP2P.iloc[i].amount}", f"{FullDataP2P.iloc[i].currency}", f"{FullDataP2P.iloc[i].country}",
               f"{FullDataP2P.iloc[i].masked_card_number}", f"{FullDataP2P.iloc[i].card_status}",
               f"{FullDataP2P.iloc[i].fio}", f"{FullDataP2P.iloc[i].birth_date}",
               f"{FullDataP2P.iloc[i].citizenship}", f"{FullDataP2P.iloc[i].registration_address}",
               f"{FullDataP2P.iloc[i].document_number}", f"{FullDataP2P.iloc[i].doc_type}",
               f"{FullDataP2P.iloc[i].pinfl}", f"{FullDataP2P.iloc[i].pos_code}",
               f"{FullDataP2P.iloc[i].pos_name}")
        my_cursor.execute(sql, val)
        mydb.commit()

    my_cursor.close()

    end_p2p_to_db_func = datetime.datetime.now()
    print(f'p2p_to_db_func ended in {end_p2p_to_db_func - start_p2p_to_db_func}')


def trans_gran_to_tt_func(my_cursor, my_db, start, table):
    start_trans_gran_to_tt_func = datetime.datetime.now()

    my_cursor.execute("SELECT pos_code, COUNT(*) count FROM "
                      "(SELECT DISTINCT pos_code, time_id FROM Initial_Data_P2P) "
                      f"WHERE created_date BETWEEN '{start}' AND '{var.today}') "
                      "X GROUP BY pos_code ORDER BY count DESC;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO trans_gran_to_tt_{table} (pos_code, count) VALUES (%s, %s)"
        val = (f"{row[0]}", f"{row[1]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_trans_gran_tt_func = datetime.datetime.now()
    print(f'trans_gran_to_tt_func ended in {end_trans_gran_tt_func - start_trans_gran_to_tt_func}')


def pinfl_receiver_func(path, flag):
    start_pinfl_receiver_func = datetime.datetime.now()

    pinfl_receiver = pd.DataFrame({'pinfl': [], 'count': [], 'amount': []})

    counter_i = 0
    for i in range(len(FullDataP2P)):
        pinfl = str(FullDataP2P.iloc[i].pinfl)
        flag_k = True
        for k in range(len(pinfl_receiver)):
            if pinfl == str(pinfl_receiver.iloc[k].pinfl):
                flag_k = False
                break

        if flag_k:
            counter_i += 1
            counter_j = 0
            sum = 0
            for j in range(len(FullDataP2P)):
                if pinfl == str(FullDataP2P.iloc[j].pinfl):
                    counter_j += 1
                    sum += FullDataP2P.iloc[j].amount

            string_of_data = {'pinfl': pinfl, 'count': counter_j, 'amount': round(float(sum), 2)}
            frame_of_data = pd.DataFrame(string_of_data, index=[counter_i], columns=['pinfl', 'count', 'amount'])
            pinfl_receiver = pd.concat([pinfl_receiver, frame_of_data])

    if os.path.exists(path):
        current_pinfl_receiver = pd.read_csv(f'{path}', sep=',')
    else:
        current_pinfl_receiver = pd.DataFrame({'pinfl': [], 'count': [], 'amount': []})

    for i in range(len(pinfl_receiver)):
        flag_j = True
        counter = 0
        for j in range(len(current_pinfl_receiver)):
            counter += 1
            if pinfl_receiver.iloc[i].pinfl == current_pinfl_receiver.iloc[j].pinfl:
                current_pinfl_receiver.iloc[j].count += pinfl_receiver.iloc[i].count
                current_pinfl_receiver.iloc[j].amount += pinfl_receiver.iloc[i].amount
                flag_j = False

        if flag_j:
            string_of_data = {'pinfl': pinfl_receiver.iloc[i].pinfl, 'count': pinfl_receiver.iloc[i].count,
                              'amount': pinfl_receiver.iloc[i].amount}
            frame_of_data = pd.DataFrame(string_of_data, index=[counter + 1], columns=['pinfl', 'count', 'amount'])
            current_pinfl_receiver = pd.concat([current_pinfl_receiver, frame_of_data])

    current_pinfl_receiver.to_csv(path, index=False, sep=',')

    if current_week_day == 'Monday' and flag:
        filenames_to_send.append(path)
        filenames_to_delete.append(path)
    elif current_day == '1' and not flag:
        filenames_to_send.append(path)
        filenames_to_delete.append(path)

    end_pinfl_receiver_func = datetime.datetime.now()
    print(f'pinfl_receiver_func ended in {end_pinfl_receiver_func - start_pinfl_receiver_func}')


def country_p2p_func(path, flag):
    start_country_p2p_func = datetime.datetime.now()

    country_p2p = pd.DataFrame({'country': [], 'count': [], 'amount': []})
    counter_i = 0

    for i in range(len(FullDataP2P)):
        country = str(FullDataP2P.iloc[i].country)
        flag_k = True
        for k in range(len(country_p2p)):
            if country == str(country_p2p.iloc[k].country):
                flag_k = False
                break

        if flag_k:
            counter_i += 1
            counter_j = 0
            sum = 0
            for j in range(len(FullDataP2P)):
                if country == str(FullDataP2P.iloc[j].country):
                    counter_j += 1
                    sum += FullDataP2P.iloc[j].amount

            string_of_data = {'country': country, 'count': counter_j, 'amount': round(float(sum), 2)}
            frame_of_data = pd.DataFrame(string_of_data, index=[counter_i], columns=['country', 'count', 'amount'])
            country_p2p = pd.concat([country_p2p, frame_of_data])

    if os.path.exists(path):
        current_country_p2p = pd.read_csv(f'{path}', sep=',')
    else:
        current_country_p2p = pd.DataFrame({'country': [], 'count': [], 'amount': []})

    for i in range(len(country_p2p)):
        flag_j = True
        counter = 0
        for j in range(len(current_country_p2p)):
            counter += 1
            if country_p2p.iloc[i].country == current_country_p2p.iloc[j].country:
                current_country_p2p.iloc[j].count += country_p2p.iloc[i].count
                current_country_p2p.iloc[j].amount += country_p2p.iloc[i].amount
                flag_j = False

        if flag_j:
            string_of_data = {'country': country_p2p.iloc[i].country, 'count': country_p2p.iloc[i].count,
                              'amount': country_p2p.iloc[i].amount}
            frame_of_data = pd.DataFrame(string_of_data, index=[counter + 1], columns=['country', 'count', 'amount'])
            current_country_p2p = pd.concat([current_country_p2p, frame_of_data])

    current_country_p2p.to_csv(path, index=False, sep=',')

    if current_week_day == 'Monday' and flag:
        filenames_to_send.append(path)
        filenames_to_delete.append(path)
    elif current_day == '1' and not flag:
        filenames_to_send.append(path)
        filenames_to_delete.append(path)

    end_country_p2p_func = datetime.datetime.now()
    print(f'country_p2p_func ended in {end_country_p2p_func - start_country_p2p_func}')


def number_receiver_octo_func(path, flag):
    start_number_receiver_octo_func = datetime.datetime.now()

    number_receiver_octo = pd.DataFrame({'dest_tool_id': [], 'count': [], 'amount': []})
    counter_i = 0
    for i in range(len(FullDataOCTO)):
        dest_tool_id = str(FullDataOCTO.iloc[i].dest_tool_id)
        flag_k = True
        for k in range(len(number_receiver_octo)):
            if dest_tool_id == str(number_receiver_octo.iloc[k].dest_tool_id):
                flag_k = False
                break

        if flag_k:
            counter_i += 1
            counter_j = 0
            sum = 0
            for j in range(len(FullDataOCTO)):
                if dest_tool_id == str(FullDataOCTO.iloc[j].dest_tool_id):
                    counter_j += 1
                    sum += FullDataOCTO.iloc[j].amount

            string_of_data = {'dest_tool_id': dest_tool_id, 'count': counter_j, 'amount': round(float(sum), 2)}
            frame_of_data = pd.DataFrame(string_of_data, index=[counter_i], columns=['dest_tool_id', 'count', 'amount'])
            number_receiver_octo = pd.concat([number_receiver_octo, frame_of_data])

    if os.path.exists(path):
        current_number_receiver_octo = pd.read_csv(f'{path}', sep=',')
    else:
        current_number_receiver_octo = pd.DataFrame({'dest_tool_id': [], 'count': [], 'amount': []})

    for i in range(len(number_receiver_octo)):
        flag_j = True
        counter = 0
        for j in range(len(current_number_receiver_octo)):
            counter += 1
            if number_receiver_octo.iloc[i].dest_tool_id == current_number_receiver_octo.iloc[j].dest_tool_id:
                current_number_receiver_octo.iloc[j].count += number_receiver_octo.iloc[i].count
                current_number_receiver_octo.iloc[j].amount += number_receiver_octo.iloc[i].amount
                flag_j = False

        if flag_j:
            string_of_data = {'dest_tool_id': number_receiver_octo.iloc[i].dest_tool_id,
                              'count': number_receiver_octo.iloc[i].count,
                              'amount': number_receiver_octo.iloc[i].amount}
            frame_of_data = pd.DataFrame(string_of_data, index=[counter + 1], columns=['dest_tool_id',
                                                                                       'count',
                                                                                       'amount'])
            current_number_receiver_octo = pd.concat([current_number_receiver_octo, frame_of_data])

    current_number_receiver_octo.to_csv(path, index=False, sep=',')

    if current_week_day == 'Monday' and flag:
        filenames_to_send.append(path)
        filenames_to_delete.append(path)
    elif current_day == '1' and not flag:
        filenames_to_send.append(path)
        filenames_to_delete.append(path)

    end_number_receiver_octo_func = datetime.datetime.now()
    print(f'number_receiver_octo_func ended in {end_number_receiver_octo_func - start_number_receiver_octo_func}')


def card_sender_octo_func(my_cursor, my_db, start, table):
    start_card_sender_octo_func = datetime.datetime.now()

    my_cursor.execute("SELECT masked_card_number, COUNT(*) count, SUM(amount) amount FROM "
                      "(SELECT DISTINCT masked_card_number, amount FROM Initial_Data_OCTO "
                      f"WHERE created_date BETWEEN '{start}' AND '{var.today}') "
                      "X GROUP BY masked_card_number ORDER BY count DESC;")
    data = my_cursor.fetchall()

    for row in data:
        sql = f"INSERT INTO card_sender_octo_{table} (masked_card_number, count, amount) VALUES (%s, %s, %s)"
        val = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
        my_cursor.execute(sql, val)
        my_db.commit()

    end_card_sender_octo_func = datetime.datetime.now()
    print(f'card_sender_octo_func ended in {end_card_sender_octo_func - start_card_sender_octo_func}')


def mrot_func(path):
    start_mrot_func = datetime.datetime.now()

    card_sender_octo = pd.read_csv(path, sep=',')
    result_card_sender_octo = pd.DataFrame({'masked_card_number': [], 'count': [],
                                            'amount': [], 'block': [], 'observation': []})
    mrot = 920000
    mrot_150 = mrot * 150

    for i in range(len(card_sender_octo)):
        if card_sender_octo.iloc[i].amount >= mrot_150:
            string_of_data = {'masked_card_number': card_sender_octo.iloc[i].masked_card_number,
                              'count': card_sender_octo.iloc[i].count,
                              'amount': card_sender_octo.iloc[i].amount,
                              'block': '*',
                              'observation': ''}
            frame_of_data = pd.DataFrame(string_of_data, index=[i + 1], columns=['masked_card_number', 'count',
                                                                                 'amount', 'block', 'observation'])
            result_card_sender_octo = pd.concat([result_card_sender_octo, frame_of_data])
        elif card_sender_octo.iloc[i].amount >= mrot_150 * 0.9:
            string_of_data = {'masked_card_number': card_sender_octo.iloc[i].masked_card_number,
                              'count': card_sender_octo.iloc[i].count,
                              'amount': card_sender_octo.iloc[i].amount,
                              'block': '',
                              'observation': '*'}
            frame_of_data = pd.DataFrame(string_of_data, index=[i + 1], columns=['masked_card_number', 'count',
                                                                                 'amount', 'block', 'observation'])
            result_card_sender_octo = pd.concat([result_card_sender_octo, frame_of_data])
        else:
            string_of_data = {'masked_card_number': card_sender_octo.iloc[i].masked_card_number,
                              'count': card_sender_octo.iloc[i].count,
                              'amount': card_sender_octo.iloc[i].amount,
                              'block': '',
                              'observation': ''}
            frame_of_data = pd.DataFrame(string_of_data, index=[i + 1], columns=['masked_card_number', 'count',
                                                                                 'amount', 'block', 'observation'])
            result_card_sender_octo = pd.concat([result_card_sender_octo, frame_of_data])

    result_card_sender_octo.to_csv(path, index=False, sep=',')

    end_mrot_func = datetime.datetime.now()
    print(f'card_sender_octo_func ended in {end_mrot_func - start_mrot_func}')


try:
    start_program = datetime.datetime.now()
    print(f'Program started at: {start_program} \n')

    # FullDataOCTO = pd.read_csv('OCTO 01-1708.csv', sep=',')
    # FullDataP2P = pd.read_csv('P2P 08-14.csv', sep=',')

    cursor, db = db_connection_func()

    # octo_to_db_func(cursor, db)
    # p2p_to_db_func(cursor, db)

    if var.current_week_day == 'Monday':
        trans_gran_to_tt_func(cursor, db, var.week_ago, 'week')
        card_sender_octo_func(cursor, db, var.week_ago, 'week')
    if var.current_day == '01':
        trans_gran_to_tt_func(cursor, db, f"{var.previous_month}-01", 'month')
        card_sender_octo_func(cursor, db, f"{var.previous_month}-01", 'month')

    end_program = datetime.datetime.now()
    print(f'\nProgram ended in {end_program - start_program}')
    print(end_program)
except KeyboardInterrupt:
    print("\n Program finished by user !!!!")

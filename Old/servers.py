from flask import Flask, request, jsonify
import re
import mysql.connector
import datetime
import bcrypt
import logging
app = Flask(__name__)

# Replace with your database configuration
mydb = mysql.connector.connect(
    host="ideal-web.site",
    user="admin_alexunderlag",
    password="OG+J(0@T{E[uakY@",
    database="admin_python"
)

@app.route('/register', methods=['POST'])
def register():
    mydb.reconnect()
    data = request.json
    logins = data.get('logins')
    email = data.get('email')
    password = data.get('password')
    password_dub = data.get('password_dub')
    fname = data.get('fname')
    lname = data.get('lname')
    city = data.get('city')
    mobile = data.get('mobile')

    # Email validation
    if not is_valid_email(email):
        return jsonify({'status': 'error', 'message': 'Некоректный Email'}), 400

    # Password match validation
    if password != password_dub:
        return jsonify({'status': 'error', 'message': 'Пароли не совпадают'}), 400

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM user WHERE logins = %s", (logins,))
    myresult = mycursor.fetchone()

    if myresult is None:
        # Хэширование пароля
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        mycursor.execute(
            "INSERT INTO user(logins, password, fname, lname, city, mobile, balance, email) VALUES (%s, %s, %s, %s, %s, %s, 0, %s)",
            (logins, hashed_password, fname, lname, city, mobile, email)
        )
        mydb.commit()
        return jsonify({'status': 'success', 'message': 'Регистрация успешна'})
    else:
        return jsonify({'status': 'error', 'message': 'Пользователь уже существует'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM user WHERE logins = %s", (username,))
    myresult = mycursor.fetchone()

    if myresult is None:
        return jsonify({'status': 'error', 'message': 'Неверное имя пользователя или пароль'}), 400
    else:
        # Проверка хэшированного пароля
        if bcrypt.checkpw(password.encode('utf-8'), myresult['password'].encode('utf-8')):
            return jsonify({'status': 'success', 'message': 'Авторизация успешна', 'user': myresult})
        else:
            return jsonify({'status': 'error', 'message': 'Неверное имя пользователя или пароль'}), 400
    
def is_valid_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(email_regex, email) is not None

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    username = data.get('username')
    balances = int(data.get('amount'))
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)
    
    # Проверяем баланс пользователя
    mycursor.execute("SELECT * FROM user where logins = %s", (username,))
    user = mycursor.fetchone()

    mycursor.execute("SELECT * FROM piramid WHERE id = 1")
    piramid = mycursor.fetchone()
    min = int(piramid['minshag'] )
    stav = int(piramid['balance'] )
    minstavka = min + stav
    lastuser  = piramid['lastuser']
    balance2 =  balances / 2

    if user:
        user_balance = int(user['balance'])
        
        if balances > user_balance:
            return jsonify({'status': 'error', 'message': 'У Вас меньше денег, чем вы хотите положить'})
        elif minstavka > balances:
            return jsonify({'status': 'error', 'message': 'Вы хотите положить меньше, минимальной ставки'})
        else:
            # Обновление баланса в БД
            mycursor.execute("UPDATE user SET balance = balance - %s WHERE logins = %s", ( balances , username))
            mycursor.execute("UPDATE piramid SET balance = balance + %s, participants = participants + 1 WHERE id = 1", (balances,))
            current_balance = int(piramid['balance'])
            mycursor.execute("UPDATE user SET balance = balance + %s + %s WHERE logins = %s;", (current_balance, balance2, lastuser))
            mycursor.execute("UPDATE piramid SET lastuser = %s WHERE id = %s;", (username, 1))
            mydb.commit()
            update_pyramid()
            return jsonify({'status': 'success', 'message': 'Пополнение успешно'})
    else:
        return jsonify({'status': 'error', 'message': 'Пользователь не найден'})

@app.route('/deposit2', methods=['POST'])
def deposit2():
    data = request.json
    username = data.get('username')
    balances = int(data.get('amount'))
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)
    
    # Проверяем баланс пользователя
    mycursor.execute("SELECT * FROM user where logins = %s", (username,))
    user = mycursor.fetchone()

    mycursor.execute("SELECT * FROM piramid WHERE id = 2")
    piramid = mycursor.fetchone()
    min = int(piramid['minshag'] )
    stav = int(piramid['balance'] )
    minstavka = min + stav
    lastuser  = piramid['lastuser']
    balance2 =  balances / 2

    if user:
        user_balance = int(user['balance'])
        
        if balances > user_balance:
            return jsonify({'status': 'error', 'message': 'У Вас меньше денег, чем вы хотите положить'})
        elif minstavka > balances:
            return jsonify({'status': 'error', 'message': 'Вы хотите положить меньше, минимальной ставки'})
        else:
            # Обновление баланса в БД
            mycursor.execute("UPDATE user SET balance = balance - %s WHERE logins = %s", ( balances , username))
            mycursor.execute("UPDATE piramid SET balance = balance + %s, participants = participants + 1 WHERE id = 2", (balances,))
            current_balance = int(piramid['balance'])
            mycursor.execute("UPDATE user SET balance = balance + %s + %s WHERE logins = %s;", (current_balance, balance2, lastuser))
            mycursor.execute("UPDATE piramid SET lastuser = %s WHERE id = %s;", (username, 1))
            mydb.commit()
            update_pyramid()
            return jsonify({'status': 'success', 'message': 'Пополнение успешно'})
    else:
        return jsonify({'status': 'error', 'message': 'Пользователь не найден'})


def update_pyramid():
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM piramid WHERE id = 1")
    piramid = mycursor.fetchone()
    start_date = piramid['start_date']
    end_date = piramid['end_date']

    # Проверка, прошел ли день с момента последнего пополнения пирамиды
    current_date = datetime.datetime.now().date()
    if current_date >= end_date:
        # Сдвиг даты на следующий день и аннулирование баланса
        new_end_date = end_date + datetime.timedelta(days=1)
        # Обновление записи пирамиды в базе данных
        mycursor.execute("UPDATE piramid SET end_date = %s WHERE id = 1",(new_end_date,))
        mydb.commit()

@app.route('/logout', methods=['POST'])
def logout():
    # Ваш код для выполнения операций выхода из системы
    # Например, удаление данных аутентификации, сброс сеанса и т.д.
    
    return jsonify({'message': 'Выход выполнен успешно'})


@app.route('/get_user_info', methods=['POST'])
def get_user_info():
    data = request.json
    username = data.get('username')
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)
    # Запрос в БД
    mycursor.execute("SELECT * FROM user WHERE logins = %s;", (username,))
    user = mycursor.fetchone()

    if user is None:
        return jsonify({'message': 'Пользователь не найден'}), 404
    else:
        return jsonify(user)

@app.route('/get_piramid_data', methods=['GET'])
def get_piramid_data():
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)
    # Получение данных для пирамиды с ID 1
    mycursor.execute("SELECT * FROM piramid WHERE id = 1;")
    piramid_data1 = mycursor.fetchone()

    # Получение данных для пирамиды с ID 2
    mycursor.execute("SELECT * FROM piramid WHERE id = 2;")

    piramid_data2 = mycursor.fetchone()
    # Возврат данных для обеих пирамид в одном ответе
    return jsonify(piramid_data1=piramid_data1, piramid_data2=piramid_data2)

@app.route('/menu_sht', methods=['GET'])

def update_sht():
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)
    
    mycursor.execute("SELECT MAX(ID) FROM user;")
    max_user_id = mycursor.fetchone().get("MAX(ID)", 0)
    
    mycursor.execute("SELECT MAX(ID) FROM piramid;")
    max_piramid_id = mycursor.fetchone().get("MAX(ID)", 0)
    today = datetime.datetime.now()
    bday = datetime.datetime(2023,7,4,11,59)
    time_diff = bday - today
    tdays = time_diff.days
    return jsonify({"max_user_id": max_user_id, "max_piramid_id": max_piramid_id, "tdays": tdays},)
@app.route('/update_balance', methods=['POST'])
def update_balance():
    try:
        data = request.json
        username = data.get('username')
        balance = data.get('balance')
        mydb.reconnect()
        mycursor = mydb.cursor(dictionary=True)

        # Обновление баланса в БД
        mycursor.execute("UPDATE user SET balance = balance + %s WHERE logins = %s;", (balance, username))
        mydb.commit()

        # Получение обновленного баланса из БД
        mycursor.execute("SELECT balance FROM user WHERE logins = %s;", (username,))
        updated_balance = mycursor.fetchone()

        # Проверяем, что updated_balance не равно None, перед тем как использовать его
        if updated_balance is not None:
            return jsonify({'message': 'Баланс успешно пополнен', 'new_balance': updated_balance['balance']})
        else:
            return jsonify({'message': 'Ошибка: Не удалось получить обновленный баланс'}), 500
    except Exception as e:
        logging.exception("Произошла ошибка при пополнении баланса")
        return jsonify({'message': 'Ошибка при пополнении баланса: ' + str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True, host='77.73.68.140')
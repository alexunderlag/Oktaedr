from flask import Flask, request, jsonify, make_response
import re
import mysql.connector
import bcrypt
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import os
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from urllib.parse import quote_plus

app = Flask(__name__)


username = 'admin_alexunderlags'
password = ''
host = 'ideal-web.site'
database = 'admin_admin_python_news'

encoded_password = quote_plus(password)
connection_string = f"mysql+pymysql://{username}:{encoded_password}@{host}/{database}"

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

# Replace with your database configuration
mydb = mysql.connector.connect(
    host="ideal-web.site",
    user="admin_alexunderlag",
    password="",
    database="admin_python"
)

app.config['SECRET_KEY'] = 'fdasfsdafsafdsfarvewr4324f3143143v43awv4w3averwarv'

db = SQLAlchemy(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['user_id']).first()
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:  # Это исключение будет ловить большинство ошибок, связанных с токеном
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(current_user, *args, **kwargs)
    
    return decorated

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user registered!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return make_response('Bad login details', 401)

    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
    return jsonify({'token': token})

@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({'message': f'Welcome {current_user.username}!'})


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
    follow = mycursor.fetchone()
    mycursor.execute("SELECT MAX(ID) FROM piramid;")
    piramidkol = mycursor.fetchone()
    
    start_date = datetime(2023, 7, 1)  # Замените эту дату на вашу начальную дату
    today = datetime.now()
    days_passed = (today - start_date).days
    
    return jsonify(max_user_id=follow["MAX(ID)"], max_piramid_id=piramidkol["MAX(ID)"], tdays=days_passed)

@app.route('/advertup', methods=['GET'])
def update_newstoday():
    # mydb.reconnect()
    # mycursor = mydb.cursor(dictionary=True)
    # mycursor.execute("SELECT MAX(ID) FROM user;")
    # follow = mycursor.fetchone()
    
    newstoday = 'Добро пожаловать на закрытое бето тестирование. Спасибо что Вы с намии)))'  # Замените эту дату на вашу начальную дату
    return jsonify({"newstoday": newstoday})

if __name__ == '__main__':
    app.run(debug=True, host='77.73.68.140')
from tkinter import *
from tkinter import ttk
import re
import tkinter
import tkinter.messagebox
import customtkinter
import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter.messagebox as mymessagebox
import tkinter as tk
import tkinter.messagebox as mb
import random
import tkinter.ttk
import requests
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox

def validate(u_input): # callback function
    return u_input.isdigit()

class Balanceup(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = customtkinter.CTkFrame(self, corner_radius=0)
        self.title("Пополнение баланса")
        self.my_valid = self.window.register(validate) 
        self.label = customtkinter.CTkLabel(self, text="Введите цельную сумму в рублях")
        self.label.grid(row=0, column=1,padx=10,pady=(10, 10), columnspan=2)
        self.reg_user = customtkinter.CTkEntry(self, placeholder_text="Сумма",validate = 'key', validatecommand = (self.my_valid,'%S'))
        self.reg_user.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.btn_balance =  customtkinter.CTkButton(self, text='Пополнить', command=self.clicked)
        self.btn_balance.grid(row=2, column=1, padx=20, pady=(10, 10))

    def clicked(self):
        balance = self.reg_user.get()
        if balance == '' or balance == "0":
            CTkMessagebox(title="Ошибка", message="Введите цельную сумму в рублях", icon="cancel")
        else:
            # Отправка запроса на сервер
            response = requests.post("http://ideal-web.site:5000/update_balance", json={"username": nikname, "balance": balance})

            # Обработка ответа
            if response.status_code == 200:
                obnovleniedepost()
                messagebox.showinfo("Успешно", response.json()["message"])
                # obnovleniedepost()  # функция обновления данных на интерфейсе
                self.close()  # Закрыть окно пополнения баланса
            else:
                CTkMessagebox(title="Ошибка", message="Произошла ошибка при пополнении баланса", icon="cancel")
    def close(self):
        self.destroy()

def login():
    global user_info, nikname, balance
    username = user_entry.get()
    password = user_pass.get()

    # Отправка запроса на сервер
    response = requests.post("http://ideal-web.site:5000/login", json={
        "username": username,
        "password": password
    })

    # Обработка ответа
    data = response.json()
    if response.status_code == 400:
        CTkMessagebox(title="Ошибка", message=data['message'], icon="cancel")
    else:
        user_info = data['user']
        balance = user_info["balance"]
        nikname = user_info["logins"]
        lname = user_info["lname"]
        fname = user_info["fname"]
        city = user_info["city"]
        mobile = user_info["mobile"]
        email = user_info["email"]
        logo_Text.configure(text=f"Никнейм: {nikname}")
        logo_Text1.configure(text=f"{fname} {lname}")
        logo_Text3.configure(text=f"Город: {city }")
        logo_Text4.configure(text=f"Номер: {mobile}")
        profil_email.configure(text=f"Email: {email}")      
        logo_Text5.configure(text=f"Баланс: {balance}р.")
 
        CTkMessagebox(title="Успешно", message="Успешная авторизация")
        frame_2_button_event()
        button.configure(state=ctk.NORMAL)
        button2.configure(state=ctk.NORMAL)   

class Deposit(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.depositwindows = customtkinter.CTkFrame(self, corner_radius=0)
        self.title("Депозит")
        self.my_valid = self.depositwindows.register(validate) 
        self.label = customtkinter.CTkLabel(self, text="Введите цельную сумму в рублях")
        self.label.grid(row=0, column=1,padx=10,pady=(10, 10), columnspan=2)
        self.reg_user = customtkinter.CTkEntry(self, placeholder_text="Сумма",validate = 'key', validatecommand = (self.my_valid,'%S'))
        self.reg_user.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.btn_balance =  customtkinter.CTkButton(self, text='Пополнить', command=self.depositus)
        self.btn_balance.grid(row=2, column=1, padx=20, pady=(10, 10))
    def depositus(self):
        amount = int(self.reg_user.get())

        # Отправка запроса на сервер
        response = requests.post("http://ideal-web.site:5000/deposit", json={
            "username": nikname,
            "amount": amount
        })

        # Обработка ответа
        data = response.json()
        if data['status'] == 'success':
            obnpir()
            obnpir2()
            obnovleniedepost()
            mymessagebox.showinfo("Успешно", "Вы успешно зарегестрировались")
            self.close()  # Закрыть окно пополнения баланса
        else:
            CTkMessagebox(title="Ошибка", message=data['message'], icon="cancel")
    def close(self):
        self.destroy()

class Deposit2(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.depositwindows = customtkinter.CTkFrame(self, corner_radius=0)
        self.title("Депозит")
        self.my_valid = self.depositwindows.register(validate) 
        self.label = customtkinter.CTkLabel(self, text="Введите цельную сумму в рублях")
        self.label.grid(row=0, column=1,padx=10,pady=(10, 10), columnspan=2)
        self.reg_user = customtkinter.CTkEntry(self, placeholder_text="Сумма",validate = 'key', validatecommand = (self.my_valid,'%S'))
        self.reg_user.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.btn_balance =  customtkinter.CTkButton(self, text='Пополнить', command=self.depositus)
        self.btn_balance.grid(row=2, column=1, padx=20, pady=(10, 10))
    def depositus(self):
        amount = int(self.reg_user.get())

        # Отправка запроса на сервер
        response = requests.post("http://ideal-web.site:5000/deposit2", json={
            "username": nikname,
            "amount": amount
        })

        # Обработка ответа
        data = response.json()
        if data['status'] == 'success':
            obnpir()
            obnpir2()
            obnovleniedepost()
            mymessagebox.showinfo("Успешно", "Вы успешно зарегестрировались")
            self.close()  # Закрыть окно пополнения баланса
        else:
            CTkMessagebox(title="Ошибка", message=data['message'], icon="cancel")
    def close(self):
        self.destroy()

class registration(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("380x300")
        self.title("Окно регистрации")

        self.label = customtkinter.CTkLabel(self, text="Введите данные")
        self.label.grid(row=0, column=1,pady=(10, 10), columnspan=2)
        self.reg_user = customtkinter.CTkEntry(self, placeholder_text="Логин")
        self.reg_user.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.reg_pass = customtkinter.CTkEntry(self, placeholder_text="Пароль",show="*")
        self.reg_pass.grid(row=2, column=1, padx=20, pady=(10, 10))
        self.reg_passdub = customtkinter.CTkEntry(self, placeholder_text="Повтор пароля",show="*")
        self.reg_passdub.grid(row=3, column=1, padx=20, pady=(10, 10))
        self.reg_email = customtkinter.CTkEntry(self, placeholder_text="Email")
        self.reg_email.grid(row=4, column=1, padx=20, pady=(10, 10))
        self.reg_fname = customtkinter.CTkEntry(self, placeholder_text="Имя")
        self.reg_fname.grid(row=1, column=2, padx=20, pady=(10, 10))
        self.reg_lname = customtkinter.CTkEntry(self, placeholder_text="Фамилия")
        self.reg_lname.grid(row=2, column=2, padx=20, pady=(10, 10))
        self.reg_city = customtkinter.CTkEntry(self, placeholder_text="Город")
        self.reg_city.grid(row=3, column=2, padx=20, pady=(10, 10))
        self.reg_mobile = customtkinter.CTkEntry(self, placeholder_text="Телефон")
        self.reg_mobile.grid(row=4, column=2, padx=20, pady=(10, 10))

        self.reg_btn =  customtkinter.CTkButton(self, text='Зарегистрировать', command=self.register)
        self.reg_btn.grid(row=10, column=2,pady=(10, 10))
    def register(self):
        # ... gather data from input fields ...

        # Sending a request to the Flask API server
        response = requests.post("http://ideal-web.site:5000/register", json={
            "logins":self.reg_user.get(),
            "email": self.reg_email.get(),
            "password": self.reg_pass.get(),
            "password_dub": self.reg_passdub.get(),
            "fname": self.reg_fname.get(),
            "lname": self.reg_lname.get(),
            "city": self.reg_city.get(),
            "mobile": self.reg_mobile.get()
        })

        # Handling the response
        data = response.json()
        if response.status_code == 400:
            messagebox.showerror("", data['message'])
        else:
            messagebox.showinfo("Регистрация успешно завершена", data['message'])
            self.close()
    def close(self):
        self.destroy()

def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)	

def obnovleniedepost():
    # Отправка запроса на сервер
    response = requests.post("http://ideal-web.site:5000/get_user_info", json={"username": nikname})

    # Обработка ответа
    if response.status_code == 404:
        messagebox.showerror("Ошибка", response.json()["message"])
    else:
        user_info = response.json()
        balance = user_info["balance"]
        
        # Обновление информации на интерфейсе
        logo_Text.configure(text=f"Никнейм: {user_info['logins']}")
        logo_Text1.configure(text=f"{user_info['fname']} {user_info['lname']}")
        logo_Text3.configure(text=f"Город: {user_info['city']}")
        logo_Text4.configure(text=f"Номер: {user_info['mobile']}")
        logo_Text5.configure(text=f"Баланс: {balance}р.")
    
def obnpir():
    # Выполнить GET запрос к серверу Flask для получения данных о пирамиде
    response = requests.get('http://ideal-web.site:5000/get_piramid_data')
    # Проверить, что запрос успешен
    if response.status_code == 200:
        # Преобразовать ответ JSON в Python словарь
        piramid_data = response.json()
        # Обновить GUI с данными из ответа
        minstavka = piramid_data['balance'] + piramid_data['minshag']
        logo_Textp1.configure(text=f"{piramid_data['name']}")
        logo_Textp2.configure(text=f"Баланс: {piramid_data['balance']}")
        logo_Textp3.configure(text=f"Участников: {piramid_data['participants']}")
        logo_Textp4.configure(text=f"Последний: {piramid_data['lastuser']}")
        logo_Textp5.configure(text=f"Минимальный шаг: {piramid_data['minshag']} + {piramid_data['balance'] } ({minstavka})")
        logo_Textp6.configure(text=f"Дата начала: {piramid_data['start_date']}")
        logo_Textp7.configure(text=f"Дата конца: {piramid_data['end_date']}")
    else:
        # Вывести сообщение об ошибке если запрос неуспешен
        print("Ошибка при получении данных о пирамиде")

def obnpir2():
    # Выполнить GET запрос к серверу Flask для получения данных о пирамиде
    response = requests.get('http://ideal-web.site:5000/get_piramid_data2')
    # Проверить, что запрос успешен
    if response.status_code == 200:
        # Преобразовать ответ JSON в Python словарь
        piramid_data2 = response.json()
        # Обновить GUI с данными из ответа
        minstavka = piramid_data2['balance'] + piramid_data2['minshag']
        logo_Textp11.configure(text=f"{piramid_data2['name']}")
        logo_Textp21.configure(text=f"Баланс: {piramid_data2['balance']}")
        logo_Textp31.configure(text=f"Участников: {piramid_data2['participants']}")
        logo_Textp41.configure(text=f"Последний: {piramid_data2['lastuser']}")
        logo_Textp51.configure(text=f"Минимальный шаг: {piramid_data2['minshag']} + {piramid_data2['balance'] } ({minstavka})")
        logo_Textp61.configure(text=f"Дата начала: {piramid_data2['start_date']}")
        logo_Textp71.configure(text=f"Дата конца: {piramid_data2['end_date']}")
    else:
        # Вывести сообщение об ошибке если запрос неуспешен
        print("Ошибка при получении данных о пирамиде")
       
def select_frame_by_name(name):
        if name == "home":
            frame.grid(row=0, column=0, rowspan=5, padx=0, pady=(0, 0))
        else:
            frame.grid_forget()
        if name == "frame_2":
            second_frame.grid(row=0, column=0, rowspan=5, padx=0, pady=(0, 0))
        else:
            second_frame.grid_forget()

def btn_exit_fun():
        select_frame_by_name("home")
        button.configure(state=tk.DISABLED)
        button2.configure(state=tk.DISABLED)
def frame_2_button_event():
        select_frame_by_name("frame_2")

root = customtkinter.CTk()
root.title("Октаэдр - заработай миллион")
root.geometry("800x512")

frame = customtkinter.CTkFrame(root, corner_radius=0)

second_frame = customtkinter.CTkFrame(root, corner_radius=0)

select_frame_by_name("home")

logo_label = customtkinter.CTkLabel(frame, text="Авторизация", font=customtkinter.CTkFont(size=20, weight="bold"), width=140)
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

user_entry = customtkinter.CTkEntry(frame, placeholder_text="Логин")
user_entry.grid(row=1, column=0, padx=20, pady=(20, 0))
user_pass = customtkinter.CTkEntry(frame, placeholder_text="Пароль",show="*")
user_pass.grid(row=2, column=0, padx=20, pady=(10, 10))

btn_register =  customtkinter.CTkButton(frame, text='Регистрация', command=registration)
btn_register.grid(row=3, column=0, pady=(0, 10))

cal_btn =  customtkinter.CTkButton(frame, text='Войти', command=login)
cal_btn.grid(row=4, column=0)

appearance_mode_label = customtkinter.CTkLabel(frame, text="Цветовая схема:")
appearance_mode_label.grid(row=7, column=0, padx=0, pady=(200,0))

appearance_mode_optionemenu = customtkinter.CTkOptionMenu(frame, values=["System", "Dark", "Light"], command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=8, column=0, padx=0, pady=(0, 50))


logo_label2 = customtkinter.CTkLabel(second_frame, text="Профиль", font=customtkinter.CTkFont(size=20, weight="bold"), width=140)
logo_label2.grid(row=0, column=0, padx=10, pady=(20, 10))

logo_Text1 = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text1.grid(row=1, column=0, padx=10, pady=(0, 10))

logo_Text = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

logo_Text3 = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text3.grid(row=3, column=0, padx=10, pady=(0, 10), sticky=W)

logo_Text4 = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text4.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="w")

logo_Text5 = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text5.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")
profil_email = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
profil_email.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="w")

cal_btn5 =  customtkinter.CTkButton(second_frame, text='Пополнить баланс', command=Balanceup)
cal_btn5.grid(row=7, column=0,pady=(10, 10))

btn_exit =  customtkinter.CTkButton(second_frame, text='Выйти', command=btn_exit_fun)
btn_exit.grid(row=8, column=0,pady=(120, 30),padx=20)

mainback = customtkinter.CTkFrame(root)
mainback.grid(row=0, column=2, padx=20, pady=(5, 0), sticky="n", )

mainbacks = customtkinter.CTkFrame(root)
mainbacks.grid(row=1, column=2, padx=20, pady=(10, 10), sticky="nw")


logo_Textp1 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=20, weight="bold"))
logo_Textp1.grid(row=0, column=1, padx=0, pady=(0, 0),columnspan=2)

logo_Textp2 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp2.grid(row=1, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp3 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp3.grid(row=2, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp4 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp4.grid(row=3, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp5 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp5.grid(row=4, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp6 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp6.grid(row=5, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp7 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp7.grid(row=6, column=1, padx=30, pady=(0, 0),sticky="w")


logo_Textp11 = customtkinter.CTkLabel(mainbacks, text='', font=customtkinter.CTkFont(size=20, weight="bold"))
logo_Textp11.grid(row=0, column=1, padx=0, pady=(0, 0),columnspan=2)

logo_Textp21 = customtkinter.CTkLabel(mainbacks, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp21.grid(row=1, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp31 = customtkinter.CTkLabel(mainbacks, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp31.grid(row=2, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp41 = customtkinter.CTkLabel(mainbacks, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp41.grid(row=3, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp51 = customtkinter.CTkLabel(mainbacks, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp51.grid(row=4, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp61 = customtkinter.CTkLabel(mainbacks, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp61.grid(row=5, column=1, padx=30, pady=(0, 0),sticky="w")

logo_Textp71 = customtkinter.CTkLabel(mainbacks, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
logo_Textp71.grid(row=6, column=1, padx=30, pady=(0, 0),sticky="w")

button2 = customtkinter.CTkButton(mainbacks, text="Депозит", command=Deposit2, state=tk.DISABLED)
button2.grid(row=7, column=1,pady=(10, 10),padx=10,sticky="e")

button = customtkinter.CTkButton(mainback, text="Депозит", command=Deposit, state=tk.DISABLED)
button.grid(row=7, column=1,pady=(10, 10),padx=10,sticky="e")

obnpir()
obnpir2()
root.mainloop()

    
# class Balanceup(customtkinter.CTkToplevel):
#     def __init__(self, *args, **kwargs, ):
#         super().__init__(*args, **kwargs)


#     def clicked(self):
#             balance = self.reg_user.get()
#             if balance=='' or balance == "0":
#                 mymessagebox.showerror("Ошибка", "Введите цельную сумму в рублях")
#             else:
#                 mydb.reconnect()
#                 mycursor = mydb.cursor(dictionary=True)
#                 # mycursor.execute("Create table if not exists user(id VARCHAR(30)  NOT NULL AUTO_INCREMENT, logins VARCHAR(30), password VARCHAR(30),fname VARCHAR(30),lname VARCHAR(30),city VARCHAR(20),mobile VARCHAR(15), balance INT, email VARCHAR(30))")
#                 mycursor.execute("UPDATE user set balance = balance + '"+ balance + "' where logins = '"+ smyresult[1] +"';")
#                 mycursor.execute("commit")
#                 obnovleniedepost()
#                 close(self)


# class deposit(customtkinter.CTkToplevel):
#     def __init__(self, *args, **kwargs, ):
#         super().__init__(*args, **kwargs)
#         self.depositwindows = customtkinter.CTkFrame(self, corner_radius=0)
#         self.title("Депозит")
#         self.my_valid = self.depositwindows.register(validate) 
#         self.label = customtkinter.CTkLabel(self, text="Введите цельную сумму в рублях")
#         self.label.grid(row=0, column=1,padx=10,pady=(10, 10), columnspan=2)
#         self.reg_user = customtkinter.CTkEntry(self, placeholder_text="Сумма",validate = 'key', validatecommand = (self.my_valid,'%S'))
#         self.reg_user.grid(row=1, column=1, padx=20, pady=(10, 10))
#         self.btn_balance =  customtkinter.CTkButton(self, text='Пополнить', command=self.depositus)
#         self.btn_balance.grid(row=2, column=1, padx=20, pady=(10, 10))


#     def depositus(self):
#         mydb.reconnect()
#         mycursor = mydb.cursor(dictionary=True)
#         balance = int(self.reg_user.get())
#         balance2 = balance / 2
#         mycursor.execute("SELECT * FROM user where logins = '"+ smyresult[1] +"';")
#         myresult = mycursor.fetchone()
#         self.userspis = list(myresult.values())
#         self.useronl = int(self.userspis[6])
#         userbalans = int(self.userspis[7])
#         mycursor.close
#         mydb.reconnect()
#         mycursor = mydb.cursor(dictionary=True)
#         mycursor.execute("SELECT * FROM piramid where id = 1;")
#         myresult = mycursor.fetchone()
#         self.piramidspi = list(myresult.values())
#         self.balanpirm = int(self.piramidspi[2])
#         self.userlastpir = self.piramidspi[6]
#         self.minstavka = int(self.piramidspi[7])
#         mycursor.close

#         if balance > userbalans:
#             mymessagebox.showerror("Ошибка", "У Вас меньше денег, чем выхотите полжоить")
#         elif self.minstavka > balance:
#             mymessagebox.showerror("Ошибка", "Вы хотите положить меньше, минимальной ставки")
#         else:
#             mydb.reconnect()
#             mycursor = mydb.cursor(dictionary=True)
#             mycursor.execute("UPDATE user SET balance = balance - %s WHERE logins = %s;", (balance, smyresult[1]))
#             mycursor.execute("UPDATE user SET balance = balance + %s WHERE logins = %s;", (balance2, self.userlastpir))
#             mycursor.execute("UPDATE piramid SET balance = balance + %s WHERE id = %s;", (balance, 1))
#             mycursor.execute("UPDATE piramid SET lastuser = %s WHERE id = %s;", (smyresult[1], 1))
#             mycursor.execute("commit")
#             obnovleniedepost()
#             obnpir()

# class registration(customtkinter.CTkToplevel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.geometry("400x500")
#         self.title("Окно регистрации")

#         self.label = customtkinter.CTkLabel(self, text="Введите данные")
#         self.label.grid(row=0, column=1,pady=(10, 10), columnspan=2)
#         self.reg_user = customtkinter.CTkEntry(self, placeholder_text="Логин")
#         self.reg_user.grid(row=1, column=1, padx=20, pady=(20, 10))
#         self.reg_pass = customtkinter.CTkEntry(self, placeholder_text="Пароль",show="*")
#         self.reg_pass.grid(row=2, column=1, padx=20, pady=(10, 10))
#         self.reg_passdub = customtkinter.CTkEntry(self, placeholder_text="Повтор пароля",show="*")
#         self.reg_passdub.grid(row=3, column=1, padx=20, pady=(10, 10))
#         self.reg_email = customtkinter.CTkEntry(self, placeholder_text="Email")
#         self.reg_email.grid(row=4, column=1, padx=20, pady=(10, 10))
#         self.reg_fname = customtkinter.CTkEntry(self, placeholder_text="Имя")
#         self.reg_fname.grid(row=5, column=1, padx=20, pady=(10, 10))
#         self.reg_city = customtkinter.CTkEntry(self, placeholder_text="Город")
#         self.reg_city.grid(row=6, column=1, padx=20, pady=(10, 10))
#         self.reg_lname = customtkinter.CTkEntry(self, placeholder_text="Фамилия")
#         self.reg_lname.grid(row=7, column=1, padx=20, pady=(10, 10))
#         self.reg_mobile = customtkinter.CTkEntry(self, placeholder_text="Телефон")
#         self.reg_mobile.grid(row=6, column=1, padx=20, pady=(10, 10))

#         self.reg_btn =  customtkinter.CTkButton(self, text='Зарегистрировать', command=self.register)
#         self.reg_btn.grid(row=9, column=2,pady=(10, 10))


#     def register(self):
#         mydb.reconnect()
#         mycursor = mydb.cursor(dictionary=True)
#         mycursor.execute("SELECT * FROM user where logins = '"+ self.reg_user.get() +"';")
#         myresult = mycursor.fetchone()

#         if not self.is_valid_email(self.reg_email.get()):
#             mymessagebox.showerror("Ошибка", "Неверный адрес электронной почты")
#         elif self.reg_pass.get() != self.reg_passdub.get():
#             mymessagebox.showerror("Ошибка", "Пароли не совпадают")
#         elif myresult==None:
#             mydb.reconnect()
#             mycursor = mydb.cursor(dictionary=True)
#             mycursor.execute("INSERT INTO user(logins,password,fname,lname,city,mobile,balance,email) VALUES ('%s','%s','%s','%s','%s','%s', 0,'%s')" % (self.reg_user.get(), self.reg_pass.get(), self.reg_fname.get(), self.reg_lname.get(),self.reg_city.get(), self.reg_mobile.get(),self.reg_email.get()))
#             mycursor.execute("commit")
#             mymessagebox.showinfo("Успешно", "Вы успешно зарегестрировались")
#             close(self)
#         else:
#             mymessagebox.showerror("Ошибка", "Такой пользователь уже существует")

#     def is_valid_email(self, email):
#         email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#         if re.fullmatch(email_regex, email):
#             return True
#         else:
#             return False

# def login():
#     # a1 = ToplevelWindow()
#     # a1.a
#     global smyresult
#     mydb.reconnect()
#     mycursor = mydb.cursor(dictionary=True)
#     # mycursor.execute("Create table if not exists user(id VARCHAR(30) NOT NULL, logins VARCHAR(30), password VARCHAR(30),fname VARCHAR(30),lname VARCHAR(30),city VARCHAR(20),mobile VARCHAR(15), balance INT, email VARCHAR(30))")
#     mycursor.execute("SELECT * FROM user where logins = '"+ user_entry.get() +"' and password = '"+ user_pass.get() +"';")
#     myresult = mycursor.fetchone()
    
#     if myresult==None:
#         mymessagebox.showerror("Ошибка", "Неверный пароль или имя пользователя")

#     else:
#         smyresult = list(myresult.values())
#         # id = smyresult[0]
#         balance = smyresult[7]
#         # bal = f"Баланс: {list(myresult.values())[7]}р."
#         frame_2_button_event()
#         logo_Text.configure(text=f"Никнейм: {smyresult[1]}")
#         logo_Text1.configure(text=f"{smyresult[3]} {smyresult[3]}")
#         logo_Text3.configure(text=f"Город: {smyresult[5]}")
#         logo_Text4.configure(text=f"Номер: {smyresult[6]}")
#         logo_Text5.configure(text=f"Баланс: {balance}р.")
#         profil_email.configure(text=f"Email: {smyresult[8]}")       
#         print(smyresult)
#         button.configure(state=ctk.NORMAL)
        
#         mymessagebox.showinfo("Успешно", "Успешная авторизация")

# def obnovleniedepost():
#     global smyresult
#     mydb.reconnect()
#     mycursor = mydb.cursor(dictionary=True)
#     mycursor.execute("SELECT * FROM user where logins = '"+ smyresult[1] +"';")
#     myresult = mycursor.fetchone()
#     smyresult = list(myresult.values())
#     balance = smyresult[7]
#     frame_2_button_event()
#     logo_Text.configure(text=f"Никнейм: {smyresult[1]}")
#     logo_Text1.configure(text=f"{smyresult[3]} {smyresult[3]}")
#     logo_Text3.configure(text=f"Город: {smyresult[5]}")
#     logo_Text4.configure(text=f"Номер: {smyresult[6]}")
#     logo_Text5.configure(text=f"Баланс: {balance}р.")

#     button.configure(state=tk.NORMAL)
#     mymessagebox.showinfo("Успешно", "Успешное пополнение")


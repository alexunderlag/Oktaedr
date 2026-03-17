 # -*- coding: utf8 -*-
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


SERVER_URL = "http://ideal-web.site:5000"

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Октаэдр - заработай миллион")
        self.geometry("1200x750")
        self.configure(fg_color="#24234a")
        self.frame = Frame(self, root_instance=self)
        self.frame.pack(side=LEFT, fill=Y)
        self.current_user_balance = 0  # Добавлено
        self.toptbar = Toptbar()
        self.toptbar.pack(side=TOP, fill=X)
        self.toptbar2 = Toptbar2()
        self.toptbar2.pack(side=TOP, fill=X)

        self.rightbar = Rightbar(topbar_instance=self.toptbar)
        self.rightbar.pack(side=RIGHT, fill=Y)

        self._frame = None
        self.switch_frame(Main_frame)

    def switch_frame(self, frame_class):
        new_frame = frame_class()
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(side="left", fill="both", expand=True,)

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, root_instance,**kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#2b2b47",border_width=0)
        self.logotype = customtkinter.CTkLabel(self, text="Октаэдр", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logotype.pack(side=TOP, anchor="nw", padx=50, pady=(20,0))
        Left_menu(self, root_instance)

class Left_menu(customtkinter.CTkFrame):
    def __init__(self, master, root_instance, **kw):
        super().__init__(master, **kw)
        self.root_instance = root_instance
        self.configure( corner_radius=0, fg_color="transparent",border_width=0)
        self.pack(side=TOP, pady=(50,0))
        # Создаем список с информацией о кнопках
        self.buttons_info = [
            {"text": "Главная", "command": lambda: self.root_instance.switch_frame(Title_frame)},
            {"text": "Правила", "command": lambda: self.root_instance.switch_frame(MainRules)},
            {"text": "Профиль", "command": lambda: self.root_instance.switch_frame(Main_frame1)},
            {"text": "Пирамиды", "command": lambda: self.root_instance.switch_frame(Main_frame)},
            {"text": "Лотерея", "command": "login"},
            {"text": "Контакты", "command": "login"},
            {"text": "О нас", "command": "login"},
        ]
        for button_info in self.buttons_info:
            self.button = customtkinter.CTkButton(
                self,
                text=button_info["text"],
                command=button_info["command"],
                font=customtkinter.CTkFont(size=13, weight="bold"),
                corner_radius=4,
                text_color="#bfbeda",
                fg_color="transparent",
                hover_color="#da3c2d",
            )
            self.button.pack(padx=20, pady=(5, 0), ipady=10, ipadx=20)

class Rightbar(customtkinter.CTkFrame):
    def __init__(self, master=None, topbar_instance=None, **kw):
        super().__init__(master, **kw)
        self.pack(side=RIGHT)
        self.configure(corner_radius=0, fg_color="#3e3e60", border_width=1, border_color="#1a1a31")
        self.second_frame_instance = Second_frame(self, rightbar_instance=self,)
        self.auth_frame_instance = Auth_frame(self, second_frame_instance=self.second_frame_instance, topbar_instance=topbar_instance)

class Auth_frame(customtkinter.CTkFrame):
    def __init__(self, master, second_frame_instance, topbar_instance, **kw):
        super().__init__(master, **kw)
        self.topbar_instance = topbar_instance
        self.pack(fill="both", expand=True, padx=5,pady=(5,5))
        self.login_manager = LoginManager(self, second_frame_instance, topbar_instance)
        self.configure(fg_color="#26264a", border_width=1, border_color="#505078")
        self.login_entry = customtkinter.CTkEntry(self, placeholder_text="Логин")
        self.login_entry.pack(padx=10, pady=(10, 0))
        self.pass_entry = customtkinter.CTkEntry(self, placeholder_text="Пароль", show="*")
        self.pass_entry.pack(padx=10, pady=(5, 5))
        self.login_btn = customtkinter.CTkButton(self, text='Войти', command=self.login)
        self.login_btn.pack(padx=10, pady=(5, 0))
        self.register_btn =  customtkinter.CTkButton(self, text='Регистрация', command=self.open_registration_window,)
        self.register_btn.pack(padx=10, pady=(10, 10))
        self.login_manager = LoginManager(self, second_frame_instance, topbar_instance)

    def open_registration_window(self):
        registration_window = Registration(master=self)
        registration_window.grab_set()

    def login(self):
        username = self.login_entry.get()
        password = self.pass_entry.get()
        if self.login_manager.login(username, password):
            self.master.rightbar_instance.logged_in_username = username

    def logout(self):
        self.master.logged_in_username = None
        self.login_manager.is_logged_in = False
        self.login_manager.user_info = None
        self.pack()
        self.topbar_instance.exit_username()

class Toptbar(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#2b2b47",border_width=1,border_color="#3a3a5a")
        self.not_register = customtkinter.CTkLabel(self, text="Вы неавторизованы", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.not_register.pack(side=TOP, anchor="ne",padx=20)
    def update_username(self, username):
        self.not_register.configure(text=f"Добро пожаловать, {username}")
    def exit_username(self):
        self.not_register.configure(text=f"Вы не авторизованы")
        
class Toptbar2(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#2b2b47",border_width=1, border_color="#3a3a5a")
        self.folowerrs_btn =  customtkinter.CTkButton(self, text='', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1",border_width=1, border_color="#3a3a5a", fg_color="#c64adf", hover_color="#aa3ec0")
        self.folowerrs_btn.pack(side=LEFT,padx=20, pady=(20, 20),ipady=10,ipadx=20)
        self.witdraw_btn =  customtkinter.CTkButton(self, text='Выплачено: 0', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1", fg_color="#4fbc71", border_width=1, border_color="#3a3a5a", hover_color="#6ce391")
        self.witdraw_btn.pack(side=LEFT,padx=0, pady=(20, 20),ipady=10,ipadx=20)
        self.pyramid_btn =  customtkinter.CTkButton(self, text='', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1", fg_color="#f88f33", border_width=1, border_color="#3a3a5a",hover_color="#f46f50")
        self.pyramid_btn.pack(side=LEFT,padx=20, pady=(20, 20),ipady=10,ipadx=20)
        self.days_btn =  customtkinter.CTkButton(self, text='Работаем: 0', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1", fg_color="#f86658", border_width=1, border_color="#3a3a5a",hover_color="#bd3528")
        self.days_btn.pack(side=LEFT,padx=0, pady=(20, 20),ipady=10,ipadx=20)
        self.menu_sht = None
        self.update_menu()

    def update_menu(self):
        response = requests.get(f"{SERVER_URL}/menu_sht")
        if response.status_code == 200:
            data = response.json()
            # Извлекаем значения max_user_id и max_piramid_id
            max_user_id = data.get("max_user_id", 0)
            max_piramid_id = data.get("max_piramid_id", 0)
            tdays = data.get("tdays", 0)
            # Обновляем тексты кнопок с полученными значениями
            self.update_followers_button(max_user_id)
            self.update_piramid_button(max_piramid_id)
            self.update_days_button(tdays)
        else:
            print("Ошибка при получении данных о пирамиде")

    def update_followers_button(self, max_id):
        # Обновляем текст кнопки участников с полученным Max ID
        self.folowerrs_btn.configure(text=f'Участников: {max_id}')

    def update_piramid_button(self, max_id):
        # Обновляем текст кнопки пирамид с полученным Max ID
        self.pyramid_btn.configure(text=f'Пирамид: {max_id}')
    def update_days_button(self, tdays):
        # Обновляем текст кнопки пирамид с полученным Max ID
        self.days_btn.configure(text=f'Дней работаем: {tdays}')
        
class Second_frame(customtkinter.CTkFrame):
    def __init__(self, master=None, rightbar_instance=None, pyramid_one=None, pyramid_two=None, is_logged_in=False, current_user_balance=0, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=5,fg_color="#ff2dd7",border_width=1,border_color="#3a3a5a")
        self.rightbar_instance = rightbar_instance
        self.pyramid_one = pyramid_one
        self.pyramid_two = pyramid_two
        self.current_user_balance = current_user_balance  # Добавлено
        self.balance_label = create_label(self, f"Баланс: {current_user_balance}р.", 7, 0)  # Добавлено
        self.logo_label2 = create_label(self, "Профиль", 0, 0, sticky="n", padx=10, pady=(0, 0))
        self.logo_Text1 = create_label(self, '', 1, 0,sticky="n", padx=10, pady=(0,0))
        self.logo_Text = create_label(self, '', 2, 0,pady=(0, 0))
        self.logo_Text3 = create_label(self, '', 3, 0)
        self.logo_Text4 = create_label(self, '', 4, 0)
        self.profil_email = create_label(self, '', 6, 0)
        self.cal_btn5 = create_button(self, 'Пополнить баланс',  self.open_balance_window, 8, 0, padx=30, pady=(10, 5))
        self.btn_exit = create_button(self, 'Выйти', self.exitbtn, 9, 0, padx=30, pady=(10, 5))

    def open_balance_window(self):
        logged_in_username = self.rightbar_instance.logged_in_username
        self.balance_window = Balanceup(logged_in_username, second_frame_instance=self)

    def exitbtn(self):
        self.pack_forget()
        self.rightbar_instance.auth_frame_instance.logout()
        
    def update_balance_label(self, new_balance):
        self.current_user_balance = new_balance
        self.balance_label.configure(text=f"Баланс: {new_balance}р.")

    def update_profile(self, nikname, fname, lname, city, mobile, email, balance):
        self.logo_Text.configure(text=f"Никнейм: {nikname}")
        self.logo_Text1.configure(text=f"{fname} {lname}")
        self.logo_Text3.configure(text=f"Город: {city }")
        self.logo_Text4.configure(text=f"Номер: {mobile}")
        self.profil_email.configure(text=f"Email: {email}")      
        self.current_user_balance = balance  # Обновление текущего баланса
        self.balance_label.configure(text=f"Баланс: {balance}р.")

class Balanceup(customtkinter.CTkToplevel):
    def __init__(self, username, second_frame_instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Здесь username - это имя пользователя, переданное при создании окна
        self.username = username
        self.second_frame_instance = second_frame_instance
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
        # Определите переменные nikname и balance
        nikname = self.username
        balance = self.reg_user.get()  # получите сумму из self.reg_user

        # Отправка запроса на сервер
        if balance == '' or balance == "0":
            CTkMessagebox(title="Ошибка", message="Введите цельную сумму в рублях", icon="cancel")
        else:
            response = requests.post(f"{SERVER_URL}/update_balance", json={"username": nikname, "balance": balance})
            # Обработка ответа
            if response.status_code == 200:
                response_data = response.json()
                messagebox.showinfo("Успешно", response_data["message"])

                # Обновление метки баланса с новым балансом
                new_balance = response_data.get("new_balance")
                print(response_data)  # Добавить эту строку, чтобы вывести ответ сервера в консоль
                if new_balance is not None:
                    self.second_frame_instance.update_balance_label(new_balance)

                self.close()  # Закрыть окно пополнения баланса
            else:
                messagebox.showerror("Ошибка", "Произошла ошибка при пополнении баланса")
    def close(self):
        self.destroy()

class Main_frame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#242438",border_width=1, border_color="#000000")
        Pyramid_one(self)
        Pyramid_two(self)

class Title_frame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#242438",border_width=1, border_color="#000000")
        self.textbox = customtkinter.CTkTextbox(master=self, width=90, font=customtkinter.CTkFont(size=20, weight="bold",) )
        self.textbox.pack(fill="both", expand=True, padx=10,pady=(10,10))
        self.textbox.insert("0.0", "Добро пожаловать, это бета тест)))" * 50)


class MainRules(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#242438",border_width=1, border_color="#000000")
        rules1 = "Для того, чтобы играть в лотерею Мечталлион, нужно зарегистрировать чек. Правила лотереи говорят, что оформить чек можно на официальном сайте акции или приобретя бумажный билет у партнеров конкурса. При обращении в «Почту России» можно купить билет в одном чеке. При покупке в сетях магазинов «Магнит», «Дикси» и «Красное и Белое» нужно приобрести 3 лотерейных билета в одном чеке. Важно, чтобы все билеты на Мечталлион были куплены в России.Следующий этап – зарегистрироваться на официальном сайте лотереи. Это обязательное условие проведения акции. Согласно правилам, участвовать могут только совершеннолетние лица, являющиеся гражданами РФ, постоянно проживающие на территории России и являющиеся налоговыми резидентами. Для этого нужно создать личный кабинет на сайте и указать имя и адрес электронной почты, приняв пользовательское соглашение. Без регистрации участие в акции Мечталлион будет невозможным."

        self.textbox1 = customtkinter.CTkTextbox(master=self, font=customtkinter.CTkFont(size=20, weight="bold",))
        self.textbox1.pack(fill='both',padx=5,pady=5,expand=True, )
        self.textbox1.insert("0.0", rules1)

class DataUpdater:
    def __init__(self):
        self.piramid_data = None
        self.piramid_data2 = None

    def update_piramid_data(self):
        response = requests.get(f"{SERVER_URL}/get_piramid_data")
        if response.status_code == 200:
            data = response.json()
            # Изменение здесь - извлекаем данные для обеих пирамид
            self.piramid_data = data['piramid_data1']
            self.piramid_data2 = data['piramid_data2']
        else:
            print("Ошибка при получении данных о пирамиде")
            self.piramid_data = None
            self.piramid_data2 = None

    def get_piramid_data(self):
        return self.piramid_data
    
    def get_piramid_data2(self):
        return self.piramid_data2

class LoginManager():
    def __init__(self, rightbar_instance, second_frame_instance, topbar_instance):
        self.rightbar_instance = rightbar_instance
        self.second_frame_instance = second_frame_instance
        self.topbar_instance = topbar_instance

    def login(self, username, password):
        response = requests.post(f"{SERVER_URL}/login", json={"username": username, "password": password})
        data = response.json()
        
        if response.status_code == 400:
            CTkMessagebox(title="Ошибка", message=data['message'], icon="cancel")
        else:
            self.is_logged_in = True
            user_info = data['user']
            balance = user_info["balance"]
            nikname = user_info["logins"]
            lname = user_info["lname"]
            fname = user_info["fname"]
            city = user_info["city"]
            mobile = user_info["mobile"]
            email = user_info["email"]
            self.second_frame_instance.update_profile(nikname, fname, lname, city, mobile, email, balance)
            self.rightbar_instance.pack_forget()
            self.second_frame_instance.pack(anchor="n",ipadx=10, ipady=10)
            CTkMessagebox(title="Успешно", message="Успешная авторизация")
            self.topbar_instance.update_username(nikname)
    def get_connected_user(self):
        return self.user_info if self.is_logged_in else None
    def logout(self):
        self.is_logged_in = False
        self.user_info = None
        self.auth_frame_instance.master.rightbar_instance.logged_in_username = None
        self.second_frame_instance.pack_forget()
        self.auth_frame_instance.pack()
        self.topbar_instance.exit_username()
class Pyramid_one(customtkinter.CTkFrame):
    def __init__(self, master=None, deposit_button=None, is_logged_in=False,**kw):
        super().__init__(master, **kw)
        self.data_updater = DataUpdater()
        self.is_logged_in = is_logged_in
        self.deposit_button = deposit_button
        self.configure(fg_color="transparent", border_width=1)
        self.pack(side=TOP,anchor="nw",padx=25,pady=(20,10)) 

        self.logo_Textp1 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_Textp1.grid(row=0, column=1, padx=0, pady=(10, 5),columnspan=2)

        self.logo_Textp2 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp2.grid(row=1, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp3 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp3.grid(row=2, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp4 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp4.grid(row=3, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp5 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp5.grid(row=4, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp6 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp6.grid(row=5, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp7 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp7.grid(row=6, column=1, padx=30, pady=(0, 0),sticky="w")

        self.button = customtkinter.CTkButton(self, text="Депозит", command='Deposit', state=tk.DISABLED)
        self.button.grid(row=7, column=1,pady=(15, 15),padx=10,sticky="e")
        self.update_labels_and_buttons()

    def update_labels_and_buttons(self):
        # Обновить данные
        self.data_updater.update_piramid_data()
        
        # Получить данные
        piramid_data = self.data_updater.get_piramid_data()

        if piramid_data is not None:
                # Преобразовать ответ JSON в Python словарь
                # Обновить GUI с данными из ответа
            minstavka = piramid_data['balance'] + piramid_data['minshag']
            self.logo_Textp1.configure(text=f"{piramid_data['name']}")
            self.logo_Textp2.configure(text=f"Баланс: {piramid_data['balance']}")
            self.logo_Textp3.configure(text=f"Участников: {piramid_data['participants']}")
            self.logo_Textp4.configure(text=f"Последний: {piramid_data['lastuser']}")
            self.logo_Textp5.configure(text=f"Минимальный шаг: {piramid_data['minshag']} + {piramid_data['balance'] } ({minstavka})")
            self.logo_Textp6.configure(text=f"Дата начала: {piramid_data['start_date']}")
            self.logo_Textp7.configure(text=f"Дата конца: {piramid_data['end_date']}")
        else:
                # Вывести сообщение об ошибке если запрос неуспешен
            print("Ошибка при получении данных о пирамиде")
        self.after(10000, self.update_labels_and_buttons)
        
class Pyramid_two(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.data_updater = DataUpdater()
        self.configure(fg_color="transparent", border_width=1)
        self.pack(side=BOTTOM, anchor="sw",padx=25,pady=(10,20)) 

        self.logo_Textp11 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_Textp11.grid(row=0, column=1, padx=0, pady=(10, 5),columnspan=2)

        self.logo_Textp21 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp21.grid(row=1, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp31 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp31.grid(row=2, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp41 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp41.grid(row=3, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp51 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp51.grid(row=4, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp61 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp61.grid(row=5, column=1, padx=30, pady=(0, 0),sticky="w")

        self.logo_Textp71 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_Textp71.grid(row=6, column=1, padx=30, pady=(0, 0),sticky="w")

        self.button2 = customtkinter.CTkButton(self, text="Депозит", command='Deposit2', state=tk.DISABLED)
        self.button2.grid(row=7, column=1,pady=(15, 15),padx=10,sticky="e")
        
        self.update_labels_and_buttons()
        
    def update_labels_and_buttons(self):
        # Обновить данные
        self.data_updater.update_piramid_data()
        
        # Получить данные
        piramid_data2 = self.data_updater.get_piramid_data2()

        if piramid_data2 is not None:
                # Преобразовать ответ JSON в Python словарь
                # Обновить GUI с данными из ответа
            minstavka = piramid_data2['balance'] + piramid_data2['minshag']
            self.logo_Textp11.configure(text=f"{piramid_data2['name']}")
            self.logo_Textp21.configure(text=f"Баланс: {piramid_data2['balance']}")
            self.logo_Textp31.configure(text=f"Участников: {piramid_data2['participants']}")
            self.logo_Textp41.configure(text=f"Последний: {piramid_data2['lastuser']}")
            self.logo_Textp51.configure(text=f"Минимальный шаг: {piramid_data2['minshag']} + {piramid_data2['balance'] } ({minstavka})")
            self.logo_Textp61.configure(text=f"Дата начала: {piramid_data2['start_date']}")
            self.logo_Textp71.configure(text=f"Дата конца: {piramid_data2['end_date']}")
        else:
                # Вывести сообщение об ошибке если запрос неуспешен
            print("Ошибка при получении данных о пирамиде")
        self.after(10000, self.update_labels_and_buttons)

class MainTitle(customtkinter.CTkFrame):
    def __init__(self, **kw):
        super().__init__( **kw)
        self.configure(corner_radius=0, fg_color="#242438",border_width=1, border_color="#000000")
        self.logo_Textp11 = customtkinter.CTkLabel(self, text='Добро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловатьДобро пожаловать', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_Textp11.grid(row=0, column=1, padx=0, pady=(10, 5),columnspan=2)

class Registration(customtkinter.CTkToplevel):
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
        response = requests.post(f"{SERVER_URL}/register", json={
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


def create_label(parent, text, row, column, padx=10, pady=(0, 0), sticky="w"):
    label = customtkinter.CTkLabel(parent, text=text, font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
    label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    return label

def create_button(parent, text, command, row, column,padx=0, pady=(0, 0),sticky="w"):
    button = customtkinter.CTkButton(parent, text=text, command=command)
    button.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    return button
def validate(u_input): # callback function
    return u_input.isdigit()

root = Root()
root.mainloop()
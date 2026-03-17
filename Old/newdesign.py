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

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Октаэдр - заработай миллион")
        self.geometry("1200x750")
        self.configure(fg_color="#24234a")
        self.frame = Frame(self)
        self.frame.pack(side=LEFT, fill=Y)

        self.second_frame = Second_frame(self)
        
        self.toptbar = Toptbar(self)
        self.toptbar.pack(side=TOP, fill=X)

        self.toptbar2 = Toptbar2(self)
        self.toptbar2.pack(side=TOP, fill=X)

        self.rightbar = Rightbar(self, profile_instance=self.second_frame)
        self.rightbar.pack(side=RIGHT, fill=Y)

        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True, )

        # словарь для хранения фреймов
        self.frames = {}
        for F in (Main_frame, MainTitle, Rules):
            frame = F(container, self)
            self.frames[F] = frame
            # Используем pack вместо grid
            frame.pack()

        # отображаем MainFrame
        self.show_frame(Main_frame)

    def show_frame(self, frame_class):
        # скрыть все фреймы
        for f in self.frames.values():
            f.pack_forget()
        # отобразить выбранный фрейм
        frame = self.frames[frame_class]
        frame.pack(pady=(5,5),padx=5,fill=BOTH,expand=True)


class Frame(customtkinter.CTkFrame):
    def __init__(self, controller, master=None, **kw):
        super().__init__(master, **kw)
        self.controller = controller
        self.configure(corner_radius=0, fg_color="#2b2b47",border_width=0)
        logotype = customtkinter.CTkLabel(self, text="Октаэдр", font=customtkinter.CTkFont(size=25, weight="bold"))
        logotype.pack(side=TOP, anchor="nw", padx=50, pady=(20,0))

        left_menu = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent",border_width=0)
        left_menu.pack(side=TOP, pady=(50,0))
        home_btn =  customtkinter.CTkButton(left_menu , text='Главная', command=lambda: controller.show_frame(MainTitle), font=customtkinter.CTkFont(size=13, weight="bold"),corner_radius=4,text_color="#bfbeda", fg_color="transparent", hover_color="#da3c2d")
        home_btn.pack(padx=20, pady=(5, 0),ipady=10,ipadx=20)

        rules_btn =  customtkinter.CTkButton(left_menu , text='Правила', command=lambda: controller.show_frame(Rules),font=customtkinter.CTkFont(size=13, weight="bold"),corner_radius=4,text_color="#bfbeda", fg_color="transparent", hover_color="#da3c2d")
        rules_btn.pack(padx=20, pady=(5, 0),ipady=10,ipadx=20)

        profile_btn =  customtkinter.CTkButton(left_menu , text='Профиль', command="login",font=customtkinter.CTkFont(size=13, weight="bold"),corner_radius=4,text_color="#bfbeda", fg_color="transparent", hover_color="#da3c2d")
        profile_btn.pack(padx=20, pady=(5, 0),ipady=10,ipadx=20)

        pyramid_btn =  customtkinter.CTkButton(left_menu , text='Пирамиды', command=lambda: controller.show_frame(Main_frame),font=customtkinter.CTkFont(size=13, weight="bold"),corner_radius=4,text_color="#bfbeda", fg_color="transparent", hover_color="#da3c2d")
        pyramid_btn.pack(padx=20, pady=(5, 0),ipady=10,ipadx=20)

        loterea_btn =  customtkinter.CTkButton(left_menu , text='Лотерея', command="login",font=customtkinter.CTkFont(size=13, weight="bold"),corner_radius=4,text_color="#bfbeda", fg_color="transparent", hover_color="#da3c2d")
        loterea_btn.pack(padx=20, pady=(5, 0),ipady=10,ipadx=20)

        contacts_btn =  customtkinter.CTkButton(left_menu , text='Контакты', command="login",font=customtkinter.CTkFont(size=13, weight="bold"),corner_radius=4,text_color="#bfbeda", fg_color="transparent", hover_color="#da3c2d")
        contacts_btn.pack(padx=20, pady=(5, 0),ipady=10,ipadx=20)

        about_btn =  customtkinter.CTkButton(left_menu , text='О нас', command="login",font=customtkinter.CTkFont(size=13, weight="bold"),corner_radius=4,text_color="#bfbeda", fg_color="transparent", hover_color="#da3c2d")
        about_btn.pack(padx=20, pady=(5, 0),ipady=10,ipadx=20)

class Second_frame(customtkinter.CTkFrame):
    def __init__(self, master=None, rightbar_instance=None,**kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0)
        self.rightbar_instance = rightbar_instance
        self.logo_label2 = customtkinter.CTkLabel(self, text="Профиль", font=customtkinter.CTkFont(size=20, weight="bold"), width=140)
        self.logo_label2.grid(row=0, column=0, padx=10, pady=(20, 10))

        self.logo_Text1 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
        self.logo_Text1.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.logo_Text = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
        self.logo_Text.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

        self.logo_Text3 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
        self.logo_Text3.grid(row=3, column=0, padx=10, pady=(0, 10), sticky=W)

        self.logo_Text4 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
        self.logo_Text4.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="w")

        self.logo_Text5 = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
        self.logo_Text5.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")
        self.profil_email = customtkinter.CTkLabel(self, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
        self.profil_email.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="w")

        self.cal_btn5 =  customtkinter.CTkButton(self, text='Пополнить баланс', command=self.open_balance_window)
        self.cal_btn5.grid(row=7, column=0,pady=(10, 10))

        self.btn_exit =  customtkinter.CTkButton(self, text='Выйти', command=self.exitbtn)
        self.btn_exit.grid(row=8, column=0,pady=(120, 30),padx=20)

    def exitbtn(self):
        self.rightbar_instance.auth_frame.pack()
        self.pack_forget()  
        
    def update_profile(self, nikname, fname, lname, city, mobile, email, balance):
        self.logo_Text.configure(text=f"Никнейм: {nikname}")
        self.logo_Text1.configure(text=f"{fname} {lname}")
        self.logo_Text3.configure(text=f"Город: {city }")
        self.logo_Text4.configure(text=f"Номер: {mobile}")
        self.profil_email.configure(text=f"Email: {email}")      
        self.logo_Text5.configure(text=f"Баланс: {balance}р.")
    def open_balance_window(self):
        self.balance_window = Balanceup(self)
    def update_balance(self, amount):
        self.current_user_balance += amount
        self.balance_label.configure(text=f"Баланс: {self.current_user_balance}р.")
class Toptbar(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#2b2b47",border_width=1,border_color="#3a3a5a")
        not_register = customtkinter.CTkLabel(self, text="Вы неавторизованы", font=customtkinter.CTkFont(size=12, weight="bold"))
        not_register.pack(side=TOP, anchor="ne",padx=20)

class Toptbar2(customtkinter.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#2b2b47",border_width=1, border_color="#3a3a5a")
        folowerrs_btn =  customtkinter.CTkButton(self, text='Участников: 0', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1",border_width=1, border_color="#3a3a5a", fg_color="#c64adf", hover_color="#aa3ec0")
        folowerrs_btn.pack(side=LEFT,padx=20, pady=(20, 20),ipady=10,ipadx=20)
        witdraw_btn =  customtkinter.CTkButton(self, text='Выплачено: 0', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1", fg_color="#4fbc71", border_width=1, border_color="#3a3a5a", hover_color="#6ce391")
        witdraw_btn.pack(side=LEFT,padx=0, pady=(20, 20),ipady=10,ipadx=20)
        pyramid_btn =  customtkinter.CTkButton(self, text='Пирамид: 0', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1", fg_color="#f88f33", border_width=1, border_color="#3a3a5a",hover_color="#f46f50")
        pyramid_btn.pack(side=LEFT,padx=20, pady=(20, 20),ipady=10,ipadx=20)
        days_btn =  customtkinter.CTkButton(self, text='Работаем: 0', command="login",font=customtkinter.CTkFont(size=14, weight="bold"),corner_radius=6,text_color="#e6e6f1", fg_color="#f86658", border_width=1, border_color="#3a3a5a",hover_color="#bd3528")
        days_btn.pack(side=LEFT,padx=0, pady=(20, 20),ipady=10,ipadx=20)

class Rightbar(customtkinter.CTkFrame):
    def __init__(self, master=None, profile_instance=None, main_frame_instance=None, **kw):
        super().__init__(master, **kw)
        self.configure(corner_radius=0, fg_color="#3e3e60", border_width=1, border_color="#1a1a31")
        self.profile_instance = profile_instance
        self.main_frame_instance = main_frame_instance
        self.auth_frame = customtkinter.CTkFrame(self, fg_color="#26264a", border_width=1, border_color="#505078")
        self.auth_frame.pack(pady=(5, 5), padx=5)
        self.second_frame_instance = Second_frame(self, rightbar_instance=self)
        self.login_entry = customtkinter.CTkEntry(self.auth_frame, placeholder_text="Логин")
        self.login_entry.pack(padx=10, pady=(10, 0))
        
        self.pass_entry = customtkinter.CTkEntry(self.auth_frame, placeholder_text="Пароль", show="*")
        self.pass_entry.pack(padx=10, pady=(5, 5))
        self.login_btn = customtkinter.CTkButton(self.auth_frame, text='Войти', command=self.login)
        self.login_btn.pack(padx=10, pady=(5, 0))
        self.register_btn =  customtkinter.CTkButton(self.auth_frame , text='Регистрация', command=self.open_registration_window,)
        self.register_btn.pack(padx=10, pady=(10, 10))
        self.response_data = None

    def open_registration_window(self):
        registration_window = registration(master=self)
        registration_window.grab_set()

    def login(self):
        username = self.login_entry.get()
        password = self.pass_entry.get()
        
        response = requests.post("http://ideal-web.site:5000/login", json={"username": username, "password": password})
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
            self.response_data = data
            self.second_frame_instance.update_profile(nikname, fname, lname, city, mobile, email, balance)
            self.auth_frame.pack_forget()
            self.second_frame_instance.pack()
            CTkMessagebox(title="Успешно", message="Успешная авторизация")
            self.main_frame_instance.button.configure(state=ctk.NORMAL)
            self.main_frame_instance.button2.configure(state=ctk.NORMAL)


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
        


# class Rightbar(customtkinter.CTkFrame):
#     def __init__(self, master=None, **kw):
#         super().__init__(master, **kw)
#         self.configure(corner_radius=0, fg_color="#3e3e60",border_width=1,border_color="#1a1a31")
#         auth_frame = customtkinter.CTkFrame(self, fg_color="#26264a", border_width=1, border_color="#505078")
#         auth_frame.pack( pady=(5,5), padx=5,)


#         login_entry = customtkinter.CTkEntry(auth_frame, placeholder_text="Логин",)
#         login_entry.pack( padx=10, pady=(10, 0))

#         pass_entry = customtkinter.CTkEntry(auth_frame , placeholder_text="Пароль",show="*",)
#         pass_entry.pack( padx=10, pady=(5, 5))


#         login_btn =  customtkinter.CTkButton(auth_frame , text='Войти', command=login,)
#         login_btn.pack(padx=10, pady=(5, 0))

#         register_btn =  customtkinter.CTkButton(auth_frame , text='Регистрация', command=registration,)
#         register_btn.pack(padx=10, pady=(10, 10))

# def login():
#     global user_info, nikname, balance
#     username = login_entry.get()
#     password = pass_entry.get()

#     # Отправка запроса на сервер
#     response = requests.post("http://ideal-web.site:5000/login", json={
#         "username": username,
#         "password": password
#     })

#     # Обработка ответа
#     data = response.json()
#     if response.status_code == 400:
#         CTkMessagebox(title="Ошибка", message=data['message'], icon="cancel")
#     else:
#         user_info = data['user']
#         balance = user_info["balance"]
#         nikname = user_info["logins"]
#         lname = user_info["lname"]
#         fname = user_info["fname"]
#         city = user_info["city"]
#         mobile = user_info["mobile"]
#         email = user_info["email"]
#         logo_Text.configure(text=f"Никнейм: {nikname}")
#         logo_Text1.configure(text=f"{fname} {lname}")
#         logo_Text3.configure(text=f"Город: {city }")
#         logo_Text4.configure(text=f"Номер: {mobile}")
#         profil_email.configure(text=f"Email: {email}")      
#         logo_Text5.configure(text=f"Баланс: {balance}р.")
 
#         CTkMessagebox(title="Успешно", message="Успешная авторизация")
#         # frame_2_button_event()
#         button.configure(state=ctk.NORMAL)
#         button2.configure(state=ctk.NORMAL)   


class MainTitle(customtkinter.CTkFrame):
    def __init__(self, container, controller, **kw):
        super().__init__(container, **kw)
        self.configure(corner_radius=0, fg_color="#242438",border_width=1, border_color="#000000")
        self.controller = controller

class Rules(customtkinter.CTkFrame):
    def __init__(self, container, controller, **kw):
        super().__init__(container, **kw)
        self.configure(corner_radius=0, fg_color="#242438",border_width=1, border_color="#000000")
        self.controller = controller

class Main_frame(customtkinter.CTkFrame):
    def __init__(self, container, controller, **kw):
        super().__init__(container, **kw)
        self.controller = controller
        self.configure(corner_radius=0, fg_color="#242438",border_width=1, border_color="#000000")
        mainback = customtkinter.CTkFrame(self, fg_color="transparent", border_width=1)
        mainback.pack(side=TOP,anchor="nw",padx=25,pady=(20,10)) 

        mainbacks = customtkinter.CTkFrame(self,fg_color="transparent", border_width=1)
        mainbacks.pack(side=BOTTOM, anchor="sw",padx=25,pady=(10,20)) 

        logo_Textp1 = customtkinter.CTkLabel(mainback, text='', font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_Textp1.grid(row=0, column=1, padx=0, pady=(10, 5),columnspan=2)

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
        logo_Textp11.grid(row=0, column=1, padx=0, pady=(10, 5),columnspan=2)

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

        self.button2 = customtkinter.CTkButton(mainbacks, text="Депозит", command=Deposit2, state=tk.DISABLED)
        self.button2.grid(row=7, column=1,pady=(15, 15),padx=10,sticky="e")

        self.button = customtkinter.CTkButton(mainback, text="Депозит", command=Deposit, state=tk.DISABLED)
        self.button.grid(row=7, column=1,pady=(15, 15),padx=10,sticky="e")

        response = requests.get('http://ideal-web.site:5000/get_piramid_data')
            # Проверить, что запрос успешен
        if response.status_code == 200:
                # Преобразовать ответ JSON в Python словарь
            piramid_data = response.json()
                # Обновить GUI с данными из ответа
            minstavka = {piramid_data['balance']} + {piramid_data['minshag']}
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

class Balanceup(customtkinter.CTkToplevel):
    def __init__(self, *args, nikname=None, response_data=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.nikname = nikname
        self.response_data = response_data
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
        nikname = self.nikname
        if balance == '' or balance == "0":
            CTkMessagebox(title="Ошибка", message="Введите цельную сумму в рублях", icon="cancel")
        else:
            # Отправка запроса на сервер
            response = requests.post("http://ideal-web.site:5000/update_balance", json={"username": nikname, "balance": balance})

            # Обработка ответа
            if response.status_code == 200:
                obnovleniedepost(nikname, self.second_frame_instance.logo_Text, self.second_frame_instance.logo_Text1, self.second_frame_instance.logo_Text3, self.second_frame_instance.logo_Text4, self.second_frame_instance.logo_Text5)
                messagebox.showinfo("Успешно", response.json()["message"])
                # obnovleniedepost()  # функция обновления данных на интерфейсе
                self.close()  # Закрыть окно пополнения баланса
            else:
                CTkMessagebox(title="Ошибка", message="Произошла ошибка при пополнении баланса", icon="cancel")
    def close(self):
        self.destroy()

def obnovleniedepost(nikname, logo_Text, logo_Text1, logo_Text3, logo_Text4, logo_Text5):
    # Отправка запроса на сервер
    response = requests.post("http://ideal-web.site:5000/get_user_info", json={"username": nikname})

    # Обработка ответа
    if response.status_code == 404:
        messagebox.showerror("Ошибка", response.json()["message"])
    else:
        user_info = response.json()
        balance = user_info["balance"]
        
        logo_Text.configure(text=f"Никнейм: {user_info['logins']}")
        logo_Text1.configure(text=f"{user_info['fname']} {user_info['lname']}")
        logo_Text3.configure(text=f"Город: {user_info['city']}")
        logo_Text4.configure(text=f"Номер: {user_info['mobile']}")
        logo_Text5.configure(text=f"Баланс: {balance}р.")
    
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
            # obnpir()
            # obnpir2()
            obnovleniedepost()
            mymessagebox.showinfo("Успешно", "Вы успешно зарегестрировались")
            self.close()  # Закрыть окно пополнения баланса
        else:
            CTkMessagebox(title="Ошибка", message=data['message'], icon="cancel")
    def close(self):
        self.destroy()


def validate(u_input): # callback function
    return u_input.isdigit()


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



def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)	

root = Root()
root.mainloop()
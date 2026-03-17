from tkinter import *
from tkinter import ttk
import re
import tkinter
import tkinter.messagebox
import customtkinter
import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter.messagebox as mymessagebox
import mysql.connector as mysqlconnector
import mysql.connector
import tkinter as tk
import tkinter.messagebox as mb
import random
import tkinter.ttk
import requests
import pandas as pd
import json
import configparser


customtkinter.set_default_color_theme("dark-blue.json")

def printResponse():
    print ("Status code  : ", r.status_code)
    print ("Encoding     : ", r.encoding)
    print ("JSON         : ", r.json())
    print ("")

r = requests.get("http://localhost:5000/logs");
data = r.json() 

mydb = mysql.connector.connect(
      host="",
      user="",
      password="@",
      database=""
    )

def save_to_mysql(data):
    try:
        mydb = mysql.connector.connect(
            host="",
            user="",
            password="",
            database=""
        )
        cursor = mydb.cursor()
        insert_query = "INSERT INTO log_entries (ip, time, status_code, requested_url, user_agent) VALUES (%s, %s, %s, %s, %s)"
        for idx in data['ip']:
            ip = data['ip'][idx]
            time = data['time'][idx]
            status_code = data['status_code'][idx]
            requested_url = data['requested_url'][idx]
            user_agent = data['user_agent'][idx]
            values = (ip, time, status_code, requested_url, user_agent)
            cursor.execute(insert_query, values)
        mydb.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        mydb.close()

def output():
        mydb = mysql.connector.connect(
            host="ideal-web.site",
            user="admin_alexunderlag",
            password="OG+J(0@T{E[uakY@",
            database="admin_python"
        )
        cursor = mydb.cursor()
        query = "SELECT * FROM log_entries"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        mydb.close()

def output302():
        mydb = mysql.connector.connect(
            host="ideal-web.site",
            user="admin_alexunderlag",
            password="OG+J(0@T{E[uakY@",
            database="admin_python"
        )
        cursor = mydb.cursor()
        query = "SELECT * FROM log_entries WHERE status_code = 302"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        mydb.close()

def close(self):
    self.destroy()

def validate(u_input):
    return u_input.isdigit()


def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)	

def login():
    global smyresult
    mydb.reconnect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM user where logins = '"+ user_entry.get() +"' and password = '"+ user_pass.get() +"';")
    myresult = mycursor.fetchone()
    save_to_mysql(data)
    if myresult==None:
        mymessagebox.showerror("Ошибка", "Неверный пароль или имя пользователя")

    else:
        smyresult = list(myresult.values())
        balance = smyresult[7]
        frame_2_button_event()
        logo_Text.configure(text=f"Никнейм: {smyresult[1]}")
        logo_Text4.configure(text=f"Номер: {smyresult[6]}")
        profil_email.configure(text=f"Email: {smyresult[8]}")       
        print(smyresult)
        button.configure(state=ctk.NORMAL)
        
        mymessagebox.showinfo("Успешно", "Успешная авторизация")
    

def select_frame_by_name(name):
        if name == "home":
            frame.grid(row=0, column=1, sticky="nsew")
        else:
            frame.grid_forget()
        if name == "frame_2":
            second_frame.grid(row=0, column=1, sticky="nsew")
            mainback.grid(row=0, column=2,padx=20, pady=(20, 10), sticky="n")
        else:
            second_frame.grid_forget()
            mainback.grid_forget()

def btn_exit_fun():
        select_frame_by_name("home")
        button.configure(state=tk.DISABLED)

def frame_2_button_event():
        select_frame_by_name("frame_2")


root = customtkinter.CTk()
root.title("Логин с Nginx")
root.geometry("756x512")

frame = customtkinter.CTkFrame(root, corner_radius=0)
frame.grid_columnconfigure(0, weight=1)

mainback = customtkinter.CTkFrame(root)
mainback.grid(row=0, column=2,padx=20, pady=(20, 10), sticky="n")

second_frame = customtkinter.CTkFrame(root, corner_radius=0)

select_frame_by_name("home")

logo_label = customtkinter.CTkLabel(frame, text="Авторизация", font=customtkinter.CTkFont(size=20, weight="bold"), width=140)
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

user_entry = customtkinter.CTkEntry(frame, placeholder_text="Логин")
user_entry.grid(row=1, column=0, padx=20, pady=(20, 0))
user_pass = customtkinter.CTkEntry(frame, placeholder_text="Пароль",show="*")
user_pass.grid(row=2, column=0, padx=20, pady=(10, 10))

cal_btn =  customtkinter.CTkButton(frame, text='Войти', command=login)
cal_btn.grid(row=4, column=0)


logo_label2 = customtkinter.CTkLabel(second_frame, text="Профиль", font=customtkinter.CTkFont(size=20, weight="bold"), width=140)
logo_label2.grid(row=0, column=0, padx=10, pady=(20, 10))

logo_Text1 = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text1.grid(row=1, column=0, padx=10, pady=(0, 10))

logo_Text = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

logo_Text4 = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
logo_Text4.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="w")

profil_email = customtkinter.CTkLabel(second_frame, text='', font=customtkinter.CTkFont(size=12, weight="bold"), width=70)
profil_email.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="w")

btn_exit =  customtkinter.CTkButton(second_frame, text='Выйти', command=btn_exit_fun)
btn_exit.grid(row=8, column=0,pady=(250, 30),padx=20)

button = customtkinter.CTkButton(mainback, text="Вывести все", command=output, state=tk.DISABLED)
button.grid(row=5, column=2,pady=(0, 10),padx=10)
button11 = customtkinter.CTkButton(mainback, text="302", command=output302)
button11.grid(row=6, column=2,pady=(0, 10),padx=10)

root.mainloop()
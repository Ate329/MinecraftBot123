import tkinter as tk
from tkinter import Button, Entry, Label
import threading
import webbrowser
from lib.bot import start_bot, stop_bot
from lib.config import load_config
from lib.handlers import setup_handlers

def start_bot_thread(host, port, username, config):
    bot_thread = threading.Thread(target=start_bot, args=(host, port, username, config, setup_handlers))
    bot_thread.start()
    return bot_thread

def create_ui():
    root = tk.Tk()
    root.geometry('319x202')
    root.configure(background='#F0F8FF')
    root.title('Minecraft Bot')

    host = Entry(root)
    host.place(x=135, y=20)

    port = Entry(root)
    port.place(x=135, y=50)

    nick = Entry(root)
    nick.place(x=135, y=80)

    Label(root, text='IP Address: ', bg='#F0F8FF', font=('arial', 12)).place(x=35, y=20)
    Label(root, text='IP Port: ', bg='#F0F8FF', font=('arial', 12)).place(x=35, y=50)
    Label(root, text='Username: ', bg='#F0F8FF', font=('arial', 12)).place(x=35, y=80)

    config = load_config('config.ini')

    start_button = Button(root, text='Start the bot', bg='#F0F8FF', font=('arial', 12), 
                          command=lambda: start_bot_thread(host.get(), port.get(), nick.get(), config))
    start_button.place(x=200, y=115)

    Button(root, text='Server List', bg='#F0F8FF', font=('arial', 12), command=server_list).place(x=20, y=115)
    Button(root, text='Stop', bg='#F0F8FF', font=('arial', 12), command=stop_bot).place(x=131, y=115)
    Button(root, text="Based on", bg="#F0F8FF", font=('arial', 12), command=open_based_on).place(x=20, y=158)
    Button(root, text="My GitHub Page", bg="#F0F8FF", font=('arial', 12), command=open_github_page).place(x=131, y=158)

    root.mainloop()

def server_list():
    with open("ServerList.txt") as list_file:
        print(list_file.read())

def open_based_on():
    webbrowser.open('https://github.com/YTFort/24-Aternos')

def open_github_page():
    webbrowser.open('https://github.com/Ate329')

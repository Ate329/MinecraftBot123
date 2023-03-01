import os
import threading
import webbrowser
from configparser import ConfigParser
from tkinter import Button, Entry, Label, Tk

from javascript import On, require

mineflayer = require('mineflayer')
Vec3 = require("vec3").Vec3
registry = require('prismarine-registry')
ChatMessage = require('prismarine-chat')

config = ConfigParser()
config.read('config.ini')


def startbot():
    global bot
    bot = mineflayer.createBot({
        'host': f'{host.get()}',
        'port': port.get(),
        'username': f'{nick.get()}'
    })

    @On(bot, "login")
    def login(this):
        bot.chat(config.get('command', 'commandjoin'))
        bot.chat('Hi everyone')

    @On(bot, "error")
    def error(err, *a):
        print("Connection ERROR", err, a)

    @On(bot, "kicked")
    def kicked(this, reason, *a):
        print("I was kicked", reason, a)
        print('Reconnecting')
        startbot()

    @On(bot, "chat")
    def antiafk(this, username, message, *args):
        if username == bot.username:
            return

        elif message.startswith(config.get('command', 'pos')):
            pb = bot.entity.position
            bot.chat(f"I am at {pb.toString()}")

        elif message.startswith(config.get('command', 'afktrue')):
            bot.chat('AntiAFK started')
            bot.setControlState('forward', True)
            bot.setControlState('jump', True)
            bot.setControlState('sprint', True)

        elif message.startswith(config.get('command', 'afkfalse')):
            bot.chat('AntiAFK stopped')
            bot.clearControlStates()

        elif message.startswith(config.get('command', 'time')):
            bot.chat(f"Current time: " + str(bot.time.timeOfDay))

        elif message.lower() in ["hi", "hello", "hey"]:
            bot.chat("Hi there, " + username + "!")

        elif message.lower() in ['your', 'ur']:
            bot.chat('mom!')

        elif message.lower() in ['who']:
            bot.chat('asked?')

        elif message.lower() in ['when']:
            bot.chat('did I ask?')

        elif message.lower() in ['i love u', 'i luv u', 'i love you', 'i luv you']:
            bot.chat('I love you too, ' + username)

        elif message.lower() in ['go']:
            bot.chat('kill yourself')

        elif message.lower() in ['i want']:
            bot.chat('your mom')

    @On(bot, "spawn")
    def spawn(this):
        bot.chat(f"Spawn is at {bot.spawnPoint.toString()}")

    @On(bot, "death")
    def death(this):
        bot.chat("I died x_x")

    def say_position(username):
        p = bot.entity.position
        bot.chat(f"I am at {p.toString()}")

    @On(bot, "rain")
    def rain(this):
        if bot.isRaining:
            bot.chat("It started raining")
        else:
            bot.chat("It stopped raining")

    @On(bot, "playerJoined")
    def playerJoined(this, player):
        print("joined", player)
        if player["username"] != bot.username:
            bot.chat(f"Hello {player['username']}, Welcome to the server")

    @On(bot, "playerLeft")
    def playerLeft(this, player):
        if player["username"] == bot.username:
            return
        bot.chat(f"Bye {player['username']}")

    @On(bot, "entitySleep")
    def entitySleep(this, entity):
        bot.chat(f"Good night, {entity.username}")

    @On(bot, "entityWake")
    def entityWake(this, entity):
        bot.chat(f"Good morning, {entity.username}")

    @On(bot, "entityEffect")
    def entityEffect(player, this, entity, effect):
        print({player.username}, "got entityEffect", entity, effect)

    @On(bot, "entityEffectEnd")
    def entityEffectEnd(player, this, entity, effect, ):
        print({player.username}, "'s", "entityEffectEnd", entity, effect)

    @On(bot, "entityAttach")
    def entityAttach(this, entity, vehicle):
        if entity.type == "player" and vehicle.type == "object":
            print(f"Sweet, {entity.username} is riding the {vehicle.objectType}")

    @On(bot, "entityDetach")
    def entityDetach(this, entity, vehicle):
        if entity.type == "player" and vehicle.type == "object":
            print(f"Lame, {entity.username} stopped riding the {vehicle.objectType}")

    @On(bot, "entityHurt")
    def entityHurt(this, entity):
        if entity.type == "mob":
            bot.chat(f"The {entity.mobType} got hurt!")
        elif entity.type == "player":
            if entity.username in bot.players:
                bot.chat(f"Poor {entity.username} got hurt.")

    @On(bot, "chestLidMove")
    def chestLidMove(this, block, isOpen, *a):
        action = "open" if isOpen else "close"
        bot.chat(f"Hey, did someone just {action} a chest?")


def stopb():
    os.system('taskkill /f /im node.exe')
    strtb.join()


strtb = threading.Thread(target=startbot)


def startb():
    strtb.start()


def ServerList():
    list = open("ServerList.txt")
    print(list.read())

def based_on():
    webbrowser.open('https://github.com/YTFort/24-Aternos')


def my_github_page():
    webbrowser.open('https://github.com/Ateee329')


root = Tk()

root.geometry('319x202')
root.configure(background='#F0F8FF')
root.title('Minecraft Bot')

host = Entry(root)
host.place(x=135, y=20)

port = Entry(root)
port.place(x=135, y=50)

nick = Entry(root)
nick.place(x=135, y=80)

Label(root, text='IP Address: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=35, y=20)

Label(root, text='IP Port: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=35, y=50)

Label(root, text='Username: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=35, y=80)

Button(root, text='Start the bot', bg='#F0F8FF', font=('arial', 12, 'normal'), command=startb).place(x=200, y=115)

Button(root, text='Server List', bg='#F0F8FF', font=('arial', 12, 'normal'), command=ServerList).place(x=20, y=115)

Button(root, text='Stop', bg='#F0F8FF', font=('arial', 12, 'normal'), command=stopb).place(x=131, y=115)

Button(root, text="Based on", bg="#F0F8FF", font=('arial', 12, 'normal'), command=based_on).place(x=20, y=158)

Button(root, text="My GitHub Page", bg="#F0F8FF", font=('arial', 12, 'normal'), command=my_github_page).place(x=131, y=158)

root.mainloop()

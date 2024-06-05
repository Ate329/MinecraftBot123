from javascript import On, require

mineflayer = require('mineflayer')
Vec3 = require("vec3").Vec3
registry = require('prismarine-registry')
ChatMessage = require('prismarine-chat')

bot = None

def create_bot(host, port, username):
    global bot
    bot = mineflayer.createBot({
        'host': host,
        'port': int(port),
        'username': username
    })
    return bot

def start_bot(host, port, username, config, handlers):
    global bot
    bot = create_bot(host, port, username)
    handlers.setup_handlers(bot, config)
    return bot

def stop_bot():
    import os
    os.system('taskkill /f /im node.exe')
    if bot and bot.process and bot.process.poll() is None:
        bot.process.terminate()

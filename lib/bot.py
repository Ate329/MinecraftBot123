from javascript import On, require
import platform
import os


mineflayer = require('mineflayer')
Vec3 = require("vec3").Vec3
registry = require('prismarine-registry')
ChatMessage = require('prismarine-chat')

bot = None

def create_bot(host, port, username):
    """
    Creates a new mineflayer bot instance.
    
    Parameters:
    host (str): The server host.
    port (int): The server port.
    username (str): The bot's username.

    Returns:
    bot: The created mineflayer bot instance.
    """
    global bot
    bot = mineflayer.createBot({
        'host': host,
        'port': int(port),
        'username': username
    })
    return bot

def start_bot(host, port, username, config, handlers):
    """
    Starts the bot with given parameters and sets up handlers.
    
    Parameters:
    host (str): The server host.
    port (int): The server port.
    username (str): The bot's username.
    config (dict): Configuration dictionary for the bot.
    handlers (module): Handlers module with setup_handlers function.
    
    Returns:
    bot: The started mineflayer bot instance.
    """
    global bot
    bot = create_bot(host, port, username)
    handlers.setup_handlers(bot, config)
    return bot

def stop_bot():
    """
    Stops the bot and terminates the node process based on the OS.
    """
    global bot
    if bot:
        bot.quit()  # Gracefully disconnect the bot from the server
        bot = None  # Reset the bot instance to None

    # Detect the operating system
    current_os = platform.system()

    if current_os == "Windows":
        os.system('taskkill /f /im node.exe')  # Force kill the node process on Windows
    elif current_os == "Linux":
        os.system('pkill -f node')  # Force kill the node process on Linux
    else:
        print(f"Unsupported OS: {current_os}. Please terminate the Node.js process manually.")

if __name__ == "__main__":
    print("You are not suppose to run this module individually")
    
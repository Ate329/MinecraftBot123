def setup_handlers(bot, config):
    @On(bot, "login")
    def on_login(this):
        bot.chat(config.get('command', 'commandjoin'))
        bot.chat('Hi everyone')

    @On(bot, "error")
    def on_error(err, *args):
        print("Connection ERROR", err, args)

    @On(bot, "kicked")
    def on_kicked(this, reason, *args):
        print("I was kicked", reason, args)
        print('Reconnecting')
        bot.reconnect()

    @On(bot, "chat")
    def on_chat(this, username, message, *args):
        if username == bot.username:
            return

        command = message.lower().strip()

        if command.startswith(config.get('command', 'pos')):
            pb = bot.entity.position
            bot.chat(f"I am at {pb.toString()}")

        elif command.startswith(config.get('command', 'afktrue')):
            bot.chat('AntiAFK started')
            bot.setControlState('forward', True)
            bot.setControlState('jump', True)
            bot.setControlState('sprint', True)

        elif command.startswith(config.get('command', 'afkfalse')):
            bot.chat('AntiAFK stopped')
            bot.clearControlStates()

        elif command.startswith(config.get('command', 'time')):
            bot.chat(f"Current time: {bot.time.timeOfDay}")

        elif command in ["hi", "hello", "hey"]:
            bot.chat(f"Hi there, {username}!")

        elif command in ['your', 'ur']:
            bot.chat('mom!')

        elif command in ['who']:
            bot.chat('asked?')

        elif command in ['when']:
            bot.chat('did I ask?')

        elif command in ['i love u', 'i luv u', 'i love you', 'i luv you']:
            bot.chat(f"I love you too, {username}")

    @On(bot, "spawn")
    def on_spawn(this):
        bot.chat(f"Spawn is at {bot.spawnPoint.toString()}")

    @On(bot, "death")
    def on_death(this):
        bot.chat("I died x_x")

    @On(bot, "rain")
    def on_rain(this):
        if bot.isRaining:
            bot.chat("It started raining")
        else:
            bot.chat("It stopped raining")

    @On(bot, "playerJoined")
    def on_player_joined(this, player):
        print("joined", player)
        if player["username"] != bot.username:
            bot.chat(f"Hello {player['username']}, Welcome to the server")

    @On(bot, "playerLeft")
    def on_player_left(this, player):
        if player["username"] == bot.username:
            return
        bot.chat(f"Bye {player['username']}")

    @On(bot, "entitySleep")
    def on_entity_sleep(this, entity):
        bot.chat(f"Good night, {entity.username}")

    @On(bot, "entityWake")
    def on_entity_wake(this, entity):
        bot.chat(f"Good morning, {entity.username}")

    @On(bot, "entityEffect")
    def on_entity_effect(player, this, entity, effect):
        print(f"{player.username} got entityEffect {entity} {effect}")

    @On(bot, "entityEffectEnd")
    def on_entity_effect_end(player, this, entity, effect):
        print(f"{player.username}'s entityEffectEnd {entity} {effect}")

    @On(bot, "entityAttach")
    def on_entity_attach(this, entity, vehicle):
        if entity.type == "player" and vehicle.type == "object":
            print(f"Sweet, {entity.username} is riding the {vehicle.objectType}")

    @On(bot, "entityDetach")
    def on_entity_detach(this, entity, vehicle):
        if entity.type == "player" and vehicle.type == "object":
            print(f"Lame, {entity.username} stopped riding the {vehicle.objectType}")

    @On(bot, "entityHurt")
    def on_entity_hurt(this, entity):
        if entity.type == "mob":
            bot.chat(f"The {entity.mobType} got hurt!")
        elif entity.type == "player":
            if entity.username in bot.players:
                bot.chat(f"Poor {entity.username} got hurt.")

    @On(bot, "chestLidMove")
    def on_chest_lid_move(this, block, isOpen, *args):
        action = "open" if isOpen else "close"
        bot.chat(f"Hey, did someone just {action} a chest?")

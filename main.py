from javascript import require, On 
import time
mineflayer = require("mineflayer")
with open("messages.txt", "r", encoding="UTF-8") as f:
    mmessages = f.read().split("\n")

ip = input("IP: ")
port = input("Port: ")
if port == "":
    port = 25565
username = input("Username: ")

def connect():
    bot = mineflayer.createBot({
        "host": ip,
        "port": port,
        "username": username,
        "auth": "microsoft"
    })

    @On(bot, "spawn")
    def spawn(*args):
        print("Spawned")
        while True:
            for i in mmessages:
                try:
                    bot.chat(i)
                    print("Sent message: " + i)
                    time.sleep(30)
                except:
                    print("Error sending message: " + i)
                    continue

connect()
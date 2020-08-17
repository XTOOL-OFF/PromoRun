from telethon.sync import TelegramClient
import re
import discord
from threading import Thread
import time
import asyncio
from discord.ext import commands, tasks
api_id = 1465388
api_hash = '4bc58026ccd22895e0df4be158a181f1'
timeout = 0.3
name = 'xfx1337'
chat = 'https://t.me/runcsgo'
client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async  def on_ready():
    change_status.start()
    print('bot in active')
print(type(api_hash))
with TelegramClient(name, api_id, api_hash) as clientx:
    first_message = True
    for message in clientx.iter_messages(chat):
        if first_message == True:
            old_message = message.text
            new_message = old_message
            first_message = False
        else:
            pass
    while True:
        time.sleep(timeout)
        first_message = True
        for message in clientx.iter_messages(chat):
            if first_message == True:
                new_message = message.text
                first_message = False
            else:
                pass
        if old_message != new_message:
            print("new!")
            print(new_message)
            old_message = new_message
            @tasks.loop(seconds=0.3)
            async def change_status():
                channel = bot.get_channel(744656917808414800)
                await bot.change_presence(activity=discord.Game('Promo Is Out!'))
                print('test')
                await channel.send(new_message)
                exit()
            bot.run('NzQ0NjYxMjkxMjA5MDY0NTg4.Xzmd3g.lvL_0Z1aNrQ8OtThuWj2hFCj9KI')
        else:
            print("no")
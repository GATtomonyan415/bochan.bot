from os import getenv
import random
import traceback
from discord.ext import commands
bot = commands.Bot(command_prefix="b!",help_command=None)

botyan = ["ボク、ボーちゃんッ！",
"ボッ!!!",
"何か用か？ボッ!!!",
"ボク、ボーちゃんッ！石、大好きッ！ボッ!!!"
]

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention}' f'{botyan}' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@client.event
async def on_message_delete(message):
    channel = client.get_channel(DEBUG_CHANNEL_ID)
    await channel.send(f"{message.author.name}さんのメッセージが削除されました:\n```\n{message.content}\n```")



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)

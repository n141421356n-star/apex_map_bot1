import discord
import datetime
from discord.ext import commands

MAPS = ["ワールズエッジ",
    "イーディス",
    "ストームポイント"]
    

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログイン成功: {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("動いてるよ！")

@bot.command()
async def map(ctx):
    MAPS = [
        "ワールズエッジ",
        "イーディス",
        "ストームポイント"
    ]

    start_time = datetime.datetime(2026, 7, 4, 2, 0, 0)

    now = datetime.datetime.now()

    interval = 4.5 * 60 * 60

    elapsed = (now - start_time).total_seconds()

    index = int(elapsed // interval) % len(MAPS)

    await ctx.send(f"現在のマップは：{MAPS[index]}")

import os
bot.run(os.getenv("DISCORD_TOKEN"))
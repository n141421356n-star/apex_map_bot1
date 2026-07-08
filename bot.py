import discord
import datetime
from discord.ext import commands

@bot.command()
async def map(ctx):
    MAPS = [
        "ワールズエッジ",
        "イーディス",
        "ストームポイント"
    ]

    IMAGE_PATHS = [
        "images/worlds_edge.png",
        "images/e_district.png",
        "images/storm_point.png"
    ]

    JST = datetime.timezone(datetime.timedelta(hours=9))

    start_time = datetime.datetime(2026, 7, 4, 2, 0, 0, tzinfo=JST)
    now = datetime.datetime.now(JST)

    interval = 4.5 * 60 * 60

    elapsed = (now - start_time).total_seconds()

    index = int(elapsed // interval) % len(MAPS)

    await ctx.send(
        f"現在のマップは：{MAPS[index]}",
        file=discord.File(IMAGE_PATHS[index])
    )
import os
bot.run(os.getenv("DISCORD_TOKEN"))
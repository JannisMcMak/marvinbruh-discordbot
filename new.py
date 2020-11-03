from discord.ext import commands
import asyncio
import discord
import sys
import pyttsx3
import random
import os

TOKEN = "NzY0ODg3MDIzNTA0MzI2NjY4.X4MyjQ.kcP1iLzAxz4j8P4X2gF0eBtuBEI"

DIR = os.path.dirname(os.path.abspath(__file__))

bot = commands.Bot(command_prefix='#', case_insensitive=True)
bot.remove_command('help')


count = 0
limit = 10

user = []
last_msg = None


@bot.event
async def on_ready():
    print("Loading...")
    print(f'{bot.user} has connected to Discord!')
    print(DIR)


def create_Embed(ctx):
    global count
    global limit
    global user

    embed = discord.Embed(
        title="AmongUs Request",
        description=f"{ctx.author.mention} möchte gerne AmongUs spielen! '#join' um teilzunehmen <@&759398942893932544>",
        color=discord.Color.blue()
    )
    embed.add_field(name="Teilnehmer", value=count, inline=True)
    embed.add_field(name="Limit", value=limit, inline=True)
    if len(user) > 0:
        teilnehmer = ', '.join(user)
        embed.add_field(name="Teilnehmer", value=teilnehmer, inline=False)

    return embed


async def update(ctx):
    global last_msg

    await last_msg.edit(embed=create_Embed(ctx))


@bot.command()
async def request(ctx, aliases=['req', 'r']):
    global last_msg
    global user
    global count

    count = 1
    msg = await ctx.send(embed=create_Embed(ctx))
    last_msg = msg
    await update(ctx)
    user.append(ctx.author.mention)


@bot.command()
async def join(ctx, aliases=['accept', 'j', 'y']):
    global count
    global user

    user.append(ctx.author.mention)
    count = count + 1
    await update(ctx)


@bot.command()
async def reset(ctx):
    global count
    global limit
    global last_msg
    global user


    await last_msg.delete()
    last_msg = None
    count = 0
    user = []
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=""))


@bot.command()
async def limit(ctx, arg1: int):
    global limit

    limit = arg1
    await update(ctx)


@bot.command()
async def code(ctx, arg1: str):
    if 4 <= len(arg1) <= 6:
        await ctx.send("AmongUs Code: {}".format(arg1))
        await bot.change_presence(activity=discord.Game(name="AmongUs Code: {}".format(arg1)))

        engine = pyttsx3.init()
        filename = 'cache/{}_{}.mp3'.format(arg1, random.randint(0, 10000))
        engine.save_to_file('Der Among Us Code ist {}'.format(arg1), filename)
        engine.runAndWait()

        channel = ctx.author.voice.channel
        vc = await channel.connect()
        # vc.play(discord.FFmpegPCMAudio(executable='c:/users/jannis/desktop/coding/projects/amongus/requestbot/ffmpeg/bin/ffmpeg.exe',
        #                               source='c:/users/jannis/desktop/coding/projects/amongus/requestbot/{}'.format(filename)))
        vc.play(discord.FFmpegPCMAudio(executable=os.path.join(DIR, 'ffmpeg/bin/ffmpeg.exe'), source=filename))

        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()

        os.remove(filename)



@bot.command()
async def bruh(ctx):
    if not ctx.author.name.startswith('Professor'):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        # vc.play(discord.FFmpegPCMAudio(executable='c:/users/jannis/desktop/coding/projects/amongus/requestbot/ffmpeg/bin/ffmpeg.exe',
        #                               source="c:/users/jannis/desktop/coding/projects/amongus/requestbot/audio.mp3"))
        vc.play(discord.FFmpegPCMAudio(executable=os.path.join(DIR, 'ffmpeg/bin/ffmpeg.exe'), source='audio.mp3'))

        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
    else:
        ctx.send("Shut up")


@bot.command()
async def justus(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    # vc.play(discord.FFmpegPCMAudio(executable='c:/users/jannis/desktop/coding/projects/amongus/requestbot/ffmpeg/bin/ffmpeg.exe',
    #                               source='c:/users/jannis/desktop/coding/projects/amongus/requestbot/justus.mp3'))
    vc.play(discord.FFmpegPCMAudio(executable=os.path.join(DIR, 'ffmpeg/bin/ffmpeg.exe'), source='justus.mp3'))

    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()


@bot.command()
async def jost(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    # vc.play(discord.FFmpegPCMAudio(executable='c:/users/jannis/desktop/coding/projects/amongus/requestbot/ffmpeg/bin/ffmpeg.exe',
    #                               source='c:/users/jannis/desktop/coding/projects/amongus/requestbot/jost.mp3'))
    vc.play(discord.FFmpegPCMAudio(executable=os.path.join(DIR, 'ffmpeg/bin/ffmpeg.exe'), source='jost.mp3'))

    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()


@bot.command()
async def versuh(ctx, text):
    print(ctx.author.name)
    engine = pyttsx3.init()
    filename = 'cache/{}_{}.mp3'.format(text, random.randint(0, 10000))
    engine.save_to_file(text, filename)
    engine.runAndWait()

    channel = ctx.author.voice.channel
    if not ctx.author.name == 'DetlefJoost':
        vc = await channel.connect()
        # vc.play(discord.FFmpegPCMAudio(executable='c:/users/jannis/desktop/coding/projects/amongus/requestbot/ffmpeg/bin/ffmpeg.exe',
        #                               source='c:/users/jannis/desktop/coding/projects/amongus/requestbot/{}'.format(filename)))
        vc.play(discord.FFmpegPCMAudio(executable=os.path.join(DIR, 'ffmpeg/bin/ffmpeg.exe'), source=filename))
    else:
        vc = await channel.connect()
        # vc.play(discord.FFmpegPCMAudio(executable='c:/users/jannis/desktop/coding/projects/amongus/requestbot/ffmpeg/bin/ffmpeg.exe',
        #                               source='c:/users/jannis/desktop/coding/projects/amongus/requestbot/jost.mp3'))
        vc.play(discord.FFmpegPCMAudio(executable=os.path.join(DIR, 'ffmpeg/bin/ffmpeg.exe'), source='jost.mp3'))

    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()

    os.remove(filename)


@bot.command()
async def exit(ctx):
    sys.exit(0)


@bot.command()
async def ping(ctx):
    await ctx.send("<@&759398942893932544>")


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        color=discord.Color.gold()
    )

    embed.set_author(name='Help für dumme Leute (Jost)')
    embed.add_field(name='#request', value='AmongUs Lobby requesten', inline=False)
    embed.add_field(name='#code', value='Set AmongUs Game Code (höchstens 6 Zeichen) + TTS', inline=False)
    embed.add_field(name='#versuh <text>', value='TTS', inline=False)

    await ctx.send(embed=embed)



bot.run(TOKEN)

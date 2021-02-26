import main
from discord.ext import commands
import asyncio
import discord
import os
import time
import requests
from text import bitchass, poetry, count, get_counters
from twitchtts import write_mp3_twitch, write_mp3_twitch_fromtext
from mutagen.mp3 import MP3


intents = discord.Intents.default()
intents.members = True

TOKEN = os.getenv('TOKEN')

DIR = os.path.dirname(os.path.abspath(__file__))

bot = commands.Bot(command_prefix='#', case_insensitive=True, intents=intents)


#bot.help_command = PrettyHelp()
#bot.remove_command('help')
async def write_mp3(text):
    text = ' '.join(text)
    print(text)
    de = 'http://api.voicerss.org/?key=16d017cd4d194a22b199c5739bd6ab42&hl=de-de&v=Jonas&src={}'
    r = requests.get(de.format(text))
    filename = 'cache/{}.mp3'.format(time.time())
    open(filename, 'wb').write(r.content)
    return filename


async def write_mp3eng(text):
    text = ' '.join(text)
    print(text)
    eng = 'http://api.voicerss.org/?key=16d017cd4d194a22b199c5739bd6ab42&hl=en-us&v=Mike&src={}'
    r = requests.get(eng.format(text))
    filename = 'cache/{}.mp3'.format(time.time())
    open(filename, 'wb').write(r.content)
    return filename


async def write_mp3ind(text):
    text = ' '.join(text)
    print(text)
    eng = 'http://api.voicerss.org/?key=16d017cd4d194a22b199c5739bd6ab42&hl=en-in&v=Ajit&src={}'
    r = requests.get(eng.format(text))
    filename = 'cache/{}.mp3'.format(time.time())
    open(filename, 'wb').write(r.content)
    return filename


@bot.event
async def on_command_error(ctx, error):
    print('Error!')
    print(error)
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Argument error')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found')
    elif 'Already connected to a voice channel' in str(error):
        await ctx.send('Wait')
    elif 'object has no attribute \'channel\'' in str(error):
        await ctx.send('Get a room')
    else:
        print('else')


@bot.event
async def on_ready():
    print("Loading...")
    print(f'{bot.user} has connected to Discord!')
    print(DIR)

    botcmd = bot.get_channel(473788466858164245)

    msg = await botcmd.fetch_message(811177327295594546)    

    global context_object
    context_object = await bot.get_context(msg)


@bot.event
async def on_member_update(before, after):
    if before.status != after.status:
      print(after.status)

@bot.command(help='Displays AmongUs code')
async def code(ctx, code: str):
    if 4 <= len(code) <= 6:
        await ctx.send("AmongUs Code: {}".format(code))
        await bot.change_presence(
            activity=discord.Game(name="Code: {}".format(code)))

        filename = await write_mp3(code)

        channel = ctx.author.voice.channel
        vc = await channel.connect()

        vc.play(discord.FFmpegPCMAudio(executable='./ffmpeg', source=filename))

        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()

        os.remove(filename)


@bot.command()
async def bruh(ctx):
    if not ctx.author.name.startswith('Professor'):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        print("Bruh", ctx.author.name)

        vc.play(
            discord.FFmpegPCMAudio(
                executable='./ffmpeg', source='mp3s/audio.mp3'))

        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
    else:
        ctx.send("Shut up")

    await count('mp3s')


@bot.command(help='Play mp3')
async def play(ctx, name: str, c=None):
  global context_object
  context_object = ctx
  if name == 'list':
    mp3s = os.listdir("./mp3s")

    embed=discord.Embed(title="Mp3s", color=0x01cdfe)

    for mp3 in mp3s:
      name = mp3.split('.') 
      try:
        audio = MP3('./mp3s/'+ name[0] + '.mp3')
        le = time.strftime('%M:%S', time.gmtime(audio.info.length))
        embed.add_field(name=name[0], value=le, inline=True)
      except Exception:
        print('Error')

    
    await ctx.send(embed=embed)

  else:
    print('Mp3: ' + name)
    filename = 'mp3s/' + name + '.mp3'

    if c is None:
        channel = ctx.author.voice.channel
    else:
        channel = c
    vc = await channel.connect()

    try:
      vc.play(discord.FFmpegPCMAudio(executable='./ffmpeg', source=filename))
    except:
      await ctx.send('No Mp3 found')

    while vc.is_playing():
      await asyncio.sleep(1)
    await vc.disconnect()


    await count('mp3s')



@bot.command(help='TTS German')
async def versuh(ctx, *text, c=None):
    print(text)
    jost = 'DetlefJoost'
    print(ctx.author.name)
    filename = await write_mp3(text)
    try:
        if c is None:
          channel = ctx.author.voice.channel
        else:
          channel = c
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source=filename))

        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
    except discord.errors.ClientException:
        await ctx.send('Warte du Hurensohn ')
    os.remove(filename)

    await count('versuh')


@bot.command(help='TTS English')
async def versuhe(ctx, *text, c=None):
    print(text)
    jost = 'DetlefJoost'
    print(ctx.author.name)
    filename = await write_mp3eng(text)
    try:
        if c is None:
          channel = ctx.author.voice.channel
        else:
          channel = c
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source=filename))
        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()

    except discord.errors.ClientException:
        await ctx.send('Wait ffs')

    os.remove(filename)

    await count('versuh')


@bot.command(help='TTS Indian')
async def versuhi(ctx, *text, c=None):
    print(text)
    jost = 'DetlefJoost'
    print(ctx.author.name)
    filename = await write_mp3ind(text)
    try:
        if c is None:
          channel = ctx.author.voice.channel
        else:
          channel = c
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source=filename))
        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()

    except discord.errors.ClientException:
        await ctx.send('Wait ffs')

    os.remove(filename)

    await count('versuh')

@bot.command(help='Twitch TTS')
async def versuht(ctx, *text, c=None):
    print(text)
    print(ctx.author.name)
    filename = await write_mp3_twitch(text)
    if filename != None:
      try:
          if c is None:
            channel = ctx.author.voice.channel
          else:
            channel = c
          vc = await channel.connect()
          vc.play(discord.FFmpegPCMAudio(source=filename))
          while vc.is_playing():
              await asyncio.sleep(1)
          await vc.disconnect()

      except discord.errors.ClientException:
          await ctx.send('Wait ffs')

      os.remove(filename)
    else: 
      await ctx.send('Too long')
    
    await count('versuh')


@bot.command(help='Bitch voice line')
async def bitch(ctx, name, level: int = 0, c=None):
    print(name)
    print(ctx.author)
    i = level
    print(i)

    if name:
        base_line = await bitchass(i)
        text = base_line.format(name, name, name, name)
        print(text)
        filename = await write_mp3eng_fromtext(text)

        try:
            if c is None:
              channel = ctx.author.voice.channel
            else:
              channel = c

            vc = await channel.connect()

            vc.play(discord.FFmpegPCMAudio(source=filename))

            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()

        except discord.errors.ClientException:
            await ctx.send('Wait ffs')

        os.remove(filename)
    else:
        await ctx.send('Argument error')

    await count('bitch')

@bot.command(help='Bitch voice line (Twitch TTS)')
async def bitcht(ctx, name, level: int = 0, c=None):
    print(name)
    print(ctx.author)
    i = level
    print(i)

    if name:
        base_line = await bitchass(i)
        text = base_line.format(name, name, name, name)
        print(text)
        filename = await write_mp3_twitch_fromtext(text)
        if filename != None:
          try:
              if c is None:
                channel = ctx.author.voice.channel
              else:
                channel = c

              vc = await channel.connect()

              vc.play(discord.FFmpegPCMAudio(source=filename))

              while vc.is_playing():
                  await asyncio.sleep(1)
              await vc.disconnect()

          except discord.errors.ClientException:
              await ctx.send('Wait ffs')

          os.remove(filename)
        else:
          await ctx.send('Too long')
    else:
        await ctx.send('Argument error')
    await count('bitch')


@bot.command(help='Gedichte von Dichtern')
async def gedicht(ctx, i: int = 0):
    print('Gedicht')
        
    text = await poetry(i)
    filename = await write_mp3de_fromtext(text)

    try:
        channel = ctx.author.voice.channel

        vc = await channel.connect()

        vc.play(discord.FFmpegPCMAudio(source=filename))

        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()

    except discord.errors.ClientException:
        await ctx.send('Wait ffs')

    os.remove(filename)

    await count('gedicht')


async def write_mp3eng_fromtext(text):
    print(text)
    eng = 'http://api.voicerss.org/?key=16d017cd4d194a22b199c5739bd6ab42&hl=en-us&v=Mike&src={}'
    r = requests.get(eng.format(text))
    filename = 'cache/{}.mp3'.format(time.time())
    open(filename, 'wb').write(r.content)
    return filename


async def write_mp3de_fromtext(text):
    print(text)
    eng = 'http://api.voicerss.org/?key=16d017cd4d194a22b199c5739bd6ab42&hl=de-de&v=Jonas&src={}'
    r = requests.get(eng.format(text))
    filename = 'cache/{}.mp3'.format(time.time())
    open(filename, 'wb').write(r.content)
    return filename


@bot.command(help='Selfdestruct')
async def exit(ctx):
    #g = ctx.message.guild
    #await g.leave()
    await ctx.author.kick()


@bot.command(help='Selfdestruct 2.0 (try it)')
async def selfdestruct(ctx):
    await ctx.author.kick()


@bot.command(help='Command usage counter')
async def counter(ctx):
  counters, values = await get_counters()
  
  embed=discord.Embed(title="COMMAND COUNTER", url="https://marvinbruh-dashboard.jannismcmak.repl.co", color=0x01cdfe)

  for counter in counters:
    embed.add_field(name=counter, value=values[counters.index(counter)], inline=True)

  await ctx.send(embed=embed)


@bot.command()
async def save(ctx):
  global context_object
  context_object = ctx


def get_channel(user_id):
  print(user_id)
  guilds = bot.guilds
  memeteam = None
  for guild in guilds:
    if guild.name == "Meme Team":
      memeteam = guild
      break

  id = None
  try:
    id = int(user_id)
  except:
    print('None')
  

  member = memeteam.get_member(id)

  try:
    channel = member.voice.channel
  except AttributeError:
    return None

  return channel

def get_voice_channels():
  guilds = bot.guilds
  memeteam = None
  for guild in guilds:
    if guild.name == "Meme Team":
      memeteam = guild
      break

  channels = memeteam.voice_channels

  return channels

async def tts(user_id, lang, text, level, i):
  channel = None
  i = int(i)
  if i == 0:  
    channel = get_channel(user_id)
  else:
    channels = get_voice_channels()
    channel = channels[i - 1]

  global context_object

  if level is None: 
    await context_object.invoke(bot.get_command(lang), text, c=channel)
  else:
    print(level)
    await context_object.invoke(bot.get_command(lang), text, level=int(level), c=channel)
  
async def mp3(user_id, name, i):
  channel = None
  i = int(i)
  if i == 0:  
    channel = get_channel(user_id)
  else:
    channels = get_voice_channels()
    channel = channels[i - 1]

  global context_object
  await context_object.invoke(bot.get_command('play'), name, c=channel)





def run_bot():
  bot.run(TOKEN)



bot.loop.create_task(main.server.run())
bot.run(TOKEN)



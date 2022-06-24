import discord
from discord.ext import commands
#made with <3 by Lushketchup8624
'''
README
the server_name, channel_name and token_number are to be replaced by the corresponding element. example: for token_number, replace it by your bot token.
'''
bot = commands.Bot(command_prefix="§") #indicates the prefix of the bot commands

@bot.event
async def on_ready():
    activity = discord.Game(name="§help")
    await bot.change_presence(activity=activity)
    print("Softwarebot' is now connected")
    print("Initializing bot log console...")
    print("--------------------------------------------------\n")


#commands
@bot.command(name="info", description="displays the bots's information") #indicates the name of the command and its description (the description displayed by the help command is the one commented out between async def and await
async def info(ctx):
    '''displays the bots's information'''
    await ctx.send('**`SoftwareBot version 1.3 made by Lushketchup8624, coded in python3,  discord server server_name | View code on github:`** https://github.com/Malwprotector/Softwarebot') #text that is sent by the bot

@bot.command(name="hello", description="answers hello")
async def hello(ctx):
    '''answers hello'''
    await ctx.send("**`Bonjour, comment vas-tu?`**")

@bot.command(name="add", description="add two numbers")
async def add(ctx, left: int, right: int):
    '''add two numbers'''
    await ctx.send(left + right)

@bot.command(name="ping", description="PoNg")
async def ping(ctx):
    '''PoNg'''
    await ctx.send("**`pong`**", delete_after=2)

@bot.command(name="github", description="show my github page")
async def github(ctx):
    '''show my github page:)'''
    await ctx.send("https://github.com/Malwprotector/Softwarebot")

@bot.command(name="hacking-definition", description="gives a definition of hacking, according to the server.")
async def hello(ctx):
    '''gives a definition of hacking, according to the server.'''
    await ctx.send("> ***hacking is the act of doing advanced computer science, a hacker is a hacker who seeks to understand the workings of different areas of computer science, there is absolutely no illegal intent through this term, hackers may perform illegal acts but that is not the definition.***")

@bot.command(name=":>", description=":>")
async def emoji_1(ctx):
    ''':>'''
    await ctx.send("**`:>`**")

@bot.command(name=":)", description=":)")
async def emoji_2(ctx):
    ''':)'''
    await ctx.send("**`:)`**")

@bot.command(name="^^", description="^^")
async def emoji_3(ctx):
    await ctx.send("**`^^`**")

@bot.command(name="spoil", description="spoiler")
async def spoil(ctx, arg):
    '''warns that the message potentially contains spoil'''
    await ctx.send(" \n **Warning, the message below contains spoilers!**", delete_after=5) #indicates that the message should be deleted after a certain number of seconds
    await ctx.send(arg, delete_after=2)

@bot.command(name="auto-answer", description="auto-answer")
async def auto_answser(ctx, arg):
    await ctx.send(arg)

@bot.command(name="warn", description="warn")
async def warn(ctx):
    await ctx.send("**`⚠️Attention, vous venez de reçevoir un avertissement.⚠️`**", delete_after=10)

@bot.command(name="quoi", description="feur")
async def auto_andwser(ctx):
    '''feur'''
    await ctx.send("**`FeUr`**")

#new_member
async def on_member_join(member):
       general_channel = client.get_channel(channel_name)
       general_channel.send(f"Bienvenue sur {guild.name} {member.display_name} !")

bot.run("token_number") #token of the bot, you can find it on discord developer platform.

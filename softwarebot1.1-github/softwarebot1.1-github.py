import discord
#made with <3 by Lushketchup8624
'''
README
the channel_name and token_number are to be replaced by the corresponding element. example: for token_number, replace it by your bot token.
'''
client = discord.Client()

@client.event
async def on_ready():
	print("Softwarebot' is now connected.")

@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong", delete_after=2)


@client.event
async def on_member_join(member):
	general_channel: discord.TextChannel = client.get_channel(channel_name)
	await general_channel.send(content=f"Bienvenue {member.display_name} !")






client.run("token_number")
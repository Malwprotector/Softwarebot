import discord
#made with <3 by Lushketchup8624
'''
README
the server_name, channel_name and token_number are to be replaced by the corresponding element. example: for token_number, replace it by your bot token.
'''
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('SoftwareBot is now connected.')


#command
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('§hello'):
            await message.channel.send('**`Hello`** {0.author.mention}'.format(message))
        if message.content.startswith('§help'):
            await message.channel.send('{0.author.mention}, \n  `SoftwareBot version 0.5 made by Lushketchup8624, coded in python3,  discord server server_name` \n **`voici les principales commandes du serveur:`** \n **`Préfixe: § `** \n **`§help: afficher les informations sur le bot et les commandes`** \n **`§ping: obtenir une réponse par pong.`** \n **`§hello: obtenir une réponse par bonjour.`**'.format(message))
        if message.content.startswith('§ping'):
            await message.channel.send(' {0.author.mention}**`pong`** '.format(message))
    #admin_command
        if message.content.startswith('§adminpass: admin §help'):
            await message.channel.send('{0.author.mention}, \n  `SoftwareBot version 0.5 made by Lushketchup8624, coded in python3,  discord server xxxxxxxxxx` \n **`voici les principales commandes du serveur:`** \n **`Préfixe: § `** \n **`§sent_general: envoyer un message dans annoncements.`** \n **`§sent_french: envoyer un message dans french.`** \n **`§sent_polish: envoyer un message dans polish.`** \n **`§warn: envoyer un message d avertissement dans général.`** \n **`§:>: envoyer :> dans général.`** \n **`§:): envoyer :) dans général.`** \n **`§^^: envoyer ^^ dans général.`** \n  **`§help: afficher les informations sur le bot et les commandes`** \n **`§ping: obtenir une réponse par pong.`** \n **`§hello: obtenir une réponse par bonjour.`**'.format(message))
    #annoncements
    #general
        if message.content.startswith('§sent_general'):
            general_channel = client.get_channel(channel_name)
            await message.channel.send('**`content_annoncement`** '.format(message))
    #french
        if message.content.startswith('§sent_french'):
            general_channel = client.get_channel(channel_name)
            await message.channel.send('**`content_annoncement`** '.format(message))
    #polish
        if message.content.startswith('§sent_polish'):
            general_channel = client.get_channel(channel_name)
            await message.channel.send('**`content_annoncement`** '.format(message))
    #serveur_particulier
        if message.content.startswith('§:>'):
            general_channel = client.get_channel(channel_name)
            await message.channel.send('**`:>`** '.format(message))
        if message.content.startswith('§:)'):
            general_channel = client.get_channel(channel_name)
            await message.channel.send('**`:)`** '.format(message))
        if message.content.startswith('§^^'):
            general_channel = client.get_channel(channel_name)
            await message.channel.send('**`^^`** '.format(message))
    #réponse_du_bot
        if message.content.startswith('§warn'):
            general_channel = client.get_channel(channel_name)
            await message.channel.send('**`Merci de bien vouloir respecter le règlement.`** '.format(message))
        if message.content.startswith('softwarebot'):
            await message.channel.send(' {0.author.mention} **`<3`** '.format(message))


    

#new_member
    async def on_member_join(member):
       general_channel = client.get_channel(channel_name)
       general_channel.send(f"Bienvenue sur {guild.name} {member.display_name} !")





client = MyClient()
client.run('token_number')

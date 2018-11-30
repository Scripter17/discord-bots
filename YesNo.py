# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=497561729048510465&scope=bot
import discord
import re
import os
import log

client=discord.Client()
@client.event
async def on_message(message):
	if message.author==client.user:
		return
	AID=message.author.id
	ANAME=message.author.name
	MESSAGE=message.content.lower()
	if MESSAGE=="yn/help":
		await client.send_message(message.channel, "`yn/yes => yesyesyes.jpg`\n`yn/no => nonono.jpg`")
		log.log("(yn) %s (%s) asked for help"%(AID, ANAME))
	if MESSAGE=="yn/yes":
		await client.send_file(message.channel, r"assets/yn-bot-yesyesyes.jpg")
		log.log("(yn) %s (%s) said yes"%(AID, ANAME))
	if MESSAGE=="yn/no":
		await client.send_file(message.channel, r"assets/yn-bot-nonono.jpg")
		log.log("(yn) %s (%s) said no"%(AID, ANAME))
@client.event
async def on_ready():
	print('YesNo bot is ready! (%s | %s)'%(client.user.id, client.user.name))


client.run(os.environ["ynbottoken"])

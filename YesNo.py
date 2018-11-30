# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=497561729048510465&scope=bot
import discord
import re
import os

client=discord.Client()
@client.event
async def on_message(message):
	if message.author==client.user:
		return
	if message.content.lower()=="yn/help":
		await client.send_message(message.channel, "`yn/yes => yesyesyes.jpg`\n`yn/no => nonono.jpg`")
	if message.content.lower()=="yn/yes":
		await client.send_file(message.channel, r"assets\yn-bot-yesyesyes.jpg")
	if message.content.lower()=="yn/no":
		await client.send_file(message.channel, r"assets\yn-bot-nonono.jpg")
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(os.environ["ynbottoken"])
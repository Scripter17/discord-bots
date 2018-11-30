# https://www.devdungeon.com/content/make-discord-bot-python
import discord
import random
import time
import re
import os
TOKEN=os.environ["rbottoke"]
client=discord.Client()
whymsg=["I have absolutely no idea.", "Why not?", "¯\_(ツ)_/¯", "Because one of my friends told me to."]
ownerUID="335554170222542851"
timeFormat="%Y-%m-%d %H:%M:%S (GMT%z)"
class functions:
	async def help(client, message):
		await client.send_message(message.channel, \
"""Literally just type 'RERO' (case insensitive) anywhere and I will reply to you
If you don't get the meme, watch JoJo's Bizarre Adventure Part 3 episode 9.
Commands: `r/help`, `r/why`, `r/explain`, and `r/invite`.
Secret Commands: The fact that there are secret commands is the only hint you're getting.""")
	async def why(client, message):
		await client.send_message(message.channel, random.choice(whymsg))
	async def invite(client, message):
		await client.send_message(message.channel, "https://discordapp.com/oauth2/authorize?client_id=485540685965950978&scope=bot")
	async def explain(client, message):
		await client.send_file(message.channel, r"rero-bot-explain.jpg")
	async def egg(client, message):
		await client.send_file(message.channel, r"rero-bot-egg.jpg")
	async def scream(client, message):
		await client.send_file(message.channel, r"rero-bot-scream.jpg")
funcmap={
	"r/help":functions.help,
	"r/why":functions.why,
	"r/invite":functions.invite,
	"r/egg":functions.egg,
	"r/scream":functions.scream,
	"r/explain":functions.explain
}
@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author==client.user:
		return
	if "rero" in message.content.lower():
		print("[%s] %s (%s) Rero'd"%(time.strftime(timeFormat), message.author.id, message.author.name))
		msg="RERO RERO RERO RERO RERO RERO RERO RERO"
		if "reor" in message.content.lower():
			msg+="\n Also, it's \"RERO\", idiot"
			print("[%s] %s (%s) Also Reor'd"%(time.strftime(timeFormat), message.author.id, message.author.name))
		await client.send_message(message.channel, msg)
	elif "reor" in message.content.lower():
		print("[%s] %s (%s) Reor'd"%(time.strftime(timeFormat), message.author.id, message.author.name))
		await client.send_message(message.channel, "It's \"RERO\", idiot.")
	elif message.content.lower() in funcmap.keys():
		print("[%s] %s (%s) %s"%(time.strftime(timeFormat), message.author.id, message.author.name, message.content.lower()))
		await funcmap[message.content.lower()](client, message)
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
client.run(TOKEN)
# https://www.devdungeon.com/content/make-discord-bot-python
import discord
import random
import re
import os
import log
client=discord.Client()
whymsg=["I have absolutely no idea.", "Why not?", "¯\_(ツ)_/¯", "Because one of my friends told me to."]
ownerUID="335554170222542851"
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
		await client.send_file(message.channel, r"assets/rero-bot-explain.jpg")
	async def egg(client, message):
		await client.send_file(message.channel, r"assets/rero-bot-egg.jpg")
	async def scream(client, message):
		await client.send_file(message.channel, r"assets/rero-bot-scream.jpg")
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
	AID=message.author.id
	ANAME=message.author.name
	MESSAGE=message.content.lower()
	if "rero" in MESSAGE:
		log.log("(rero) %s (%s) Rero'd"%(AID, ANAME))
		msg="RERO RERO RERO RERO RERO RERO RERO RERO"
		if "reor" in MESSAGE:
			msg+="\n Also, it's \"RERO\", idiot"
			log.log("(rero) %s (%s) Also Reor'd"%(AID, ANAME))
		await client.send_message(message.channel, msg)
	elif "reor" in MESSAGE:
		log.log("(rero) %s (%s) Reor'd"%(AID, ANAME))
		await client.send_message(message.channel, "It's \"RERO\", idiot.")
	elif MESSAGE in funcmap.keys():
		log.log("(rero) %s (%s) %s"%(AID, ANAME, MESSAGE))
		await funcmap[MESSAGE](client, message)
@client.event
async def on_ready():
	print('Rero bot is ready! (%s | %s)'%(client.user.id, client.user.name))

client.run(os.environ["rbottoken"])

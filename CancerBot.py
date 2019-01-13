# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=508384658166382593&scope=bot
import discord
import cowsaygen
import sys
import re
import os
import log
import time
client=discord.Client()
jacksonGBT=0
@client.event
async def on_message(message):
	if message.author==client.user:
		return
	AID=message.author.id
	ANAME=message.author.name
	MESSAGE=message.content.lower()
	#log.log(str(AID)+MESSAGE)
	if AID=="182962569147973633" and "https://tenor.com/view/" in MESSAGE: # Make Jackson able to use tenor, but not spam with it.
		log.log("(cancer) Jackson used GIF")
		if time.time()-jacksonGBT<20:
			await client.delete_message(message)
			await client.send_message(message.channel, "Cooldown remaining: "+str(int(time.time()-jacksonGBT))+" seconds.")
			log.log("(cancer) It's not very effective")
	if "ooof" in MESSAGE or re.match("\\bo+og\\b", MESSAGE):
		await client.send_message(message.channel, "IT'S \"OOF\" YOU FUCKING MORON")
		log.log("(cancer) %s (%s) is a moron"%(AID, ANAME))
	if message.mention_everyone:
		await client.send_message(message.channel, "Stop it with `@everyone`, you marrowey clog.")
		log.log("(cancer) %s (%s) pinged everyone"%(AID, ANAME))
	if MESSAGE[0:10]=="oof/cowsay":
		say=message.content[11:]
		if say[0]=="\n": say=say[1:]
		say=say.replace("\n","\\n")
		await client.send_message(message.channel, "```"+cowsaygen.cowsaygen(say)+"```")
		log.log("(cancer) %s (%s) cowsayed %s"%(AID, ANAME, say))
	robotRacism=re.match("((beep|boop|bop|bz+t) ?)+", MESSAGE)
	if robotRacism!=None:
		await client.send_message(message.channel, ">"+robotRacism[0]+"\nTHAT'S RACIST TOWARDS ROBOTS")
		log.log("(cancer) %s (%s) is racist towards robots"%(AID, ANAME))
@client.event
async def on_ready():
	print('Cancerbot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["cbottoken"])

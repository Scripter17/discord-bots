# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=508384658166382593&scope=bot
import discord
import cowsaygen
import sys
import re
import os
sys.path.insert(0, r'C:\Users\James Wise\AppData\Roaming\WinPythonZero\python-3.6.6.amd64')
TOKEN=os.environ["cbottoken"]
client=discord.Client()
@client.event
async def on_message(message):
	if message.author==client.user:
		return
	if "ooof" in message.content.lower():
		await client.send_message(message.channel, "IT'S \"OOF\" YOU FUCKING MORON")
	if message.mention_everyone:
		await client.send_message(message.channel, "Stop it with `@everyone`, you marrowey clog.")
	if message.content.lower()[0:10]=="oof/cowsay":
		say=message.content.lower()[11:]
		if say[0]=="\n": say=say[1:]
		say=say.replace("\n","\\n")
		await client.send_message(message.channel, "```"+cowsaygen.cowsaygen(say)+"```")
	robotRacism=re.match("((beep|boop|bop|bz+t) ?)+",message.content.lower())
	if robotRacism!=None:
		await client.send_message(message.channel, ">"+robotRacism[0]+"\nTHAT'S RACIST TOWARDS ROBOTS")
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
client.run(TOKEN)
# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=508384658166382593&scope=bot
import discord, cowsaygen, sys, re, os, time
from currency_converter import CurrencyConverter
sys.path.append("..")
import globalTools

cConv=CurrencyConverter()
client=discord.Client()
class __:
	class cooldowns:
		jacksonGBT=0
		fuckoff=0
	prefix="$"

class functions:
	async def runIfJackson(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		global cooldown # Global warming fixed!
		if "https://tenor.com/view/" in content: # Make Jackson able to use tenor, but not spam with it.
			#print("Jackson: "+"\n\t".join(MESSAGE.split("\n"))
			globalTools.log("(cancer) Jackson used GIF")
			if time.time()-cooldowns.jacksonGBT<20:
				await client.delete_message(message)
				if time.time()-cooldowns.fuckoff>=20:
					await client.send_message(message.channel, "Cooldown remaining: "+str(20-int(time.time()-cooldowns.jacksonGBT))+" seconds.")
				globalTools.log("(cancer) It's not very effective")
				cooldowns.fuckoff=time.time()
			else:
				cooldowns.jacksonGBT=time.time()
		if ":woke:" in content or ":iamaloser:" in content:
			await client.delete_message(message)
			if time.time()-cooldowns.fuckoff>=20:
				await client.send_message(message.channel, "Fuck off with that shit")
			globalTools.log("(cancer) Jackson can fuck off with that shit")
			cooldowns.fuckoff=time.time()
	
	async def ooof(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		await client.send_message(message.channel, "IT'S \"OOF\" YOU FUCKING MORON")
		globalTools.log("(cancer) %s (%s) is a moron"%(authorId, authorName))
	
	async def conv(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.upper() # Currency names have to be in uppercase
		args=content[len(__.prefix)+5:].split(" ")
		print(args)
		try:
			args[0]=float(args[0])
		except:
			await client.send_message(message.channel, "You gotta make the first argument just a number, don't put $, €, or whatever before/after it")
			return None
		await client.send_message(message.channel, "%0.02f %s = %0.02f %s"%(args[0], args[1], cConv.convert(args[0], args[1], args[2]), args[2]))
	
	async def cowsay(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		say=message.content[len(__.prefix)+7:]
		if say[0]=="\n": say=say[1:]
		say=say.replace("\n","\\n")
		await client.send_message(message.channel, "```"+cowsaygen.cowsaygen(say)+"```")
		globalTools.log("(cancer) %s (%s) cowsayed %s"%(authorId, authorName, say))
	
	async def atEveryone(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		await client.send_message(message.channel, "Stop it with `@everyone`, you marrowey clog.")
		globalTools.log("(cancer) %s (%s) pinged everyone"%(authorId, authorName))
	
	async def robotRacism(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		robotRacism=re.match("((beep|boop|bop|bz+t) ?)+", content)
		if robotRacism!=None:
			await client.send_message(message.channel, ">"+robotRacism[0]+"\nTHAT'S RACIST TOWARDS ROBOTS")
			globalTools.log("(cancer) %s (%s) is racist towards robots"%(authorId, authorName))

funcMap={
	"conv": functions.conv,
	"cowsay": functions.cowsay
}

@client.event
async def on_message(message):
	if message.author==client.user:
		return
	if message.author!=os.environ["James"] and os.environ["test"]=="true": return
	authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
	
	funcName=globalTools.getFunc(__.prefix, content)
	if funcName in funcMap.keys(): await funcMap[funcName](message)
	
	if authorId==os.environ["Jackson"]: await functions.runIfJackson(message)
	if re.match("\\bo+o[gf]\\b", content): await functions.ooof(message)
	if message.mention_everyone: await functions.atEveryone(message)
	await functions.robotRacism(message)

@client.event
async def on_ready():
	print('Cancerbot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["cbottoken"])

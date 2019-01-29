# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=517772410565558295&scope=bot
import discord, os, sys
sys.path.append("..")
import globalTools

class __:
	prefix="$"
	zombie=lambda:discord.utils.get(message.server.roles, name="Zombie")
	vampire=lambda:discord.utils.get(message.server.roles, name="Vampire")

class functions:
	async def vampire(message):
		await client.remove_roles(user, zombie())
		await client.add_roles(user, vampire())
		await client.send_message(message.channel, "Role updated to vampire for "+message.author.mention)
		log.log("(DIO) %s (%s) is now a vampire"%(message.author.id, message.author.name))
	async def zombie(message):
		await client.remove_roles(user, vampire())
		await client.add_roles(user, zombie())
		await client.send_message(message.channel, "Role updated to zombie for "+message.author.mention)
		log.log("(DIO) %s (%s) is now a zombie"%(message.author.id, message.author.name))
	async def help(message):
		await client.send_message(message.channel, "Type `$zombie` to be a zombie.\nType `$vampire` to be a vampire.")

funcMap={
	"vampire":functions.vampire,
	"zombie":functions.zombie,
	"help":functions.help
}

client=discord.Client()
@client.event
async def on_message(message):
	if message.author==client.user:
		return
	if message.author!=os.environ["James"] and os.environ["test"]=="true": return
	
	funcName=globalTools.getFunc(__.prefix, content)
	if funcName in funcMap.keys(): await funcMap[funcName](message)

# discord.utils.get(server.roles, name="admin")
@client.event
async def on_ready():
	print('DIOBot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["DIObottoken"])

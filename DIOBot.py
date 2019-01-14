
# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=517772410565558295&scope=bot
import discord, os, log
client=discord.Client()
@client.event
async def on_message(message):
	zombie=lambda:discord.utils.get(message.server.roles, name="Zombie")
	vampire=lambda:discord.utils.get(message.server.roles, name="Vampire")
	if message.author==client.user:
		return
	user=message.author
	if message.content.lower()=="$vampire":
		await client.remove_roles(user, zombie())
		await client.add_roles(user, vampire())
	elif message.content.lower()=="$zombie":
		await client.remove_roles(user, vampire())
		await client.add_roles(user, zombie())
	if message.content.lower() in ["$vampire", "$zombie"]:
		await client.send_message(message.channel, "Role updated to `"+message.content.lower()[1:]+"` for "+message.author.mention)
		log.log(("(DIO) %s (%s) is now a "+message.content.lower()[1:])%(message.author.id, message.author.name))

# discord.utils.get(server.roles, name="admin")
@client.event
async def on_ready():
	print('DIOBot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["DIObottoken"])

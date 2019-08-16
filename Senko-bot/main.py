import os, asyncio, sys
sys.path.insert(0, "deps")
import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="$", help_command=None)

owner=bot.get_user(335554170222542851)
nsb=bot.get_user(439205512425504771)
jolyne_irl=bot.get_guild(560507261341007902)

@bot.event
async def on_ready():
	bot.colours=[
		discord.Colour.red(),
		discord.Colour.orange(),
		discord.Colour.gold(),
		discord.Colour.green(),
		discord.Colour.blue(),
		discord.Colour.purple()
	]
	print('Senko-bot bot is ready (%s | %s)'%(bot.user.id, bot.user.name))
	await doRoles()

async def doRoles():
	i=0
	while True:
		for server in bot.guilds:
			role=discord.utils.get(server.roles, name="Certified Senko")
			#print(role)
			await role.edit(color=bot.colours[i])
		i=(i+1)%len(bot.colours)
		await asyncio.sleep(60)


@bot.command(name="verify", help="Owner only - Give user Certified Senko")
async def verify(ctx,):
	message=ctx.message
	if message.author!=bot.owner: return
	role=discord.utils.get(message.guild.roles, name="Certified Senko")
	[await m.add_roles(role, reason="Verified") for m in message.mentions]

@bot.command(name="revoke", help="Owner only - Revoke person's Certified Senko")
async def revoke(ctx):
	message=ctx.message
	if message.author!=bot.owner: return
	role=discord.utils.get(message.guild.roles, name="Certified Senko")
	[await m.remove_roles(role, reason="Unverified") for m in message.mentions]

@bot.command(name="list", help="List all Certified Senkos")
async def list(ctx):
	message=ctx.message
	role=discord.utils.get(message.guild.roles, name="Certified Senko")
	await ctx.send("```"+"\n".join([x.name+"#"+x.discriminator for x in role.members])+"```")

@bot.command(name="help", help="Help")
async def helpmsg(ctx):
	await ctx.send("""Hello! I'm Senko Bot! I was developed by a ~~fucking loser~~ very intelligent person!
Basically, my main function is to take the role labeled \"Certified Senko\" and make its color change every minute.
The rule for getting the Certified Senko role is that you need to change your profile picture to a picture of Senko-san from \"The Helpful Fox Senko-san\", or at least add her ears to your current pfp.
Type `$ears` to get some transparent pictures of said ears.""")

@bot.command(name="ears", help="Some ears to add to your pfp")
async def ears(ctx):
	await ctx.send(files=[
		discord.File(open("Ear1.png", "rb")),
		discord.File(open("Ear2.png", "rb"))
	])

pokemonTags=set(open("pokemon.txt", "r").read().replace("\n", ",").replace(" ", "_").lower().split(","))
urlChars="+%&#"
delChannel=set()
@bot.event
async def on_message(message):
	if message.author==bot.user:
		return
	if message.guild==bot.jolyne_irl:
		if message.content.lower().split(" ")[0] in [".e621", ".r34", ".paheal", ".xbooru", ".yandera", ".pornhub"]:
			delFlag=False
			tags=set(message.content.lower().split(" ")[1:])
			reply="Your command has been deleted for the following reasons:"
			if tags&pokemonTags!=set():
				delFlag=True
				delChannel.add(message.channel)
				reply+="\n- Pokémon tags ("+" ".join([str(x) for x in tags&pokemonTags])+")"
			if set(urlChars)&set(message.content)!=set():
				delFlag=True
				delChannel.add(message.channel)
				reply+="\n- URL escape characters"
			reply+="\nThe command was:```"+message.content.replace("`", "`\u200b")+"```"
			if delFlag:
				await message.channel.send(reply)
				await message.delete()
		elif message.channel in delChannel and message.author==bot.nsb:
			delChannel.remove(message.channel)
			await message.delete()
	await bot.process_commands(message)

bot.run(os.environ["senkobottoken"])
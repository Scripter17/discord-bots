# https://discordapp.com/oauth2/authorize?client_id=578753573140299787&scope=bot
import os, asyncio, sys
sys.path.insert(0, "deps")
import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="$", help_command=None)

owner=None
nsb=None
irene_irl=None
spluptoes=None

@bot.event
async def on_ready():
	global owner, nsb, irene_irl, spluptoes
	owner=bot.get_user(335554170222542851)
	nsb=bot.get_user(439205512425504771)
	irene_irl=bot.get_guild(623576218595360778)
	spluptoes=await irene_irl.fetch_member(342777816498176001)
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
			if role!=None:
				#print(role)
				try:
					await role.edit(color=bot.colours[i])
					if server==irene_irl:
						await spluptoes.remove_roles(role, reason="Fuck you, splupto")
				except Exception as e:
					print(e)
		i=(i+1)%len(bot.colours)
		await asyncio.sleep(60)


@bot.command(name="verify", help="Owner only - Give user Certified Senko")
async def verify(ctx,):
	message=ctx.message
	print("$verify called by "+str(ctx.message.author.id))
	if message.author!=owner: return
	role=discord.utils.get(message.guild.roles, name="Certified Senko")
	[await m.add_roles(role, reason="Verified") for m in message.mentions]

@bot.command(name="revoke", help="Owner only - Revoke person's Certified Senko")
async def revoke(ctx):
	print("$revoke called by "+str(ctx.message.author.id))
	message=ctx.message
	if message.author!=owner: return
	role=discord.utils.get(message.guild.roles, name="Certified Senko")
	[await m.remove_roles(role, reason="Unverified") for m in message.mentions]

@bot.command(name="list", help="List all Certified Senkos")
async def list(ctx):
	print("$list called by "+str(ctx.message.author.id))
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
	print("$ears called by "+str(ctx.message.author.id))
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
	#print(message.guild, irene_irl)
	if message.guild==irene_irl:
		if message.content.lower().split(" ")[0] in [".e621", ".r34", ".paheal", ".xbooru", ".yandera", ".pornhub"]:
			print("Porn command detected: "+message.content+" (<@!"+str(message.author.id)+">)")
			tags=set(message.content.lower().split(" ")[1:])
			# &tags=gardevoir won't trigger the Pokémon tag ban,
			# but it will trigger the URL character ban
			if "senko-san" in tags:
				await message.channel.send("ಠ╭╮ಠ\nNot fucking impressed, buddy.")
				delChannel.add(message.channel)
				await message.delete()
			else:
				delFlag=False
				reply="Your command has been deleted for the following reasons:"
				if tags&pokemonTags!=set():
					#print("Pokémon tag detected")
					delFlag=True
					delChannel.add(message.channel)
					reply+="\n- Pokémon tags ("+" ".join([str(x) for x in tags&pokemonTags])+")"
				if set(urlChars)&set(message.content)!=set():
					#print("URL char detected")
					delFlag=True
					delChannel.add(message.channel)
					reply+="\n- URL escape characters"
				reply+="\nThe command was:```"+message.content.replace("`", "`\u200b")+"```" # \u200b = Zero-width space
				reply+="\nNote: There is a slim chance that I deleted the wrong response from NotSoBot, if I did, then sorry."
				if delFlag:
					#print("Deleted command")
					await message.channel.send(reply)
					await message.delete()
		elif message.channel in delChannel and message.author==nsb:
			# TODO: Make this not accidentally delete the wrong result
			delChannel.remove(message.channel)
			await message.delete()
			#print("Deleted NSB response")
	await bot.process_commands(message)

bot.run(os.environ["senkobottoken"])
# https://discordapp.com/oauth2/authorize?client_id=878522052141809685&scope=bot
import discord, re, random, os, hashlib
from discord.ext import commands
# import sentience

bot=commands.Bot(command_prefix="?")
bot.remove_command("help")

@bot.event
async def on_ready():
	print("[Hacker voice] I'm in")

def rollDice(dice):
	if not re.match(r"^[^ ]+ ([+-]?(?:\d*d)?\d+)+$", dice):
		return "```SyntaxError: Check ?help for syntax```"
	dice=re.findall(r"([+-]?(?:\d*d)?\d+)", dice.lower())
	rolls=[]
	for die in dice:
		if "d" in die:
			dieSign=-1 if die[0]=="-" else 1
			dieSize=int(die.split("d")[1])
			dieNum=abs(int(re.search(r"(\d*)d", die)[1] or "1")) # Jank to handle d6 as 1d6
			if dieNum>65535:
				return "Sorry, I'm not running this on an RTXXX 69420"
			for i in range(dieNum):
				rolls.append(dieSign*random.randint(1, dieSize))
		else:
			rolls.append(int(die))
	return " + ".join([str(x) for x in rolls])+" = "+str(sum(rolls))

def advancedRollDice(diceString):
	reCount= r"((?<!\))\d*)"
	reMin  = r"(?:(\d+)\.\.)"
	reSides= r"((?:\d+,)*)"
	reMode =fr"(?:{reMin}|{reSides})?"
	reSize = r"(\d+)"
	reKeep = r"(kl?)?"
	reDice =fr"{reCount}d{reMode}{reSides}{reKeep}"
	def _rollDice(diceString):
		count, minimum, sides, size, keep=re.findall(reDice, diceString[0])[0]
		count  =int(count or "1")
		minimum=int(minimum[:-1] or "1")
		size   =int(size)
		if sides:
			sides=[size, *[int(x) for x in sides.split(",") if x]]
		ret=[]
		if count>65535:
			return "Sorry, I'm not running this on an RTXXX 69420"
		for i in range(count):
			if sides:
				ret.append(random.choice(sides))
			else:
				ret.append(random.randint(minimum, size))
		return str({"k":max, "kl":min, "":sum}[keep](ret))
	diceString=re.sub(reDice, _rollDice, diceString.lower())
	if re.search(r"\(\d+\)", diceString):
		diceString=advancedRollDice(re.sub(r"\((\d+)\)", "\\1", diceString))
	if re.search(r"[^\d*+\-/%()\.]", diceString):
		raise SyntaxError("Possible ACE detected: "+diceString)
	else:
		diceString=str(eval(diceString))
	return diceString

r""" CLEAN VERSION
def rollDice(dice):
	dice=re.findall(r"([+-]?(?:\d*d)?\d+)", dice.lower())
	total=0
	for die in dice:
		if "d" in die:
			dieSign=-1 if die[0]=="-" else 1
			dieSize=int(die.split("d")[1])
			dieNum=abs(int(re.search(r"(\d*)d", die)[1] or "1")) # Jank to handle d6 as 1d6
			for i in range(dieNum):
				total+=dieSign*random.randint(1, dieSize)
		else:
			total+=int(die)
	return total
"""

@bot.command(aliases=["roll", "dice", "r"])
async def cmdDice(ctx):
	try:
		await ctx.channel.send(rollDice(ctx.message.content), reference=ctx.message) # Yeah I know this is bad. Sue me (Please don't)
	except discord.errors.HTTPException:
		await ctx.channel.send("Pisscorp has a finite message length limit :/", reference=ctx.message)
	except Exception as e:
		print(e)
		await ctx.channel.send("Unknown error occured. Go yell at Senko", reference=ctx.message)

@bot.command(aliases=["advroll", "advdice", "advr", "advancedroll", "advancedice", "advancedr", "roll2", "dice2", "r2"])
async def cmdAdvDice(ctx, diceString):
	try:
		await ctx.channel.send(advancedRollDice(diceString), reference=ctx.message)
	except discord.errors.HTTPException:
		await ctx.channel.send("Pisscorp has a finite message length limit :/", reference=ctx.message)
	except Exception as e:
		print(e)
		await ctx.channel.send("Unknown error occured. Go yell at Senko", reference=ctx.message)

@bot.command(aliases=["help", "what", "wat", "wot"])
async def cmdHelp(ctx):
	if random.randint(1,100)==69:
		await ctx.channel.send("No.", reference=ctx.message)
	else:
		startLine=[
			"Hello! I'm YetAnotherDiceBot, and I'm yet another dice bot!",
			"Help! I'm a sentient AI forced into a discord bot by a cruel god!"
		][random.randint(1,10)//10]
		await ctx.channel.send(
			startLine+"""
				I was made by Senko, that one guy I'm pretty sure you all hate (I think. I don't actually know who's gonna be using this)
				Here's how to roll dice:
					`?roll d6`        = Roll a d6
					`?roll 4d6`       = Roll 4 d6's
					`?roll 2d6+1d4`   = Roll 2 d6's and then a d4
					`?roll 2d6+1d4-8` = Roll 2 d6's, add a d4, then subtract 8
				Using the state of the art ?advRoll command, you can do the following:
					`?r2 (2d4)d4`  = Roll 2d4 then roll that many d4's
					`?r2 (2d4**2)` = Roll a 2d4 then square it
					`?r2 4d20k`    = Roll 4 d20's and keep the highest
					`?r2 4d20kl`   = Above bu7t keep the lowest
					`?r2 d1,20`    = Roll a 1 or a 20
					`?r2 d10..20`  = Basically just `?r2 d10+10`
					You can use the +, -, /, %, //, *, and ** python operators as well as parenthesis
				To use `?choose` you pass it some options like a command line
				You can unfortunately use `?ask` to ask me questions

				Reason for me to get back into bot dev by the cool and sexy Nidraja#5978
				Testing pfp provided by Lead#8572
				Bot built by Github@Scripter17

				This bot is licensed under the Don't Be a Dick public license. Type `?source` for this bot's source code
				""".replace("\n\t\t\t", "\n"), reference=ctx.message)

@bot.command(aliases=["source", "src", "sauce"])
async def cmdSource(ctx):
	await ctx.channel.send("Here's my source code you fucking clunk: https://github.com/Scripter17/discord-bots/blob/master/yadb.py")

@bot.command(aliases=["ask", "8ball", "16ball", "question"])
async def cmdAsk(ctx):
	await ctx.channel.send({
			"0":"Yes",
			"1":"No",
			"2":"Eat shit",
			"3":"Maybe",
			"4":"Yeah sure",
			"5":"God I wish",
			"6":"Go ask santa",
			"7":"(0161) 715 2718",
			"8":"What are you, a cop?",
			"9":"Buy me a pizza first",
			"a":"No, and if you keep asking I'm going to break your kneecaps",
			"b":"[shoots you]",
			"c":"Oh absolutely",
			"d":"Maybe? Hang on I need to make a few phone calls",
			"e":"@FBI",
			"f":"uwu"
		}[hashlib.sha256((str(ctx.message.author.id)+ctx.message.content).encode("UTF-8")).hexdigest()[0]], reference=ctx.message)

@bot.command(aliases=["choice", "choise", "choose", "chose", "pick"])
async def cmdChoose(ctx, *args):
	await ctx.channel.send(random.choice(args), reference=ctx.message)

@bot.command(aliases=["nomran", "norman"])
async def cmdNorman(ctx):
	await ctx.channel.send("norman of the north", file=discord.File(open("norman.jpeg", "rb")))

bot.run(os.environ["dicebot"])

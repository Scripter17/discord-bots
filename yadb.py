# https://discordapp.com/oauth2/authorize?client_id=878522052141809685&scope=bot
import sys, random, os, hashlib, dice
sys.path.insert(0, "deps")
import discord
from discord.ext import commands
# import sentience

bot=commands.Bot(command_prefix="?")
bot.remove_command("help")

@bot.event
async def on_ready():
	print("[Hacker voice] I'm in")

@bot.command(aliases=["help", "what", "wat", "wot", "huh"])
async def cmdHelp(ctx):
	startLine=[
		"Hello! I'm YetAnotherDiceBot, and I'm yet another dice bot!",
		"Help! I'm a sentient AI forced into a discord bot by a cruel god!"
	][random.randint(1,10)//10]
	await ctx.channel.send(
		startLine+"""
			I was made because a friend of my creator needed a dice bot that didn't suck
			Here's how to roll dice using `?roll`/`?r`:
				`?roll d6       ` = Roll a d6
				`?roll 4d6      ` = Roll 4 d6's
				`?roll 2d6+1d4  ` = Roll 2 d6's and then a d4
				`?roll 2d6+1d4-8` = Roll 2 d6's, add a d4, then subtract 8
			Using the state of the art ?roll2/?r2 command, you can do the following:
				`?r2 (2d4)d4` = Roll 2d4 then roll that many d4's
				`?r2 2d4**2 ` = Roll a 2d4 then square it
				`?r2 4d20k  ` = Roll 4 d20's and keep the highest
				`?r2 4d20kl ` = Above but keep the lowest
				`?r2 d1,20  ` = Roll a 1 or a 20
				`?r2 d10..20` = Basically just `?r2 d10+10`

			roll2 supports all non-alphanumeric python operators:
				`+`, `-`, `*`, `/`,
				`**` (exponent), `%` (modulo), `//` (floor division),
				`>`, `>=`, `==`, `<=`, `<`, `!=` (not eaquals),
				`& ` (`0b0011 & 0b0101` = `0b0001`) (bitwise AND),
				`| ` (`0b0011 | 0b0101` = `0b0111`) (bitwise OR),
				`^ ` (`0b0011 ^ 0b0101` = `0b0110`) (bitwise XOR),
				`<<` (`0b0101 <<     1` = `0b1010`) (left shift),
				`>>` (`0b0101 >>     1` = `0b0010`) (right shift)
				Also parenthesis, lists, and dicts work
				Basically it uses python's `exec` function
				With this you can do crazy stuff like `?r2 (2d4**3d10..20)>>2`

				**Currently if any string of two or more letters/underscores are detected roll2 intentionally errors out to prevent Arbitraty Code Execution**
				But, because single letters are okay, you can do weird things like `?r2 (a:=1d4)**a`
				With this there's a total of 53 variables in a single command, which is hopefully more than enough

			You can use `?choose` like `?choose a "b c"` to choose between "a" or "b c"
			You can also use `?ask` to ask me questions

			Reason for me to get back into bot dev by the cool and sexy Nidraja
			Testing pfp provided by Lead
			Bot built and maintaned by Github@Scripter17

			This bot is licensed under the Don't Be a Dick public license. Type `?source` for this bot's source code
			""".replace("\n\t\t\t", "\n"), reference=ctx.message, mention_author=False)

@bot.command(aliases=["source", "code", "sourcecode", "src", "sauce"])
async def cmdSource(ctx):
	await ctx.channel.send("""
			Bot's source code: https://github.com/Scripter17/discord-bots/blob/master/yadb.py
			Dice algorithms: https://github.com/Scripter17/discord-bots/blob/master/dice.py
			""".replace("\n\t\t\t", "\n")[1:], reference=ctx.message, mention_author=False)

@bot.command(aliases=["roll", "dice", "r", "r1"])
async def cmdDice(ctx):
	try:
		result=dice.rollDice(ctx.message.content)
		await ctx.channel.send(result, reference=ctx.message, mention_author=False)
	except discord.errors.HTTPException as e:
		print(e)
		await ctx.channel.send(f"Can't send the whole calculation but your answer is {result}", reference=ctx.message, mention_author=False)
	except Exception as e:
		print(e)
		await ctx.channel.send(f"`{str(type(e))}: {str(e)}`", reference=ctx.message, mention_author=False)

@bot.command(aliases=["roll2", "dice2", "r2"])
async def cmdAdvDice(ctx, diceString):
	try:
		result=dice.advancedRollDice(diceString)
		await ctx.channel.send(result, reference=ctx.message, mention_author=False)
	except discord.errors.HTTPException as e:
		print(e)
		await ctx.channel.send(f"Can't send the whole calculation but your answer is {result}", reference=ctx.message, mention_author=False)
	except Exception as e:
		print(e)
		await ctx.channel.send(f"`{str(type(e))}: {str(e)}`", reference=ctx.message, mention_author=False)

@bot.command(aliases=["ask", "8ball", "8b", "16ball", "16b", "question"])
async def cmdAsk(ctx):
	answers={
		"0":"Yes",
		"1":"No",
		"2":"Eat hot coals",
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
		"e":"@\u0307FBI",
		"f":"uwu"
	}
	msgBin=(str(ctx.message.author.id)+ctx.message.content).lower().encode("UTF-8")
	await ctx.channel.send(answers[hashlib.sha256(msgBin).hexdigest()[0]], reference=ctx.message, mention_author=False)

@bot.command(aliases=["choice", "choise", "choose", "chose", "pick"])
async def cmdChoose(ctx, *args):
	await ctx.channel.send(random.choice(args), reference=ctx.message, mention_author=False)

bot.run(os.environ["dicebot"])

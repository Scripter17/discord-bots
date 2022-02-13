import discord, datetime, colorsys, os
from discord.ext import commands

@bot.event
async def on_ready():
	print("[Hacker voice] I'm in")
	await doRoles()

async def doRoles():
	while True:
		for server in bot.guilds:
			role=discord.utils.get(server.roles, name="Senko Moment")
			if role is not None:
				try:
					await role.edit(color=getColor())
				except Exception as e:
					print(e)
		await asyncio.sleep(60*60)

def getColor():
	color=colorsys.hsv_to_rgb(getHue(), 100, 100)
	return discord.Color((color[0]<<16)+(color[1]<<8)+color[2])

def getHue():
	today=datetime.datetime.today()
	return today.timetuple().tm_yday/(365/isLeapYear(today.year))*360

def isLeapYear(y):
	return y%4==0 and y%100!=0 or y%400==0

bot.run(os.environ["senkobottoken"])
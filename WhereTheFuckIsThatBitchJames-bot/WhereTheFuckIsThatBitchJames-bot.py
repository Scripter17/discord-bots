# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=569276005093736506&scope=bot
import discord, os, globalTools
from datetime import datetime, timedelta
client=discord.Client()
def isSecondWeek():
	epoch=datetime(1970,1,1,0,0,0)
	today=datetime.today()
	epochMonday=epoch-timedelta(epoch.weekday())
	todayMonday=today-timedelta(today.weekday())
	return (todayMonday-epochMonday).days//7%2==0

@client.event
async def on_message(message):
	if message.content.lower()=="*locate":
		w=datetime.today().weekday()
		h=datetime.today().hour
		if w<5 and 8<=h<=16:
			await client.send_message(message.channel, "James should be at school")
		elif isSecondWeek():
			await client.send_message(message.channel, "James should be at his dad's place")
		else:
			await client.send_message(message.channel, "James should be at home")

@client.event
async def on_ready():
	print(isSecondWeek())
	globalTools.log('WhereTheFuckIsThatBitchJames-bot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["lbottoken"])

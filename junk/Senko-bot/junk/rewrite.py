# https://discordapp.com/api/oauth2/authorize?client_id=588137258276880385&permissions=0&scope=bot
import sys, os, re
sys.path.insert(0, "deps")
import discord

class MyClient(discord.Client):
	async def on_ready(self):
		print("Senko-bot is up and ready to assist!")
		self.cfg.notSoBot=self.get_user(439205512425504771)
		self.cfg.vioGuilds=set()
		self.cfg.mod=self.get_user(185220964810883072) # Thanatos from the Jolyne_irl discord server. Er, sorry, *guild*

	class cfg:
		pass

	async def on_message(self, message):
		if message.author==self.user:
			return
		if re.match(r"^\.r34.*[+%]", message.content)!=None:
			self.cfg.vioGuilds.add(message.channel)
			await message.delete()
			reply="""No. Just because the bot lets you bypass the block list, doesn't mean I will.
			%s, %s appears to have bypassed the banned tag filter (or at least attempted to) with the following command
			`%s`""".replace("\t", "")%(self.cfg.mod.mention, message.author.mention, message.content.replace("@", "@ "))
			if "`" in message.content:
				reply+="\nThe cheeky bugger seems to be trying to break me, too."
			await client.send_message(message.channel, reply)
		elif message.channel in self.cfg.vioGuilds and message.author==self.cfg.notSoBot:
			await message.delete()

client = MyClient()
client.run(os.environ["testbot"])

pokemonTags=set(open("pokemon.txt", "r").read().replace("\n", ",").replace(" ", "_").lower().split(","))

URLChars="+%&#"
delChannel=set()

async def runIfJolyne(client, message):
	if message.content.lower().split(" ")[0] in [".e621", ".r34", ".paheal", ".xbooru", ".yandera", ".pornhub"]:
		isJolyne=message.channel.server==servers.jolyneIrl.server
		tags=set(message.content.lower().split(" ")[1:]) # ".r34 a b c" -> ["a", "b", "c"]
		delFlags=[
			(set(URLChars)&set(message.content)!=set(), "containing URL character"), # URL
			(isJolyne and pokemonTags&tags!=set(), "containing Pokémon tags") # Pokémon
		]
		if any([x[0] for x in delFlags]):
			farr=[x[1] for x in delFlags if x[0]]
			"""if len(farr)>1:
				# ["a", "b"] -> "a and b"
				# ["a", "b", "c"] -> "a, b, and c"
				ftxt=", ".join(farr[:-1])
				ftxt="," if len(farr)>2 else ""
				ftxt+=" and "+farr[-1]
			else:
				# ["a"] -> "a"
				ftxt=farr[0]"""
			if len(farr)==1:
				ftxt=farr[0]
			elif len(farr)==2:
				ftxt=farr[0]+" and "+farr[1]
			else:
				ftxt=", ".join(farr[:-1])+", and "+farr[-1]
			delChannel.add(message.channel)
			reply="Your command was flagged for "+ftxt+"."
			reply+="\n"+message.author.mention+" tried to use the following illegal command:"
			reply+="\n```"+message.content.replace("`", "`\u200b")+"```" # "\u200b" = Zero-width space
			await client.send_message(message.channel, reply)
			await client.delete_message(message)
	elif (message.channel in delChannel) and (message.author==people.notSoBot) and (not message.content.lower().startswith(":no_entry: **cooldown**")):
		delChannel.remove(message.channel)
		await client.delete_message(message)
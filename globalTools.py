import time
def log(msg, fmt="%Y-%m-%d %H:%M:%S (GMT%z)"):
	print("\033[2K\033[48D"+time.strftime(fmt)+" "+msg)

def getFunc(prefix, content):
	if content[0:len(prefix)]!=prefix:
		return False
	return content[len(prefix):content.index(" ") if " " in content else None]

async def msgMe(client, message):
	await client.send_message(await client.get_user_info(os.environ["James"]), message)
import time, os
def log(msg, fmt="%Y-%m-%d %H:%M:%S (GMT%z)", out=print):
	out("\033[2K\033[48D\033[33m"+time.strftime(fmt)+" "+msg+"\033[39m")

def getFunc(prefix, content):
	if content[0:len(prefix)]!=prefix:
		return False
	return content[len(prefix):content.index(" ") if " " in content else None]

async def msgMe(client, message):
	await client.send_message(await client.get_user_info(os.environ["James"]), message)

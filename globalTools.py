import time
def log(msg, fmt="%Y-%m-%d %H:%M:%S (GMT%z)"):
	print(time.strftime(fmt)+" "+msg)

def getFunc(prefix, content):
	return content[len(prefix):content.index(" ") if " " in content else None]
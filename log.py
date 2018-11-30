import time
def log(msg, fmt="%Y-%m-%d %H:%M:%S (GMT%z)"):
	print(time.strftime(fmt)+" "+msg)
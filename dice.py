import safeNum, re, random

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
				raise ValueError("Sorry, I can't run more than 65535 dice at once because time sucks")
			for i in range(dieNum):
				rolls.append(dieSign*random.randint(1, dieSize))
		else:
			rolls.append(int(die))
	return " + ".join([str(x) for x in rolls])+" = "+str(sum(rolls))

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

def advancedRollDice(diceString):
	reCount= r"((?<!\))\d*)"
	reMin  = r"(?:(\d+)\.\.)"
	reSides= r"((?:\d+,)*)"
	reSize = r"(\d+)"
	reMode =fr"(?:{reMin}?{reSize}|{reSides})?"
	reKeep = r"(kl?)?"
	reDice =fr"{reCount}d{reMode}{reKeep}"
	def _rollDice(diceString):
		"""
			Process individual dice rolls including ranges, sides, and keeps
		"""
		count, minimum, size, sides, keep=diceString.groups(default="")
		count  =int(count or "1")
		minimum=int(minimum or "1")
		size   =int(size)
		if sides:
			sides=[size, *[int(x) for x in sides.split(",") if x]]
		ret=[]
		if count>65535:
			raise ValueError(f"Too many dice ({count})")
		for i in range(count):
			if sides:
				ret.append(random.choice(sides))
			else:
				ret.append(random.randint(minimum, size))
		return str({"k":max, "kl":min, "":sum}[keep](ret))
	diceString=re.sub(reDice, _rollDice, diceString.lower())
	if re.search(r"\(\d+\)", diceString):
		diceString=advancedRollDice(re.sub(r"\((\d+)\)", "\\1", diceString))
	if re.search(r"[a-zA-Z]", diceString):
		raise SyntaxError("Possible ACE detected: "+diceString)
	else:
		diceString=str(eval(re.sub(r"(\d+)", "safeNum.SafeNum(\\1)", diceString)))
	return diceString

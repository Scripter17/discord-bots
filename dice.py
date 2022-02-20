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
	reSides= r"((?:\d+,)+\d+)"
	reSize = r"(\d+)"
	reMode =fr"(?:{reSides}|{reMin}?{reSize})"
	reKeep = r"(kl?)?"
	reDice =fr"{reCount}d{reMode}{reKeep}"
	def _rollDice(diceString):
		"""
			Process individual dice rolls including ranges, sides, and keeps
		"""
		count, sides, minimum, size, keep=diceString.groups(default="")
		count  =int(count   or "1")
		minimum=int(minimum or "1")
		if size : size   =int(size)
		if sides: sides  =[int(x) for x in sides.split(",") if x]
		ret=[]
		if count>65535:
			raise ValueError(f"Too many dice ({count})")
		for ii in range(count):
			if sides:
				ret.append(random.choice(sides))
			else:
				ret.append(random.randint(minimum, size))
		return str({"k":max, "kl":min, "":sum}[keep](ret))
	diceString=re.sub(reDice, _rollDice, diceString)
	if re.search(r"\B\(\d+\)", diceString):
		diceString=advancedRollDice(re.sub(r"\B\((\d+)\)", "\\1", diceString))
	for sus in re.findall(r"(?i)\b[a-z_][a-z_\d]+\b", diceString):
		if sus not in allowedVars:
			raise SyntaxError("Possible ACE detected: "+diceString)
	else:
		diceString=str(eval(re.sub(r"(\d+)", "safeNum.SafeNum(\\1)", diceString)))
	return diceString

allowedVars=[
	"min", "max", "sum",
	"any", "all",
	"bool", "int", "float", "str", "list",
	"True", "False", "None",
	"hex", "oct", "bin",
	"and", "or", "not",
	"if", "else", "in",
	"lambda",
]

if __name__=="__main__":
	import sys
	print(advancedRollDice(sys.argv[1]))
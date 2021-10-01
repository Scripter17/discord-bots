class SafeNum:
	def __init__(self, num):
		self.num=num
	def __add__(self, other):      return SafeNum(self.num+other.num)
	def __sub__(self, other):      return SafeNum(self.num-other.num)
	def __mul__(self, other):      return SafeNum(self.num*other.num)
	def __matmul__(self, other):   return SafeNum(self.num@other.num)
	def __truediv__(self, other):  return SafeNum(self.num/other.num)
	def __floordiv__(self, other): return SafeNum(self.num//other.num)
	def __mod__(self, other):      return SafeNum(self.num%other.num)

	def __pow__(self, other):
		if self.num*other.num>=1000:
			raise MemoryError("It's possible to crash the bot with a power tower that's too big. This error prevents that")
		return SafeNum(self.num**other.num)

	def __lshift__(self, other): return SafeNum(self.num<<other.num)
	def __rshift__(self, other): return SafeNum(self.num>>other.num)
	def __and__(self, other):    return SafeNum(self.num&other.num)
	def __xor__(self, other):    return SafeNum(self.num^other.num)
	def __or__(self, other):     return SafeNum(self.num|other.num)
	def __str__(self): return str(self.num)

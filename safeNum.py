class SafeNum:
	def __init__(self, num):
		if isinstance(num, SafeNum):
			self.num=num.num
		else:
			self.num=num

	def __add__     (self, other): return SafeNum(self.num+ SafeNum(other).num)
	def __sub__     (self, other): return SafeNum(self.num- SafeNum(other).num)
	def __mul__     (self, other): return SafeNum(self.num* SafeNum(other).num)
	def __matmul__  (self, other): return SafeNum(self.num@ SafeNum(other).num)
	def __truediv__ (self, other): return SafeNum(self.num/ SafeNum(other).num)
	def __floordiv__(self, other): return SafeNum(self.num//SafeNum(other).num)
	def __mod__     (self, other): return SafeNum(self.num% SafeNum(other).num)

	def __pow__(self, other):
		if self*other>=1000:
			raise ValueError(f"An exponentiation that's too big was detected ({self}**{other})")
		return SafeNum(self.num**SafeNum(other).num)

	def __lshift__(self, other): return SafeNum(self.num<<SafeNum(other).num)
	def __rshift__(self, other): return SafeNum(self.num>>SafeNum(other).num)
	def __and__   (self, other): return SafeNum(self.num& SafeNum(other).num)
	def __xor__   (self, other): return SafeNum(self.num^ SafeNum(other).num)
	def __or__    (self, other): return SafeNum(self.num| SafeNum(other).num)

	def __pos__   (self): return SafeNum(+self.num)
	def __neg__   (self): return SafeNum(-self.num)
	def __invert__(self): return SafeNum(~self.num)

	def __gt__(self, other): return SafeNum(self.num> SafeNum(other).num)
	def __ge__(self, other): return SafeNum(self.num>=SafeNum(other).num)
	def __eq__(self, other): return SafeNum(self.num==SafeNum(other).num)
	def __le__(self, other): return SafeNum(self.num<=SafeNum(other).num)
	def __lt__(self, other): return SafeNum(self.num< SafeNum(other).num)
	def __ne__(self, other): return SafeNum(self.num!=SafeNum(other).num)

	def __bool__(self): return bool(self.num)

	def __str__ (self): return str(self.num)
	def __repr__(self): return str(self)

	def __int__(self)  : return int(self.num)
	def __float__(self): return float(self.num)

try:
	from currency_converter import CurrencyConverter as cc
except:
	import pip
	pip.main(["install", "currencyconverter"])
	from currency_converter import CurrencyConverter as cc
conv=cc()
print(conv.convert(5, "CAD", "GBP"))
import PIL.Image, PIL.ImageDraw, PIL.ImageFont
def draw_word_wrap(draw, text,
				   xpos=0, ypos=0,
				   max_width=130,
				   fill=(250,0,0),
				   font=PIL.ImageFont.truetype("arial.ttf", 50)):
	'''Draw the given ``text`` to the x and y position of the image, using
	the minimum length word-wrapping algorithm to restrict the text to
	a pixel width of ``max_width.``
	'''
	text_size_x, text_size_y = draw.textsize(text, font=font)
	remaining = max_width
	# use this list as a stack, push/popping each line
	output_text = []
	# split on whitespace...	
	for word in list(text):
		word_width, word_height = draw.textsize(word, font=font)
		if word_width > remaining:
			output_text.append(word)
			remaining = max_width - word_width
		else:
			if not output_text:
				output_text.append(word)
			else:
				output = output_text.pop()
				output += '%s' % word
				output_text.append(output)
			remaining = remaining - (word_width)
	for text in output_text:
		draw.text((xpos, ypos), text, font=font, fill=fill)
		ypos += text_size_y

def word_wrap_height(draw, text,
				   max_width=130,
				   font=PIL.ImageFont.truetype("arial.ttf", 50)):
	'''Draw the given ``text`` to the x and y position of the image, using
	the minimum length word-wrapping algorithm to restrict the text to
	a pixel width of ``max_width.``
	'''
	text_size_x, text_size_y = draw.textsize(text, font=font)
	remaining = max_width
	# use this list as a stack, push/popping each line
	output_text = []
	# split on whitespace...	
	for word in list(text):
		word_width, word_height = draw.textsize(word, font=font)
		if word_width > remaining:
			output_text.append(word)
			remaining = max_width - word_width
		else:
			if not output_text:
				output_text.append(word)
			else:
				output = output_text.pop()
				output += '%s' % word
				output_text.append(output)
			remaining = remaining - (word_width)
	return len(output_text)*text_size_y
#!/usr/bin/env python3
# Modified from https://gist.github.com/cdiener/10491632

import sys
from PIL import Image, ImageDraw
'''
max_offset = 256
# offset from character.txt
offsets = {
	'%': 0,
	'h': 11,  #2 to 18
	'x': 27, #19 to 35
	'e': 44, # 36 to 52
	'1': 61, # 53 to 69
	'0': 78, # 70 to 86
	'=': 95, # 87 to 103
	'+': 112, # 104 to 120
	')': 129, # 121 to 137
	'(': 146, # 138 to 154
	'c': 165, # 155 to 170
	'r': 180, # 172 to 188
	'~': 196, # 189 to 204
	'"': 208, # 205 to 211
	'-': 230, # 222 to 238
	' ': 256 
}
'''

charset = '%hxe10=+)(cr~"- '
#charset = 'hxe10=+)(cr~"- '
max_offset = len(charset) - 1

#text = '""""""""%%%%%%                '
text = charset
#text = '"%" '
text = 'exec(chr(110+1+1)+chr(110+1+1+1+1)+chr(100+1+1+1+1+1)+chr(110)+chr(110+1+1+1+1+1+1)+chr(10+10+10+10)+chr(100+1+1)+chr(100+1+1+1+1+1+1+1+1)+chr(10+10+10+10+10+10+10+10+10+1+1+1+1+1+1+1)+chr(100+1+1+1)+chr(10+10+10+10+1+1%1))' # Letter A
print(text)
text2 = ''

# justify the text width
text_width = max(len(text), len(text2))
text = text.ljust(text_width, ' ')
text2 = text2.ljust(text_width, ' ')

# w, h
w_scale = int(1/(1/10*7/4)) # manually tuned
width = int(len(text) * w_scale)
height = 10

im= Image.new('RGB', (width, height))
draw = ImageDraw.Draw(im)

def generate_colors(text, h):
	for w in range(width):
		text_index = int(w // w_scale)
		char = text[text_index]
		#print(char, offsets[char])
		#offset = offsets[char]
		assert char in charset
		offset = charset.index(char)
		color = int(offset / max_offset * 255)
		color = (color, color, color)
		draw.point((w, h), color)

for h in range(height):
	#generate_colors(text if h < height/2 else text2, h)
	generate_colors(text, h)

im.save('payload.png')

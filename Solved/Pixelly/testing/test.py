#!/usr/bin/env python3
# Modified from https://gist.github.com/cdiener/10491632

import sys
from PIL import Image, ImageDraw

# w, h
h_scale = 10
height = 256 * h_scale
width = 20
im= Image.new('RGB', (width, height))
draw = ImageDraw.Draw(im)

pixels = []
for h in range(height):
	for w in range(width):
		if (w < width/2):
			val = int(h/h_scale)
		else:
			val = 0xFF-int(h/h_scale)
		color = (val, val, val)
		draw.point((w, h), color)
im.save('test.png')
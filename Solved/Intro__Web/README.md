# Intro: Web
Intro - 10 points

## Challenge 
> Written by michael

> The web goes well beyond the surface of the browser! Warm up your web-sleuthing skills with this challenge by finding the hidden flag on [this page](https://www.easyctf.com/chals/autogen/92/index.html)!

## Hint
> Not sure where to look? Try looking up 'source code', specifically related to web pages.

## Solution

	$ curl https://cdn.easyctf.com/c46ebe0b42ff952351a3d4ee0ac05240137ce24fb48d98cf1f88108448883571_index.html | grep "easyctf"
	        <!-- easyctf{hidden_from_the_masses_b0b88d} -->

## Flag
`easyctf{hidden_from_the_masses_b0b88d}`
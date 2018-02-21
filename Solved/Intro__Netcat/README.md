# Intro: Netcat
Intro - 20 points

## Challenge 
> Written by michael

> I've got a little flag for you! Connect to `c1.easyctf.com:12481` to get it, but you can't use your browser!

> (Don't know how to connect? Look up TCP clients like Netcat. Hint: the Shell server has Netcat installed already!)

> Here's your player key: `874002350`. Several challenges might ask you for one, so you can get a unique flag!

## Solution
	$ nc c1.easyctf.com 12481
	enter your player key: 874002350
	thanks! here's your key: easyctf{hello_there!_0aB703048538fA08}

## Flag
`easyctf{hello_there!_0aB703048538fA08}`

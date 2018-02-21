# Pixelly
Reverse Engineering - 220 points

## Challenge 
> I've created a new [ASCII art generator](http://c1.easyctf.com:12489/), and it works beautifully! But I'm worried that someone might have put a backdoor in it. Maybe you should check out [the source](asciinator.py) for me...

## Hint
> How many characters do you really need, now?

## Solution

#### Analysis of source

- There's a few characters that is used. They are in order of the value of the color.
	+ `charset = ' -"~rc()+=01exh%'`

- To select the character, we need a color of
	+ `charset.index(c) / (len(charset) - 1) * 255`

- We can do this at each pixel which the color is read from.
	+ The pixels which are read are about `SC*WCF` pixels apart

- From this we find that we can use the following functions to form `print(flag)`
	+ `chr, eval, exec`

- To write flag, we can use ASCII in decimal
	+ Since we have `1`, `0`, `+`, `-` operators

- But if we key in any text, we realise the offset changes. 
	+  source-code has `img -= img.min()`
	+ hence we must make sure `%` is always there so the offset does not change
	+ we can solve this by using `1%1` which is `0`

#### Payload

From...

	exec("print(flag)")

To...

	exec(chr(112)+chr(114)+chr(105)+chr(110)+chr(116)+chr(40)+chr(102)+chr(108)+chr(97)+chr(103)+chr(41))

To...

	exec(chr(110+1+1)+chr(110+1+1+1+1)+chr(100+1+1+1+1+1)+chr(110)+chr(110+1+1+1+1+1+1)+chr(10+10+10+10)+chr(100+1+1)+chr(100+1+1+1+1+1+1+1+1)+chr(10+10+10+10+10+10+10+10+10+1+1+1+1+1+1+1)+chr(100+1+1+1)+chr(10+10+10+10+1+1%1))



#### Conversion to image

Unfortunately, my script (`payload.py`) is wonky at best. 

***I borrowed my friend's reversing techniques for reversing the asciinator code (not uploaded in this repo)***.

...

After running his script with the outputs we get the flag `<redacted>`:

	$ python3 asciinator-debug.py flag.png 

	(224, 1)
	exec(chr(110+1+1)+chr(110+1+1+1+1)+chr(100+1+1+1+1+1)+chr(110)+chr(110+1+1+1+1+1+1)+chr(10+10+10+10)+chr(100+1+1)+chr(100+1+1+1+1+1+1+1+1)+chr(10+10+10+10+10+10+10+10+10+1+1+1+1+1+1+1)+chr(100+1+1+1)+chr(10+10+10+10+1+1%1)) 
	<redacted>

Uploading so on the server

	here's your ascii art
	exec(chr(110+1+1)+chr(110+1+1+1+1)+chr(100+1+1+1+1+1)+chr(110)+chr(110+1+1+1+1+1+1)+chr(10+10+10+10)+chr(100+1+1)+chr(100+1+1+1+1+1+1+1+1)+chr(10+10+10+10+10+10+10+10+10+1+1+1+1+1+1+1)+chr(100+1+1+1)+chr(10+10+10+10+1+1%1)) 
	easyctf{wish_thi5_fl@g_was_1n_ASCII_@rt_t0o!}

	[2018-02-15T08:48:00+0000] [W][1257] void cmdline::logParams(nsjconf_t*)():255 Process will be UID/EUID=0 in the global user namespace, and will have user root-level access to files
	[2018-02-15T08:48:00+0000] [W][1257] void cmdline::logParams(nsjconf_t*)():266 Process will be GID/EGID=0 in the global user namespace, and will have group root-level access to files


## Flag

`easyctf{wish_thi5_fl@g_was_1n_ASCII_@rt_t0o!}`
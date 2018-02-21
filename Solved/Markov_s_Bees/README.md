# Markov's Bees
Linux - 50 points

## Challenge 
> Written by ztaylor54

> Head over to the shell and see if you can find the flag at `/problems/markovs_bees/` !

## Hint
> Don't do this by hand!

## Solution

#### Bash loop
Reference: [Recursively find all files in subfolders](https://stackoverflow.com/a/5905066)

	for f in $(find . -name "*.txt"); do
		cat $f | grep 'easyctf';
	done
	
	easyctf{grepping_stale_memes_is_fun}

## Flag
`easyctf{grepping_stale_memes_is_fun}`
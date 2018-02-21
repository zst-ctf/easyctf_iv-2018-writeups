# Zipperoni
Miscellaneous - 160 points

## Challenge 
> Written by gengkev

>I've created a dastardly chain of [zip files](9a894176201a4b9a76c7ebe224239e127e3071bf2d3f2a7ecf974dcd26f96dfa_zip_files). Now you'll never find my flag!

> The first file is `begin.zip`, with password `coolkarni`.

## Hint 1
> I love writing Python programs, don't you?

## Hint 2
	
	hint for zipperoni: you're trying to guess a password. the underscores in the pattern appear at the corresponding location in the actual password.
	
	Hint: You need to guess the password of the next zip file. However, the underscores in the pattern appear in the same positions as they do in the actual password, so you don't need to guess them. For example, the first pattern is __0_0_, which means that you need to guess the 3rd and 5th characters.

## Solution

Extract `begin.zip`
	
	$ unzip -P coolkarni -o zip_files/begin.zip

We are given `pattern.txt` and `hash.txt` which is SHA-1 of the password.

After experimenting around with the patterns: `0` is to bruteforce digits, `A` to bruteforce upper chars and `a` for lower chars, `_` is left as it is.

Attempt a bruteforce after unzipping each ZIP file.

	$ unzip -P $(cat password.txt) -o $(cat filename.txt)
	$ python3 bruteforce_hash.py

Since there are 100 zip files... Run attempt 100 times

	$ echo 'coolkarni' > password.txt
	$ echo 'zip_files/begin.zip' > filename.txt

	$ for i in {0..99}; do bash attempt.sh; done

	$ cat flag.txt
	easyctf{you_must_REALLY_luv_zip_files_by_now!}

## Flag
`easyctf{you_must_REALLY_luv_zip_files_by_now!}`
# Zippity
Miscellaneous - 80 points

## Challenge 
> Written by gengkev

>I heard you liked zip codes! Connect via `nc c1.easyctf.com 12483` to prove your zip code knowledge.

## Hint
>I wonder if you could write a program...

## Solution

Get the 2010 Census for ZIP Code Tabulation Areas (ZCTAs) here:
> https://www.census.gov/geo/maps-data/data/gazetteer2010.html

Python3 program to read from the database and return the answer to the server

	$ python3 solve.py 
	Received: +======================================================================+
	| Welcome to Zippy! We love US zip codes, so we'll be asking you some  |
	| simple facts about them, based on the 2010 Census. Only the          |
	| brightest zip-code fanatics among you will be able to succeed!       |
	| You'll have 30 seconds to answer 50 questions correctly.             |
	+======================================================================+

	3...

	...
	You succeeded! Here's the flag:
	easyctf{hope_you_liked_parsing_tsvs!}

## Flag
`easyctf{hope_you_liked_parsing_tsvs!}`
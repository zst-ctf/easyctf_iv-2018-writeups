# In Plain Sight
Web - 70 points

## Challenge 
> Written by ztaylor54

> I've hidden a flag somewhere at [this site](http://blockingthesky.com/)... can you find it?

> Note: There is not supposed to be a website. Nothing is "down". The YouTube link that some of you are finding is unintentional, pleaes ignore it.

## Hint
> Dig around and see what you can find


## Solution
Couldn't solve it until they added that "Note".

DNS Record Lookup
http://viewdns.info/dnsrecord/?domain=blockingthesky.com

	blockingthesky.com.	30	IN	TXT	 	"easyctf{betcha_wish_you_could_have_used_ANY}"

## Flag
`easyctf{betcha_wish_you_could_have_used_ANY}`
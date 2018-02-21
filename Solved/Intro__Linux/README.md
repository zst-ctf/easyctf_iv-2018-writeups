# Intro: Linux
Intro - 10 points

## Challenge 
> Written by michael

> Log into the shell server! You can do this in your browser by clicking on the Shell server link in the dropdown in the top right corner, or using an SSH client by following the directions on that page.

> Once you've logged in, you'll be in your home directory. We've hidden something there! Try to find it. :)

## Solution

SSH into [EasyCTF Shell Server](https://www.easyctf.com/chals/shell)

	ssh user72122@s.easyctf.com
	
	user72122@shell:~$ ls -la
	total 36
	drwx------   3 user72122 ctfuser  4096 Feb 11 05:02 .
	drwxr-xr-x 219 root      root    12288 Feb 11 05:01 ..
	-rw-r--r--   1 user72122 ctfuser   220 Aug 31  2015 .bash_logout
	-rw-r--r--   1 user72122 ctfuser  3771 Aug 31  2015 .bashrc
	drwx------   2 user72122 ctfuser  4096 Feb 11 05:02 .cache
	-rw-r--r--   1 user72122 ctfuser     0 Feb  7 13:52 .cloud-locale-test.skip
	-rw-r--r--   1 user72122 ctfuser    41 Feb  7 13:41 .flag
	-rw-r--r--   1 user72122 ctfuser   655 May 16  2017 .profile
	user72122@shell:~$ cat .flag
	easyctf{i_know_how_2_find_hidden_files!}

## Flag
`easyctf{i_know_how_2_find_hidden_files!}`
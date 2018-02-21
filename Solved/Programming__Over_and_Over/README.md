# Programming: Over and Over
Programming - 30 points

## Challenge 
> Written by michael

> over and over and over and over and over and ...

> Given a number `N`, print the string "over [and over]" such that the string contains `N` "over"s. There should not be newlines in the string.

>For example:

>- For `N` = 1, print "over".
- For `N` = 5, print "over and over and over and over and over".
- For Python, consider using `for` and `range`.
- For Java/CXX, consider using a `for` loop.

> Try doing it with `while` too for practice!


## Solution

Python3

	N = int(input())
	print(' and '.join(['over'] * N))

C

	#include <stdio.h>

	int main(void) {
	    int numb = 0;
	    scanf("%d", &numb);
	    
	    while (--numb) {
	        printf("over and ");
	    }
	    printf("over");

	    return 0;
	}

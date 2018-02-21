# Little Language
Miscellaneous - 250 points

## Challenge 
> Written by ztaylor54

>I want root access to this special programming portal, and this file is my only clue. Maybe the password is inside? Even if it is, I'm not sure how to enter it. [encrypted](encrypted.png)

>`nc c1.easyctf.com 12480`

>Oh! Almost forgot... [this might help](parser.txt).

## Hint
> One small step for man...

## Solution

If we see the strings, we find the redacted password.

	$ strings encrypted.png | tail -1
	note: the password is l7&4C&Cg


Thanks to some reconnaissance done by my secret spy... It is similar to 5ive programming language by the creator

- [5iveLanguage Specification](https://github.com/eherbert/5ive1terpreter/blob/master/5ive_LanguageSpecification.pdf)

---

Given the `parser.txt`

	S : E                           { ExpS $1 }
	  | global var '=' E            { GlobalVarS $2 $4 }

Compare to [the interpreter parser code](https://github.com/eherbert/5ive1terpreter/blob/master/1nterpreter/Parser.y#L95) 

	Stmt : Expr                                { NodeE $1 }
	  | alive var '=' Expr                  { NodeLet $2 $4 }

Now, looking at the [interpreter test case, `alive` is used to initialise a variable](https://github.com/eherbert/5ive1terpreter/blob/master/TestCases/v4.0/test.iv)

For this CTF, they used `global` instead. Hence, we can try...

	$ nc c1.easyctf.com 12480
	ctflang
	commands begin with ":" (try :help)
	global x = 100
	x
	100

Nice, we have gotten the variable initialised!

---

![encrypted](encrypted.png)

Looking back at the image, it is similar to the language semantics in the specifications.

I'm guessing `flag` is a token which takes in username and password from `E` which is the global variable.

	global username = "root"
	global password = "l7&4C&Cg"
	flag
	EasyCTF{5m4ll_573p_53m4n71c5_4r3_fun_r16h7?}


## Flag
`EasyCTF{5m4ll_573p_53m4n71c5_4r3_fun_r16h7?}`
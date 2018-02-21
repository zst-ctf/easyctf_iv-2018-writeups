# Nosource, Jr.
Web - 80 points

## Challenge 
> Written by gengkev

> I don't like it when people try to view source on my page. Especially when I put all this effort to put my flag verbatim into the source code, but then people just look at the source to find the flag! How annoying.

> This time, when I write my wonderful website, I'll have to hide my beautiful flag to prevent you CTFers from stealing it, dagnabbit. We'll see what you're able to find...

> http://c1.easyctf.com:12486/jr/


## Hint
> Did you know that Chrome Developer Tools has a Network tab?


## Solution

We see this in the source code

	  function process(a, b) {
	    'use strict';
	    var len = Math.max(a.length, b.length);
	    var out = [];
	    for (var i = 0, ca, cb; i < len; i++) {
	      ca = a.charCodeAt(i % a.length);
	      cb = b.charCodeAt(i % b.length);
	      out.push(ca ^ cb);
	    }
	    return String.fromCharCode.apply(null, out);
	  }

	  (function (global) {
	    'use strict';
	    var formEl = document.getElementById('flag-form');
	    var inputEl = document.getElementById('flag');
	    var flag = 'Fg4GCRoHCQ4TFh0IBxENAE4qEgwHMBsfDiwJRQImHV8GQAwBDEYvV11BCA==';
	    formEl.addEventListener('submit', function (e) {
	      e.preventDefault();
	      if (btoa(process(inputEl.value, global.encryptionKey)) === flag) {
	        alert('Your flag is correct!');
	      } else {
	        alert('Incorrect, try again.');
	      }
	    });
	  })(window);

Upon submitting the input, it goes through XOR cipher with `encryptionKey`.
The ciphertext goes through base64 and then compared to `var flag`

----

Let's reverse it using the Javascript console!

	> var flag = 'Fg4GCRoHCQ4TFh0IBxENAE4qEgwHMBsfDiwJRQImHV8GQAwBDEYvV11BCA==';
	> process(atob(flag), window.encryptionKey);

	< "easyctf{congrats!_but_now_f0r_n0s0urc3_...}"

## Flag
`easyctf{congrats!_but_now_f0r_n0s0urc3_...}`
# Soupstitution Cipher
Reverse Engineering - 150 points

## Challenge 
> Written by gengkev

> We had a flag, but lost it in a mess of alphabet soup! Can you help us [find it?](soupstituted.py)

> Connect to the server via `nc c1.easyctf.com 12484`.

## Hint
> I love parsing characters!

## Solution

#### Analysis of program:

***(See soupstituted_modded.py which I have refactored to make it easier to analyse)***

- Takes in 7 digits
- Parse as base-10 int, and reverses it (`1234 -> 4321`)
- Convert to base-16 and pads it with zeros at the left
- Hex string is compared with 's0up'

#### Getting input text

Do in reverse

    >>> 's0up'.encode('hex')
    '73307570'

    >>> 0x73307570
    1932555632

Hence we need to key in `2365552391`

But we realise it is more than 7 chars!

#### Python 3 and unicode?

This is python 3, hence digits in unicode are also accepted!
Hence we can form a 7 char unicode digit which equates to 2365552391.

> Reference: https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python

Here's a list of unicode digits
> http://www.fileformat.info/info/unicode/category/Nd/list.htm

Alternatively, print it using python

    # create list of unicode chars
    digit_list = []
    codepoint_list = []
    for codepoint in range(2**16):
        c = chr(codepoint)
        if c.isdigit():
            digit_list.append(c)
            codepoint_list.append(codepoint)
     
    print(codepoint_list)

#### Codepoint List

Codepoint (base-10 integer) of digit unicodes are listed below:

    [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 178, 179, 185, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1776, 1777, 1778, 1779, 1780, 1781, 1782, 1783, 1784, 1785, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2662, 2663, 2664, 2665, 2666, 2667, 2668, 2669, 2670, 2671, 2790, 2791, 2792, 2793, 2794, 2795, 2796, 2797, 2798, 2799, 2918, 2919, 2920, 2921, 2922, 2923, 2924, 2925, 2926, 2927, 3046, 3047, 3048, 3049, 3050, 3051, 3052, 3053, 3054, 3055, 3174, 3175, 3176, 3177, 3178, 3179, 3180, 3181, 3182, 3183, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310, 3311, 3430, 3431, 3432, 3433, 3434, 3435, 3436, 3437, 3438, 3439, 3558, 3559, 3560, 3561, 3562, 3563, 3564, 3565, 3566, 3567, 3664, 3665, 3666, 3667, 3668, 3669, 3670, 3671, 3672, 3673, 3792, 3793, 3794, 3795, 3796, 3797, 3798, 3799, 3800, 3801, 3872, 3873, 3874, 3875, 3876, 3877, 3878, 3879, 3880, 3881, 4160, 4161, 4162, 4163, 4164, 4165, 4166, 4167, 4168, 4169, 4240, 4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 4969, 4970, 4971, 4972, 4973, 4974, 4975, 4976, 4977, 6112, 6113, 6114, 6115, 6116, 6117, 6118, 6119, 6120, 6121, 6160, 6161, 6162, 6163, 6164, 6165, 6166, 6167, 6168, 6169, 6470, 6471, 6472, 6473, 6474, 6475, 6476, 6477, 6478, 6479, 6608, 6609, 6610, 6611, 6612, 6613, 6614, 6615, 6616, 6617, 6618, 6784, 6785, 6786, 6787, 6788, 6789, 6790, 6791, 6792, 6793, 6800, 6801, 6802, 6803, 6804, 6805, 6806, 6807, 6808, 6809, 6992, 6993, 6994, 6995, 6996, 6997, 6998, 6999, 7000, 7001, 7088, 7089, 7090, 7091, 7092, 7093, 7094, 7095, 7096, 7097, 7232, 7233, 7234, 7235, 7236, 7237, 7238, 7239, 7240, 7241, 7248, 7249, 7250, 7251, 7252, 7253, 7254, 7255, 7256, 7257, 8304, 8308, 8309, 8310, 8311, 8312, 8313, 8320, 8321, 8322, 8323, 8324, 8325, 8326, 8327, 8328, 8329, 9312, 9313, 9314, 9315, 9316, 9317, 9318, 9319, 9320, 9332, 9333, 9334, 9335, 9336, 9337, 9338, 9339, 9340, 9352, 9353, 9354, 9355, 9356, 9357, 9358, 9359, 9360, 9450, 9461, 9462, 9463, 9464, 9465, 9466, 9467, 9468, 9469, 9471, 10102, 10103, 10104, 10105, 10106, 10107, 10108, 10109, 10110, 10112, 10113, 10114, 10115, 10116, 10117, 10118, 10119, 10120, 10122, 10123, 10124, 10125, 10126, 10127, 10128, 10129, 10130, 42528, 42529, 42530, 42531, 42532, 42533, 42534, 42535, 42536, 42537, 43216, 43217, 43218, 43219, 43220, 43221, 43222, 43223, 43224, 43225, 43264, 43265, 43266, 43267, 43268, 43269, 43270, 43271, 43272, 43273, 43472, 43473, 43474, 43475, 43476, 43477, 43478, 43479, 43480, 43481, 43504, 43505, 43506, 43507, 43508, 43509, 43510, 43511, 43512, 43513, 43600, 43601, 43602, 43603, 43604, 43605, 43606, 43607, 43608, 43609, 44016, 44017, 44018, 44019, 44020, 44021, 44022, 44023, 44024, 44025, 65296, 65297, 65298, 65299, 65300, 65301, 65302, 65303, 65304, 65305]


#### Guess & Check (Failed)

      2365552391
    - 1993000000 (Codepoint 1993 @ 6th index)
    ============
       372552391 (Left over)
    -  367300000 (Codepoint 3673 @ 5th index)
    ============
         5252391 (Left over)
    -    4977000 (Codepoint 4977 @ 3th index)
    ============
          275391 (Left over)
    -     240800 (Codepoint 2408 @ 2nd index)
    ============
           34791 (Left over)
    -      27980 (Codepoint 2798 @ 1st index)
    ============
            6611 (Left over)
    -       6611 (Codepoint 6611 @ 0th index)
    ============
               0

1993, 3673, 0, 4977, 2408, 2798, 6611
Wait... the 4th index is the null byte?

***Oops, I forgot the `- ord('0')`. Damn! We must shift everything by 48!!! I must redo it now `:(`***

#### Guess & Check (Working)

Each codepoint must be subtracted by 48dec

      2365552391
    - 2358000000 (Codepoint 2406 = 2358) @ 6th index
    ============
         7552391
    -    7209000 (Codepoint 7257 = 7209) @ 3rd index
    ============
          343391
    -     300100 (Codepoint 3049 = 3001) @ 2nd index
    ============
           43291
    -      33870 (Codepoint 3435 = 3387) @ 1st index
    ============
            9421 
    -       9421 (Codepoint 9469 = 9421) @ 0th index
    ============
               0

#### Techique for Guess & Check
The technique is to choose the closest number in the unicode digits list above

Example, for 2365552391, I chose 2406-48=2358 since it is the closest number to match. (6th index because there's 6 padded zeros on the right)

Then it gets harder towards the bottom because the closest number may make it more difficult to match for the next carry-over number. Hence, it has to be tweaked back and forth until the carry-over number is easier to match.

Another thing to note is that the source code subtracts the codepoint by `ord('0')` or decimal-48. Hence it must be taken into consideration when choosing the closest match

(Note: this has to be done manually, I reckon... bruteforcing is not the way...)

## Flag

    python3 -c "print(''.join([chr(2406), '0', '0', chr(7257), chr(3049), chr(3435), chr(9469)]))" > payload.txt
    cat payload.txt | nc c1.easyctf.com 12484

    oh yay it's a flag! easyctf{S0up_soup_soUP_sOuP_s0UP_S0up_s000000OOOOOOuuuuuuuuppPPppPPPp}

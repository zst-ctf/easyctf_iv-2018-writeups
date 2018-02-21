# Remember Me
Forensics - 130 points

## Challenge 
> Written by neptunia

> I'm such a klutz! I know I hid a flag in [this file](scarboroughfair.mp3) somewhere, but I can't remember where I put it!

> Song is from sukasuka.

## Hint
> Sometimes I can't tell my left from my right, either.


## Solution

From the hint, there's some difference between left and right channels.

References:
 - http://forum.audacityteam.org/viewtopic.php?f=26&t=4851
 - https://github.com/ctfs/write-ups-2015/tree/master/easyctf-2015/forensics/sayonara

We need to subtract the left and right channels, we can do this using Audacity.

#### Steps:
- Open in Audacity
- Select track: `Split Stereo Track`
- Select 1 track: `Effect > Invert`
- Change both tracks: `Pan: 100% Left`
- Select both tracks: `Track > Mix > Mix and Render`
- Export: `File > Export > Export as WAV > Save as: flag.wav`

> flag.wav
>
> Between ***15 sec to 20 sec*** we can hear Text-To-Speech of the flag

## Flag
`easyctf{4ud1o_st3g}`

*Challenge creator annouced that the submitted flag should have a `0` instead of `o`.*

`easyctf{4ud10_st3g}`

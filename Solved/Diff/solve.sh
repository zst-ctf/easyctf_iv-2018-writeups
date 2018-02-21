#!/bin/bash

# https://superuser.com/questions/125376/how-do-i-compare-binary-files-in-linux/
tarfile='9e60f4f6dd55b56236d3d266bb7219c5b92e6542b32c2d42913f3063bc67c390_file.tar'

mkdir -p ./files
tar -xf $tarfile -C ./files
cd files

cmp -l file file2 | gawk '{printf "%c", strtonum(0$3)}' > ../flag.txt
cmp -l file file3 | gawk '{printf "%c", strtonum(0$3)}' >> ../flag.txt
cmp -l file file4 | gawk '{printf "%c", strtonum(0$3)}' >> ../flag.txt
cat ../flag.txt

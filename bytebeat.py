#/usr/bin/env python

from __future__ import print_function
from optparse import OptionParser

t = 0
while True:
    print(chr(int(
        # PUT MATH ON FOLLOWING LINE:
        (t*((15&t>>11)%12)&55-(t>>5|t>>12)|t*(t>>10)*32)-1
        ) % 256 ), end="")
    t += 1

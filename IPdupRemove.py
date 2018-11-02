#!/usr/bin/python

# pip install ipcalc
# python IPdupRemove.py 1.1.1.1/8

import ipcalc
import sys

for x in ipcalc.Network(sys.argv[1]):
   print x

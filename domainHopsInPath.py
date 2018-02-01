"""
@author: souravmaji
"""

from __future__ import division
import sys
import numpy as np
from operator import itemgetter

# Open the file
f = open(str(sys.argv[1]), 'r')

# Each line is stored as an element of the "list" lines
lines = f.readlines()

# Close the file
f.close()
path = []
count = 1
firstTime=True

for l in lines:
    if(firstTime == True):
        startItem = l[:-1]
        firstTime=False
        continue;

    item = l[:-1]
    if(startItem == item):
        count = count + 1
    else:
        val = [startItem, count]
        path.append(val)
        startItem = item
        count = 1

val = [startItem, count]
path.append(val)
print path

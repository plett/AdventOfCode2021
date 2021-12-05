#!/usr/bin/python3
'''
Unfortunately, considering only horizontal and vertical lines doesn't give you
the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your
list will only ever be horizontal, vertical, or a diagonal line at exactly 45
degrees. In other words:

 - An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
 - An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following
diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines
overlap. In the above example, this is still anywhere in the diagram with a 2 or
larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
'''

import fileinput
import re
from itertools import chain

grid= [ [0]*1000 for i in range(1000) ] # a 1000x1000 array. the input data all looks to fit in that size
#grid= [ [0]*10 for i in range(10) ] # for the sample data

def main():
    for line in fileinput.input():
        m = re.search(r"^(\d+),(\d+) -> (\d+),(\d+)$", line)
        x1,y1,x2,y2 = map(int,m.groups())
        if x1==x2:
            #vertical line
            for y in range(min(y1,y2), max(y1,y2)+1):
                grid[y][x1] += 1
        elif y1==y2:
            #horizontal line
            for x in range(min(x1,x2), max(x1,x2)+1):
                grid[y1][x] += 1
        else:
            #diagonal line
            nowx,nowy = x1,y1
            slopex = 1 if x2>x1 else -1
            slopey = 1 if y2>y1 else -1
            while nowx!=x2:
                grid[nowy][nowx] += 1
                nowx += slopex
                nowy += slopey
            grid[y2][x2] += 1

    flat = list(chain.from_iterable(grid))
    count = sum(1 for a in flat if a>1)
    print(count)

if __name__ == '__main__':
    main()



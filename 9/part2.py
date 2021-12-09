#!/usr/bin/python3
'''
Next, you need to find the largest basins so you know what areas are most
important to avoid.

A basin is all locations that eventually flow downward to a single low point.
Therefore, every low point has a basin, although some basins are very small.
Locations of height 9 do not count as being in any basin, and all other
locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the
low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above
example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
'''

import fileinput
import numpy as np
from scipy import ndimage
from itertools import chain
import collections

def inbasin(c):
    # "Locations of height 9 do not count as being in any basin"
    if c=='9':
        return 0
    return 1

def main():
    grid = []
    for line in fileinput.input():
        # this puts a 1 in the grid everywhere there is a value in a basin, and
        # a 0 otherwise
        grid.append( list(map(inbasin, line.rstrip() )))

    # label (i.e. find) contiguous regions in the grid
    labeled_array, num_features = ndimage.label(np.array(grid))
    flatlabeled = chain.from_iterable(list(labeled_array))

    # strip all the zeros out so we only have labels of basins
    basins = filter(lambda x: x>0, flatlabeled)
    #frequency count of all the labels - i.e. sizes of all the basins
    basinsizes = list(collections.Counter(basins).values())
    basinsizes.sort()
    print(np.product(basinsizes[-3:])) #product of largest 3 basins

if __name__ == '__main__':
    main()

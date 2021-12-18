#!/usr/bin/python3

import fileinput
import numpy as np
import re

def fold(grid, direction, pos):
    if direction == 'y':
        #folding "up"
        newgrid = grid[ 0:pos , : ]
        flip = np.flipud(grid[ pos+1:2*pos+1, : ])
        newgrid += flip
        return newgrid
    elif direction == 'x':
        #folding "across"
        newgrid = grid[ : , 0:pos]
        flip = np.fliplr(grid[ : , pos+1:2*pos+1 ])
        newgrid += flip
        return newgrid
    else:
        raise Exception("unknown direction")

def main():
    grid = np.full( (2000,2000), False, np.bool_)
    folds = []
    for line in fileinput.input():
        m = re.search(r"^(\d+),(\d+)$",line)
        if m != None:
            x,y = map(int,m.groups())
            grid[y][x] = True
        else:
            m = re.search(r"^fold along (\w+)=(\d+)$",line)
            if m != None:
                folds.append( ( m.groups()[0] , int(m.groups()[1]) ) )

    for direction, pos in folds:
        grid = fold(grid, direction, pos)
        print(f"There are {np.count_nonzero(grid)} dots after the first fold")
        break




if __name__ == '__main__':
    main()

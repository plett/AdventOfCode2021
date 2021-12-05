#!/usr/bin/python3

# After the initial naive versions which plotted everything on a grid, a second
# version which skips the grid

import fileinput

lines = []
for line in fileinput.input():
    # Turn line into e.g. [0,9,5,9]
    lines.append( [int(num) for pair in line.split(' -> ') for num in pair.split(',')] )

def points_on_line(x1,y1,x2,y2):
    slopex = bool(x2>x1) - bool(x2<x1) # True=1, False=0 giving -1, 0 or +1 for slope
    slopey = bool(y2>y1) - bool(y2<y1)
    return [ (x1 + i*slopex, y1+i*slopey) for i in range(max(abs(x2-x1),abs(y2-y1)) + 1)]

def find_overlaps(lines):
    vents = set()
    overlaps = set()
    for line in lines:
        for x,y in points_on_line(*line):
            if (x,y) in vents:
                overlaps.add((x,y))
            else:
                vents.add((x,y))
    return overlaps

def is_flat(x1,y1,x2,y2):
    return x1==x2 or y1==y2

part1 = len(find_overlaps( [l for l in lines if is_flat(*l)]))
part2 = len(find_overlaps(lines))
print(f"Part 1: {part1} , part 2: {part2}")

#!/usr/bin/python3

import fileinput

def flash(grid, flasher, willflash):
    (y,x) = flasher
    toincrement = []
    if y!=0:
        toincrement.append( (y-1,x) )
        if x!=0:
            toincrement.append( (y-1,x-1) )
        if x!= len(grid[y])-1:
            toincrement.append( (y-1,x+1) )
    if y!=len(grid)-1:
        toincrement.append( (y+1,x) )
        if x!=0:
            toincrement.append( (y+1,x-1) )
        if x!= len(grid[y])-1:
            toincrement.append( (y+1,x+1) )
    if x!=0:
        toincrement.append( (y,x-1) )
    if x!=len(grid[y])-1:
        toincrement.append( (y,x+1) )
    for y1,x1 in toincrement:
        grid[y1][x1] += 1
        if grid[y1][x1] > 9 and (y1,x1) not in willflash:
            willflash.append( (y1,x1) )



def main():
    grid = []
    for line in fileinput.input():
        line=line.strip()
        grid.append( list(map(int,line)) )

    num_flashes = 0
    for step in range(100):
        # First, the energy level of each octopus increases by 1.
        for y in range(len(grid)):
            grid[y] = [x+1 for x in grid[y]]
        # Then, any octopus with an energy level greater than 9 flashes
        willflash = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                energy = grid[y][x]
                if energy == 10:
                    willflash.append( (y,x) )
        for flasher in willflash:
            flash(grid,flasher, willflash)
        num_flashes += len(willflash)
        # Finally, any octopus that flashed during this step has its energy
        # level set to 0, as it used all of its energy to flash.
        for y,x in willflash:
            grid[y][x] = 0
    print(f"{num_flashes=}")


if __name__ == '__main__':
    main()

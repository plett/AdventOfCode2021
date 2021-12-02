#!/usr/bin/python3
import fileinput

horiz = 0
depth = 0
aim = 0 # this is also the depth for part 1

for line in fileinput.input():
    command, value = line.split(' ')
    value = int(value)
    if command == 'forward':
        horiz += value
        depth += (value*aim)
    elif command == 'down':
        aim += value
    elif command == 'up':
        aim -= value
    else:
        print(f"unparsable line {line}")

print(f"part1 : {horiz*aim}")
print(f"part2 : {horiz*depth}")

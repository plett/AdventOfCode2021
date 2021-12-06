#!/usr/bin/python3
'''
Suppose the lanternfish live forever and have unlimited food and space. Would
they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539
lanternfish!

How many lanternfish would there be after 256 days?
'''

# Part 1's brute force method doesn't scale to the trillions of fish in part 2
# So be a bit cleverer about the approach

import fileinput

agemap = [0] * 9 # this is the number of fish with each age, zero through eight
for line in fileinput.input():
    for timer in list(map(int,line.split(','))):
        agemap[timer] += 1

for day in range(256):
    # slide the array along, and put the zeros in as eights (new births)
    agemap = agemap[1:] + agemap[:1]
    # the old zeros are now eights, add them back in as sixes too (reset timer)
    agemap[6] += agemap[8]

    if day==17 or day==79 or day==255:
        print(f"After {day+1} days: {sum(agemap)}")


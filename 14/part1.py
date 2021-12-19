#!/usr/bin/python3

import fileinput
import collections

def applyrules(polymer, rules):
    newpolymer = [ polymer[0] ]
    for i in range(1, len(polymer)):
        pair = polymer[i-1] + polymer[i]
        if pair in rules:
            newpolymer.append(rules[pair])
        newpolymer.append(polymer[i])
    return(newpolymer)

def main():
    polymer = []
    rules = {}
    for line in fileinput.input():
        line=line.strip()
        if fileinput.isfirstline():
            polymer = list(line )
        elif len(line) == 0:
            continue
        else:
            pair,insert = line.split(' -> ')
            rules[pair] = insert

    steps = 10
    for i in range(1,steps+1):
        polymer = applyrules(polymer, rules)
        print(f"After step {i}: {len(polymer)}")
        if i==10:
            counts = collections.Counter(polymer)
            print(counts)
            biggest = max(counts, key=lambda x: counts[x])
            smallest = min(counts, key=lambda x: counts[x])
            diff = counts[biggest] - counts[smallest]
            print(f"{biggest=} {smallest=} {diff=}")




if __name__ == '__main__':
    main()

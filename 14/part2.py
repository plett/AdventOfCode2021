#!/usr/bin/python3

import fileinput
import collections

def addorinc(d, k, i):
    if k in d:
        d[k]+=i
    else:
        d[k]=i

def main():
    rules = {}
    for line in fileinput.input():
        line=line.strip()
        if fileinput.isfirstline():
            polymer = line
        elif len(line) == 0:
            continue
        else:
            pair,insert = line.split(' -> ')
            rules[pair] = insert

    pairs = {}
    for i in range(1, len(polymer)):
        pair = polymer[i-1] + polymer[i]
        addorinc(pairs,pair,1)

    elements = {}
    for e in list(polymer):
        addorinc(elements,e,1)

    steps = 40
    for i in range(1,steps+1):
        addpairs = {}
        for p in pairs.keys():
            if p in rules:
                addorinc(addpairs, p[0]+rules[p], pairs[p])
                addorinc(addpairs, rules[p]+p[1], pairs[p])
                addorinc(addpairs, p, 0-pairs[p])
                addorinc(elements,rules[p],pairs[p])
        for k in addpairs:
            addorinc(pairs,k,addpairs[k])
        #print(f"After step {i}: {sum(elements.values())}")
        if i==10 or i==40:
            biggest = max(elements, key=lambda x: elements[x])
            smallest = min(elements, key=lambda x: elements[x])
            diff = elements[biggest] - elements[smallest]
            print(f"After step {i} {biggest=} {smallest=} {diff=}")

if __name__ == '__main__':
    main()

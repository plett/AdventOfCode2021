#!/usr/bin/python3

import fileinput

def issmall(name):
    return name.islower()

allpaths = []

def findpaths(map, path=[], cave='start', smalltwice=False):
    newsmalltwice = smalltwice
    if issmall(cave) and cave in path:
        # this is a small cave and we've been here before
        if newsmalltwice:
            return
        else:
            newsmalltwice = True
    newpath = path + [cave]
    if cave == 'end':
        # we have found a way out
        allpaths.append(newpath)
        return
    for nextcave in map[cave]:
        findpaths(map, newpath, nextcave, newsmalltwice)


def main():
    map = {}
    for line in fileinput.input():
        a,b = line.strip().split('-')
        if b != 'start':
            if a in map:
                map[a].append(b)
            else:
                map[a] = [b]
        if a != 'start':
            if b in map:
                map[b].append(a)
            else:
                map[b] = [a]
    findpaths(map)
    print(len(allpaths))


if __name__ == '__main__':
    main()

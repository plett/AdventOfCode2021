#!/usr/bin/python3

import fileinput

boards = []

def markboard(n, b) -> bool:
    result = False
    values,marks = b
    for y in range(len(values)):
        for x in range(len(values[y])):
            if values[y][x] == n:
                marks[y][x]=1
                result = True
    return result

def iswin(b) -> bool:
    values,marks = b
    # test for a horizontal win
    for row in marks:
        if sum(row) == 5:
            #all marks are marked
            return True
    # test for a vertical win
    rotated = rotated = [list(r) for r in zip(*marks[::-1])]
    for col in rotated:
        if sum(col) == 5:
            #all marks are marked
            return True
    return False

def calculate_score(n,b) -> int:
    values,marks = b
    thesum = 0
    for y in range(len(marks)):
        for x in range(len(marks[0])):
            if marks[y][x] == 0:
                thesum += values[y][x]
    result = thesum * n
    return result


def main():
    newboard = []
    for line in fileinput.input():
        if fileinput.isfirstline():
            drawn_numbers = list(map(int,line.split(',')))
            continue
        if line == '\n':
            #blank line between boards
            if len(newboard):
                boards.append([newboard , [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]])
                newboard = []
        else:
            #non-blank non-first line - must be board content
            row = list(map(int,filter(None,line.rstrip().split(' '))))
            newboard.append(row)
    #EOF. store the last board
    if len(newboard):
        boards.append([newboard , [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]])

    for n in drawn_numbers:
        #print(f"playing {n}")
        for b in boards:
            wasmarked = markboard(n,b)
        for b in boards:
            if iswin(b):
                if len(boards) == 1:
                    print(f"winner! {b}")
                    score = calculate_score(n,b)
                    print(f"score is {score}")
                    return
                else:
                    #print(f"board {b} would win, removing it")
                    boards.remove(b)



if __name__ == '__main__':
    main()

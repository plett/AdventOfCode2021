#!/usr/bin/python3
'''
Through a little deduction, you should now be able to determine the remaining
digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and segments only
make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

So, the unique signal patterns would correspond to the following digits:

  - acedgfb: 8
  - cdfbe: 5
  - gcdfa: 2
  - fbcad: 3
  - dab: 7
  - cefabd: 9
  - cdfgeb: 6
  - eafb: 4
  - cagedb: 0
  - ab: 1

Then, the four digits of the output value can be decoded:

  - cdfeb: 5
  - fcadb: 3
  - cdfeb: 5
  - cdbaf: 3

Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above,
the output value of each entry can be determined:

  - fdgacbe cefdb cefbgd gcbe: 8394
  - fcgedb cgb dgebacf gc: 9781
  - cg cg fdcagb cbg: 1197
  - efabcd cedba gadfec cb: 9361
  - gecf egdcabf bgf bfgea: 4873
  - gebdcfa ecba ca fadegcb: 8418
  - cefg dcbef fcge gbcadfe: 4548
  - ed bcgafe cdgba cbgef: 1625
  - gbdfcae bgc cg cgb: 8717
  - fgae cfgab fg bagce: 4315

Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the
four-digit output values. What do you get if you add up all of the output
values?
'''


'''
Actual, non scrambled 7-segment layout:

 aaaa
f    b
f    b
 gggg
e    c
e    c
 dddd

Which means that sorted segments for digits are:
'''

digits = {
        'abcdef'    : 0,
        'bc'        : 1,
        'abdeg'     : 2,
        'abcdg'     : 3,
        'bcfg'      : 4,
        'acdfg'     : 5,
        'acdefg'    : 6,
        'abc'       : 7,
        'abcdefg'   : 8,
        'abcdfg'    : 9}

'''
From the lengths in part 1 we can identify digits 1,4,7,8

Segment a is the one that appears in digit 7 but not digit 1

Frequency counts of segments:
a = 8 (i.e. segment A appears in 8 of the 10 digits)
b = 8
c = 9
d = 7
e = 4
f = 6
g = 7

Segment c is the only segment which is used in 9 digits (all but digit 2)
Segment e is the only segment which is used in 4 digits
Segment f is the only segment which is used in 6 digits

b is the segment in digit 1 which isn't c
g is the segment in digit 4 which isn't b,c or f
d is the segment we don't have yet :)
'''

import fileinput

outputsum=0
for line in fileinput.input():
    patternstring,output = line.split(' | ')
    patterns = patternstring.split(' ')
    mapping = {} # will be dict of real->scrambled

    one = next(filter(lambda x: len(x)==2, patterns))
    four = next(filter(lambda x: len(x)==4, patterns))
    seven = next(filter(lambda x: len(x)==3, patterns))
    eight = next(filter(lambda x: len(x)==7, patterns))

    mapping['a'] = list(set(seven) - set(one))[0] #a is the segment in seven but not one

    joined=''.join(patterns)
    frequencies = {x:joined.count(x) for x in joined}

    #c, e and f occur in 9, 4 and 6 digits each
    mapping['c'] = [k for k in frequencies if frequencies[k]==9][0]
    mapping['e'] = [k for k in frequencies if frequencies[k]==4][0]
    mapping['f'] = [k for k in frequencies if frequencies[k]==6][0]

    # b is the element in digit 1 which isn't c
    mapping['b'] = list(set(one) - set(mapping['c']))[0]

    # g is the element in digit 4 which we don't have yet
    mapping['g'] = list(set(four) - set(mapping.values()))[0]

    # d is the elemtn in digit 8 which we dont' have yet
    mapping['d'] = list(set(eight) - set(mapping.values()))[0]

    inversemapping = {v: k for k,v in mapping.items()} # now goes scrambled->real
    number = 0
    for scrambled in output.split(' '):
        scrambled = scrambled.rstrip()
        real = list(map(lambda x: inversemapping[x] , list(scrambled)))
        real.sort()
        real = ''.join(real)
        number = number * 10 + digits[real]
    outputsum += number

print(outputsum)






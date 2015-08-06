"""
Your program should accept a file as its first argument. Each line of input contains three space separated integers:
the length of the wire "l", distance "d", and number of bats "n" that are already hanging on the wire.

The "n" number of bats is located in any order. All numbers are integers. You can assume that the bats that are
already hanging on the wire are at least 6 cm from the buildings and at least "d" centimeters apart from each other.

Output sample:
3
5
0
5
8
"""

import sys
# test_cases = open(sys.argv[1], 'r')
with open('bats_input.txt') as test_cases:
    for test in test_cases:
        # code goes here


test_cases.close()

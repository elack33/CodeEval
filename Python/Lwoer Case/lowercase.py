"""
INPUT SAMPLE:

The first argument will be a path to a filename containing sentences, one per line. You can assume all characters are from the english language. E.g.

HELLO CODEEVAL
This is some text
OUTPUT SAMPLE:

Print to stdout, the lowercase version of the sentence, each on a new line. E.g.

hello codeeval
this is some text
"""

import sys
# test_cases = open(sys.argv[1], 'r')
with open('lowercase.txt') as test_cases:
    for test in test_cases:
        # code goes here
        print test
        print test.lower()

test_cases.close()
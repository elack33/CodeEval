# The first argument is a path to a file. The file contains strings.
#
# For example:
# yellow
# tooth
#
# OUTPUT SAMPLE:
#
# Print to stdout the first non-repeated character, one per line.
#
# For example:
# y
# h
# with open('fnrc.txt') as test_cases:
import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # code goes here
    for x in test:
        count = test.count(x)
        if count == 1:
            char = x
            print x
            break

test_cases.close()

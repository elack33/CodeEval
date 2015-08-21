
import os, sys

# with open('rc.txt') as test_cases:

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # code goes here
    string_array = []
    string_array = test.rstrip('\n').split(', ')
    letter_list = list(string_array[1])
    word = string_array[0]
    for each in letter_list:
        if each in word:
            new_word = word.replace(each, '')
    print new_word
test_cases.close()
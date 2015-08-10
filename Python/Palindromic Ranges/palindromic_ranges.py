"""
CHALLENGE DESCRIPTION:

A positive integer is a palindrome if its decimal representation (without leading zeros) is a palindromic string
(a string that reads the same forwards and backwards). For example, the numbers 5, 77, 363, 4884, 11111,
12121 and 349943 are palindromes.

A range of integers is interesting if it contains an even number of palindromes. The range [L, R],
with L <= R, is defined as the sequence of integers from L to R (inclusive): (L, L+1, L+2, ..., R-1, R).
L and R are the range's first and last numbers.

The range [L1,R1] is a subrange of [L,R] if L <= L1 <= R1 <= R. Your job is to determine how many interesting
subranges of [L,R] there are.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case.
Each test case will contain two positive integers, L and R (in that order), separated by a space. eg.
1 2
1 7
87 88
OUTPUT SAMPLE:

For each line of input, print out the number of interesting subranges of [L,R] eg.
1
12
1
For the curious: In the third example, the subranges are: [87](0 palindromes), [87,88](1 palindrome),[88](1 palindrome).
Hence the number of interesting palindromic ranges is 1
"""
with open('pp.txt') as test_cases:
# import sys
# test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        # code goes here
        int_array = map(int, test.split(' '))
        last = int_array.pop()
        first = int_array.pop()
        palin_list = []
        count = 0

        subrange_list = [(x, y) for x in range(first, last + 1) for y in range(first, last + 1) if x != y]
        # a = tuple(first)
        # b = tuple(last)
        # subrange_list.insert(0, a)
        # subrange_list.append(b)
        print subrange_list
        for x in (range(first, last + 1)):
            y = str(x)[::-1]
            if str(x) == y:
                palin_list.append(x)

        # print palin_list

        # mylist = [i for i, j in zip(subrange_list, palin_list) if i == j]
        # mylist = set(subrange_list).intersection(palin_list)
        # mylist = [(x, y) for x in subrange_list if x in palin_list for y in subrange_list if y in palin_list]
        print palin_list
        # mylist = [(x, y) for x in subrange_list if x in palin_list]
        # mylist = [(i for i, v in enumerate(subrange_list) if v[0] in palin_list)]
        # print "My list: ", mylist
        test_list = []
        for (x, y) in subrange_list:
            if x in palin_list:
                if x % 2 == 0:
                    test_list.append(x)
                    print "test x: ", test_list
                    count += 1
            elif y in palin_list:
                if y % 2 == 0:
                    test_list.append(y)
                    print"test y:",  test_list
                    count += 1
        newset = set(test_list)

        print newset
        print count
        print len(newset)


    # TODO: I need to look at each tuple and see if it has a palindrome and if so, which palindrome and then see if it is an even number!






# test_cases.close()
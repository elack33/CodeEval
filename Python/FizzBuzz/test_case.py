# with open('Fizzbuzz_input.txt') as test_cases:

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.split()
    n = int(test[2])
    y = int(test[1])
    x = int(test[0])
    result_list = []
    for num in range(1, n + 1):
        if (num % x == 0) & (num % y == 0):
            result_list.append('FB')
        else:
            if num % x == 0:
                result_list.append('F')
            if num % y == 0:
                result_list.append('B')
            else:
                result_list.append(str(num))
    print " ".join(result_list)
test_cases.close()



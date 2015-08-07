# with open('soi.txt') as test_cases:
import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # code goes here
    int_array = map(int, test.split(','))
    current = 0
    current_max = 0
    for num in int_array:
        current += num
        if current < 0:
            current = 0
        elif current > 0:
            if current > current_max:
                current_max = current
    if current_max == 0:
        current_max = max(int_array)
    print current_max
test_cases.close()
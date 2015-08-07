#
# ((((val1 op1 val2) op2 val3) op3 val4) op4 val5) = 42
import sys
import itertools
# test_cases = open(sys.argv[1], 'r')
with open('num_ops.txt') as test_cases:
    for test in test_cases:
        # code goes here
        int_array = map(int, test.split(' '))
        ops = [' + ', ' - ', ' * ', ' / ']
        print int_array

        # if (((int_array[0] + int_array[1]) - int_array[2] * int_array[3]) / int_array[4]) == 42:
        #     print 'YES'
        list3 = [zip(x,ops) for x in itertools.permutations(int_array, len(ops))]

        chain = itertools.chain(*list3)
        list4 = list(chain)
        print list4

# test_cases.close()
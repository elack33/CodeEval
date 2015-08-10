# ASADB
# ABCCED
# ABCF

# with open('soi.txt') as test_cases:
# import sys
# test_cases = open(sys.argv[1], 'r')
with open('ws.txt') as test_cases:
    for test in test_cases:
        # code goes here
        print 'test:', test
        char_list = []
        for each in test:
            char_list.append(each)
        # char_list.pop()
        # print 'list char:', char_list
        board = [
                    ['ABCE'],
                    ['SFCS'],
                    ['ADEE']
        ]

        top = ''.join(board[0])
        middle = ''.join(board[1])
        bottom = ''.join(board[2])
        ind_map = []

        for each_char in char_list:
            if each_char in top:
                ind = char_list.index(each_char)
                ind_map.append(ind)

        def group(L):
            first = last = L[0]
            for n in L[1:]:
                if n - 1 == last: # Part of the group, bump the end
                    last = n
                else: # Not part of the group, yield current group and start a new
                    yield first, last
                    first = last = n
            yield first, last # Yield the last group

        # from operator import itemgetter
        # from itertools import groupby
        # # data = [2, 3, 4, 5, 12, 13, 14, 15, 16, 17]
        # for k, g in groupby(enumerate(ind_map), lambda (i,x):i-x):
        #     print "k data", k
        #     print "g data: ", g
        #     print map(itemgetter(1), g)
        #     x = map(itemgetter(1), g)
        #     print "x : ", x
        #     # if len(x) > 0:
        #     #     ind_seq = x
        #
        # print ind_map
        # print ind_seq




        # for each_char in char_list:
        #     # print 'each char:', each_char
        #     top = ''.join(board[0])
        #     middle = ''.join(board[1])
        #     bottom = ''.join(board[2])
        #     # print 'top:', top
        #     # print 'middle: ', middle
        #     # print 'bottom', bottom
        #     print char_list
        #     if each_char in top:
        #
        #         ind = char_list.index(each_char)
        #         print ind





# test_cases.close()

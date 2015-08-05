__author__ = 'Dar'


class FizzBuzz(object):

    def __init__(self):
        # self.validate_input(3, 5, 50)
        self.import_list('Fizzbuzz_input.txt')

    def import_list(self, filename):
        with open(filename) as load_import_data:
            for line in load_import_data:
                x = line.split(' ')
                y = line.split(' ')
                n = line.split(' ')
                self.validate_input(x, y, n)

    def validate_input(self, x, y, n):
        if 0 < x < 21:
            if 0 < y < 21:
                if 20 < n < 101:
                    self.fizzb(x, y, n)
                else:
                    print "Invalid number range found.\n"
            else:
                print "Y value is out of range.\n"
        else:
            print "X value is out of range.\n"

    def fizzb(self, x, y, n):
        n = int(n)
        for num in range(1, n):
            if (num % x == 0) & (num % y == 0):
                print 'FB',
            else:
                if num % x == 0:
                    print 'F',
                if num % y == 0:
                    print 'B',
                else:
                    print num,


test = FizzBuzz()

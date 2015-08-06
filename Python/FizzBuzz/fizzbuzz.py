import sys
import os


class FizzBuzz(object):

    def __init__(self):
        self.line_count = 0
        self.filename = ''
        self.check_file()

    def check_file(self):
        self.filename = str(sys.argv[1])

        if os.path.exists(self.filename):
            self.import_list(self.filename)
        else:
            print "File not found, please try again."

    def import_list(self, filename):
        with open(filename) as load_import_data:
            for line in load_import_data:
                line = line.split()
                n = int(line.pop())
                y = int(line.pop())
                x = int(line.pop())
                self.line_count += 1
                self.validate_input(x, y, n)

    def validate_input(self, x, y, n):
        if 0 < x < 21:
            if 0 < y < 21:
                if 20 < n < 101:
                    self.fizzb(x, y, n)
                else:
                    print "N value is out of range, skipping this line: {}.\n".format(self.line_count)
                    return
            else:
                print "Y value is out of range, skipping this line: {}.\n".format(self.line_count)
                return
        else:
            print "X value is out of range, skipping this line: {}.\n".format(self.line_count)
            return

    def fizzb(self, x, y, n):
        for num in range(1, n +1):
            if (num % x == 0) & (num % y == 0):
                print 'FB',

            else:
                if num % x == 0:
                    print 'F',
                if num % y == 0:
                    print 'B',
                if num == n:
                    print '\n'
                else:
                    print num,


test = FizzBuzz()

# Write a program which determines the largest prime palindrome less than 1000.

# try to figure out how to go form 1000 down to 2 instead of looking at every prime from 2 to 1000


def main():
    high = 1000
    low = 2
    if (high % 2) == 0:
        high -= 1
    for x in reversed(range(low, high)):
        if is_prime(x):
            y = str(x)[::-1]
            if str(x) == y:
                print x
                exit()


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        return True

main()

def main():
    prime_list = []
    sum_of_prime = 1
    count = 1
    while len(prime_list) < 1000:
        if is_prime(count):
            prime_list.append(count)
            count += 2
        else:
            count += 2
    for x in prime_list:
        sum_of_prime += x
    print sum_of_prime


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

main()

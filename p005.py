from itertools import permutations
from math import sqrt


def main():
    print(max([int(''.join(p)) for p in permutations('1234567') if is_prime(int(''.join(p)))]))
    is_prime(5)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()

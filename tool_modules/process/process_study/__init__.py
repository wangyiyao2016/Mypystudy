import concurrent.futures
import math

PRIMES = [
    112272,
    11258,
    112272,
    115280,
    11579,
    109972]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = executor.map(is_prime, PRIMES)
        for i in futures:
            print(i)
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()

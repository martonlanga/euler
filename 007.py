import time


def isPrime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate(nThPrime):
    n = 0
    i = 0
    while n < nThPrime:
        i += 1
        if isPrime(i):
            n += 1
    return i


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate(10001)
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

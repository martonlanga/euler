import time


def smallestPrime(n):
    assert n >= 2
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


def calculate(num):
    while True:
        n = smallestPrime(num)
        if n < num:
            num //= n
        else:
            return n


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate(600_851_475_143)
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

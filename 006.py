import time


def calculate(first, last):
    sumOfSqaures = 0
    for i in range(first, last + 1):
        sumOfSqaures += i ** 2
    squareOfSums = sum(range(first, last + 1))
    return squareOfSums ** 2 - sumOfSqaures


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate(1, 100)
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

import time


def calculate():
    x = y = 1
    sum = 0
    while x < 4 * 10 ** 6:
        print(x, y)
        sum += x + y
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate()
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

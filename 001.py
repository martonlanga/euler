import time


def calculate():
    return sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate()
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

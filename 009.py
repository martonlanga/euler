import time


def calculate(sum):
    for x in range(1, sum + 1):
        for y in range(x, sum + 1):
            for z in range(y, sum + 1):
                if x + y + z == sum and x ** 2 + y ** 2 == z ** 2:
                    print(x, y, z)
                    return x * y * z
    return 0


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate(1000)
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

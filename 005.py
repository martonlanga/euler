import time

# #bruteforce
def calculate(smallest, biggest):
    number = 0
    found = False
    while found == False:
        number += 1

        for i in range(smallest, biggest + 1):
            if number % i != 0:
                break
            if i == biggest:
                found = True
    return number


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate(1, 20)
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

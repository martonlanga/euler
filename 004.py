import time


def palindrome(num):
    return str(num) == str(num)[::-1]


def calculate():
    palindromes = set()
    for i in range(100, 999):
        for k in range(100, 999):
            num = i * k
            if palindrome(num):
                palindromes.add(num)

    return max(palindromes)


if __name__ == "__main__":
    start = time.perf_counter()
    result = calculate()
    end = time.perf_counter()

    print("Result:", result)
    print(f"🏃 {end - start} 🏃")

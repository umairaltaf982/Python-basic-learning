import time

def log_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("Time taken:", end - start, "seconds")
        return result
    return wrapper


@log_time
def sum_numbers(n):
    tot = 1
    for i in range(1, n):
        tot = tot + i
    return tot

print("Sum:", sum_numbers(1234567))
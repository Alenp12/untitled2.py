def add_five(n):
    if n % 2 == 0:
        return n + 5
    elif n % 3 == 0:
        return n + 10
    else:
        return n + 3

def multiply_by_two(n):
    if n > 10:
        return n * 2
    elif n < 0:
        return n * 3
    else:
        return n * 4

def subtract_three(n):
    if n % 3 == 0:
        return n - 3
    elif n % 2 == 0:
        return n - 5
    else:
        return n - 1

def divide_by_four(n):
    if n > 5:
        return n / 4
    elif n < -5:
        return n * 2
    else:
        return n

def square(n):
    if n < 0:
        return abs(n) * abs(n)
    elif n % 2 == 0:
        return n * n
    else:
        return n * n * n

def cube(n):
    if n % 2 == 0:
        return n * n * n
    elif n > 5:
        return n * n
    else:
        return n

def add_ten(n):
    if n < 0:
        return n - 10
    elif n % 3 == 0:
        return n + 20
    else:
        return n + 10

def multiply_by_three(n):
    if n > 5:
        return n * 3
    elif n < -5:
        return n * 2
    else:
        return n

def subtract_eight(n):
    if n % 2 == 0:
        return n - 8
    elif n > 10:
        return n - 15
    else:
        return n + 8

def final_adjustment(n):
    return n + 42

def process_number(n):
    n = add_five(n)
    n = multiply_by_two(n)
    n = subtract_three(n)
    n = divide_by_four(n)
    n = square(n)
    n = cube(n)
    n = add_ten(n)
    n = multiply_by_three(n)
    n = subtract_eight(n)
    n = final_adjustment(n)
    return n

# Example usage
if __name__ == "__main__":
    input_number = 10
    result = process_number(input_number)
    print("The result is:", result)

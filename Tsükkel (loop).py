# 1. Sum between

def sum_between(start: int, end: int) -> int:
    """
    Return sum of integers between start and end (both included).

    print(sum_between(3, 5)) => 3 + 4 + 5 = 12
    print(sum_between(5, 5)) => 5
    """
    # Your code goes here
    sum = 0
    for number in range(start, end+1):
        print(number)
        sum = sum + number
    return sum

if __name__ == "__main__":
    print(sum_between(3, 5))
    print(sum_between(5, 5))


print("---------------------------------")


# 2. Sum of even numbers

def sum_of_even_numbers(n: int) -> int:
    """
    Return sum of even numbers from 0 up to n (included).

    print(sum_of_even_numbers(5)) => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0)) => 0
    """
    # Your code goes here
    sum = 0
    for number in range(n+1):
        if number % 2 == 0:
            sum = sum + number
    return sum


if __name__ == "__main__":
    print(sum_of_even_numbers(5))
    print(sum_of_even_numbers(0))

print("---------------------------------")


# 3. Sum of multiples

def sum_of_multiples(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between 0 and end (included).

    print(sum_of_multiples(3, 10)) => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10)) => 7
    print(sum_of_multiples(11, 10)) => 0
    """
    # Your code goes here
    sum = 0
    for number in range(n, end):
        if number % n == 0:
            sum = sum + number
    return sum

if __name__ == "__main__":
    print(sum_of_multiples(3, 10)) #=> 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10)) #=> 7
    print(sum_of_multiples(11, 10)) #=> 0

print("---------------------------------")

# 4. Cross sum

def cross_sum(numbers: str) -> int:
    """
    Return cross sum of numbers.
    print(cross_sum("1234")) => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0")) => 0
    print(cross_sum("4129458")) => 33
    """
    sum = 0
    for letter in numbers:
        sum += int(letter)
    return sum

if __name__ == "__main__":
    print(cross_sum("1234")) #=> 1 + 2 + 3 + 4 = 10
    print(cross_sum("0")) #=> 0
    print(cross_sum("4129458")) #=> 33


    print("---------------------------------")

#5. Multiple between

def multiply_between(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    # Your code goes here
    numbers = list(range(start, end + 1))
    sum = 1
    for number in numbers:
        sum = sum * number
    return sum

if __name__ == "__main__":
    print(multiply_between(1, 3)) #=> 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) #=> 14529715200
    print(multiply_between(0, 7)) #=> 0
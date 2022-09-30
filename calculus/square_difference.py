# Square difference 3025 - 325 = 2640
def square_difference(number):
    result = square_of_sum(number) - sum_of_squares(number)
    return result

# The sum of the squares of the first ten natural numbers 1^2 + 2^2...+ 10^2 = 325
def sum_of_squares(number):
    sum_squares = 0
    
    for i in range(number):
        i += 1
        sum_squares += i * i
    return sum_squares

# The square of the sum of the first ten natural numbers (1+2+...+10)^ 2 = 55 ^ 2 = 3025
def square_of_sum(number):
    square = 0
    for i in range(number):
        i += 1
        square += i
    return square * square
    
    


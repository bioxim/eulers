""" Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
find the sum of the even-valued terms. """
seq = [1,2]

def fibonacci(target): 
    i = 3
    sum = 0
    
    if target <= 32:
        for i in range(target - 2):
            seq.append(seq[i] + seq[i+1])
        i += 1
        print("The Fibonacci sequence is: ", seq)
        for x in range(len(seq)):
            if seq[x] % 2 == 0:
                sum = sum + seq[x]
        return sum
    else:
        print(target, "es mayor que 32, ingrese otro número nuevamente")

"""
    SECUENCIA FIBONACCI
"""
def fibonacci_seq(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)

print(fibonacci_seq(1))

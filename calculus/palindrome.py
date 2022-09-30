"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

def max_palindrome(number):
    max_limit = 10**number - 1 # 10^2 = 100 -> 100 - 1 = 99  --> para 3 dígitos
    min_limit = max_limit // 10 + 1 # 99/10 = 9 + 1 --> para 2 dígitos
    temp = 0
    list_palindrome = []
    
    for i in range(max_limit, min_limit - 1, -1):
        for j in range(i, min_limit - 1, -1):
            if isPalindrome(i*j) and i*j > temp:
                temp = i * j
                list_palindrome.append(i*j)
    print(list_palindrome) 
    return temp

def isPalindrome(n):
    # 9009 --> reversed number 9009
    reversed_number = 0
    unit = 0
    temp = n
    
    while temp != 0:
        unit = temp%10  # 9009 % 10 -> 9
        reversed_number = reversed_number * 10 + unit
        temp = int(temp/10)
    
    if reversed_number == n:
        return True
    return False
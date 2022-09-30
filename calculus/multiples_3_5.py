# Multiples of 3 or 5 below a given natural number.
  
def multiples(target):
    sum = 0 
    i = 0 
    for i in range(1,target):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum

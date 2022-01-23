

def factorial(number: int) -> int:
    '''
    formula: n! = n . (n – 1) . (n – 2) . (n – 3)!
    stop conditions: 
    returns: factorial of number
    A = {x | x e N+}
    '''
    total = number
    actual_number = number
    for count in range(number):
        if actual_number == 1:
            return total
        if actual_number == 0:
            return 1
        total *= (actual_number-1)
        actual_number -= 1


def factorial_recursive(number: int) -> int:
    '''
    formula: n! = n . (n – 1) . (n – 2) . (n – 3)!
    stop conditions: 
    returns: factorial of number
    A = {x | x e N+}
    '''
    total = number
    if number == 1:
        return total
    if number == 0:
        return 1

    return total * factorial_recursive(number-1)

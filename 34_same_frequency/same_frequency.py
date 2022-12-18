def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return count_freq(num1) == count_freq(num2)
    

def count_freq(num):
    result = {}
    num = str(num)
    for digit in num:
        result[digit] = result.get(digit, 0) + 1

    return result
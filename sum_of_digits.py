def sum_of_digits(n):
    while n >= 10: #chat gpt 
       n = sum(int(digit) for digit in str(n)) #chat gpt 
    return n
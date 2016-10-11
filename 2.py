'''
Project Euler Problem #2 - Python

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fibs_gen(limit):

    cur, prev = 1, 0

    while cur < limit:

        yield cur
        cur, prev = cur + prev, cur

even_fibs = (fib for fib in fibs_gen(4000000) if fib % 2 == 0) 
print(sum(even_fibs))

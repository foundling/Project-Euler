'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fibs(limit):

    cur, prev = 1, 0

    while cur < limit:

        yield cur
        cur, prev = cur + prev, cur

print sum(n for n in fibs(4000000) if n % 2 == 0)

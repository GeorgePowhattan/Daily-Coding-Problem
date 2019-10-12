'''The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below are the first few values of the sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

Given a number n, print the n-th Fibonacci Number.'''

# Fibonacci - recursive
def fibonacci_rec(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# Fibonacci - iteration
def fibonacci_iter(n):
    if n==0 or n==1:
        return n
    a, b = 1, 1
    _ = 2
    while _ < n:
        a, b = a + b, a
        _ += 1
    return a

for n in range(1,10):
    print('Recursive{}:{}'.format(n, fibonacci_rec(n)))
    print(f'Iterative{n}:{fibonacci_iter(n)}')
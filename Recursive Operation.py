import sys
sys.setrecursionlimit(10**6)
def factorial(n):
    if (n<0 or int(n)!=n):
        return 'Not defined'
    if (n==1 or n==0):
        return 1
    else:
            return n*factorial(n-1)
f = int(input('Enter the number:\n'))
print('factorial of a given number: ',factorial(f))

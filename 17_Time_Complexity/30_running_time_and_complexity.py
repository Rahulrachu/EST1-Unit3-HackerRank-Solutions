# HackerRank: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
def p(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
for _ in range(int(input())):
    print('Prime' if p(int(input())) else 'Not prime')
# HackerRank: https://www.hackerrank.com/challenges/the-power-sum/problem
X=int(input());N=int(input())
def f(x,b):
    v=b**N
    if v>x:
        return 0
    if v==x:
        return 1
    return f(x-v,b+1)+f(x,b+1)
print(f(X,1))
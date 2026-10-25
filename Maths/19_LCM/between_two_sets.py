# HackerRank: https://www.hackerrank.com/challenges/between-two-sets/problem
from math import gcd
from functools import reduce
input();a=list(map(int,input().split()));b=list(map(int,input().split()))
l=reduce(lambda x,y:x*y//gcd(x,y),a);g=reduce(gcd,b)
print(sum(1 for m in range(l,g+1,l) if g%m==0))
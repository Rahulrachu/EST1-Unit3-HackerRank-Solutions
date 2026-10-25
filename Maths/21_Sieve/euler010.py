# HackerRank: https://www.hackerrank.com/challenges/euler010/problem
import sys
L=1000001;s=bytearray([1])*L;s[0]=s[1]=0
for i in range(2,1001):
    if s[i]:
        s[i*i::i]=bytearray(len(range(i*i,L,i)))
ps=[0]*L;t=0
for i in range(L):
    if s[i]:
        t+=i
    ps[i]=t
d=sys.stdin.read().split();print('\n'.join(str(ps[int(x)]) for x in d[1:]))
# HackerRank: https://www.hackerrank.com/challenges/crush/problem
import sys
d=sys.stdin.buffer.read().split();n=int(d[0]);m=int(d[1]);a=[0]*(n+2)
for i in range(m):
    p=int(d[2+3*i]);q=int(d[3+3*i]);k=int(d[4+3*i]);a[p]+=k;a[q+1]-=k
s=0;b=0
for v in a:
    s+=v
    if s>b:
        b=s
print(b)
# HackerRank: https://www.hackerrank.com/challenges/power-of-large-numbers/problem
import sys
M=1000000007
d=sys.stdin.read().split()
o=[]
for i in range(int(d[0])):
    a=d[1+2*i];b=d[2+2*i];x=0;e=0
    for c in a:
        x=(x*10+ord(c)-48)%M
    for c in b:
        e=(e*10+ord(c)-48)%(M-1)
    o.append(str(0 if x==0 else pow(x,e,M)))
print('\n'.join(o))

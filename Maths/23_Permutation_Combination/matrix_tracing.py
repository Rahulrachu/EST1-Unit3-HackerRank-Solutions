# HackerRank: https://www.hackerrank.com/challenges/matrix-tracing/problem
import sys
M=1000000007;d=sys.stdin.read().split();t=int(d[0]);q=[(int(d[1+2*i]),int(d[2+2*i])) for i in range(t)];N=max(m+n for m,n in q)
f=[1]*N
for i in range(1,N):
    f[i]=f[i-1]*i%M
o=[]
for m,n in q:
    o.append(f[m+n-2]*pow(f[m-1],M-2,M)%M*pow(f[n-1],M-2,M)%M)
print('\n'.join(map(str,o)))
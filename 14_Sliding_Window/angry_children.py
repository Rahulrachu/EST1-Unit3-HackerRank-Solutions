# HackerRank: https://www.hackerrank.com/challenges/angry-children/problem
n=int(input());k=int(input());a=sorted(int(input()) for _ in range(n))
print(min(a[i+k-1]-a[i] for i in range(n-k+1)))
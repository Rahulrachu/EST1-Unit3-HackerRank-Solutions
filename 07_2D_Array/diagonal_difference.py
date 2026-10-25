# HackerRank: https://www.hackerrank.com/challenges/diagonal-difference/problem
n=int(input());g=[list(map(int,input().split())) for _ in range(n)]
print(abs(sum(g[i][i]-g[i][n-1-i] for i in range(n))))
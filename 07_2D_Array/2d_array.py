# HackerRank: https://www.hackerrank.com/challenges/2d-array/problem
g=[list(map(int,input().split())) for _ in range(6)]
print(max(g[i][j]+g[i][j+1]+g[i][j+2]+g[i+1][j+1]+g[i+2][j]+g[i+2][j+1]+g[i+2][j+2] for i in range(4) for j in range(4)))
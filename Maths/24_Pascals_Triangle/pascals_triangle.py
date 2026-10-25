# HackerRank: https://www.hackerrank.com/challenges/pascals-triangle/problem
n=int(input());r=[1]
for i in range(n):
    print(*r);r=[1]+[r[j]+r[j+1] for j in range(len(r)-1)]+[1]

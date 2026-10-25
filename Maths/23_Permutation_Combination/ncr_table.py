# HackerRank: https://www.hackerrank.com/challenges/ncr-table/problem
R=[[1]]
for n in range(1,1000):
    p=R[-1];R.append([1]+[(p[i]+p[i+1])%1000000000 for i in range(n-1)]+[1])
for _ in range(int(input())):
    print(*R[int(input())])
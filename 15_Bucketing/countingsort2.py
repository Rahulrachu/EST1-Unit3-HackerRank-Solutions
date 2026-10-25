# HackerRank: https://www.hackerrank.com/challenges/countingsort2/problem
input();c=[0]*100
for x in input().split():
    c[int(x)]+=1
print(*[i for i in range(100) for _ in range(c[i])])
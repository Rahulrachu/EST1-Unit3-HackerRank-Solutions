# HackerRank: https://www.hackerrank.com/challenges/countingsort1/problem
input();c=[0]*100
for x in input().split():
    c[int(x)]+=1
print(*c)
# HackerRank: https://www.hackerrank.com/challenges/recursive-digit-sum/problem
n,k=input().split();p=sum(map(int,n))*int(k)
while p>9:
    p=sum(map(int,str(p)))
print(p)
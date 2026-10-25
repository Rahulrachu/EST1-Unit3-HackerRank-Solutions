# HackerRank: https://www.hackerrank.com/challenges/compare-the-triplets/problem
a=list(map(int,input().split()));b=list(map(int,input().split()))
print(sum(x>y for x,y in zip(a,b)),sum(x<y for x,y in zip(a,b)))
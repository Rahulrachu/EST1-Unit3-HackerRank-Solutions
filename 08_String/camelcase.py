# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem
s=input().strip()
print(1+sum(c.isupper() for c in s))
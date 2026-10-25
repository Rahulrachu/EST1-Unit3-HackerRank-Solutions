# HackerRank: https://www.hackerrank.com/challenges/plus-minus/problem
n=int(input());a=list(map(int,input().split()))
print('%.6f'%(sum(x>0 for x in a)/n));print('%.6f'%(sum(x<0 for x in a)/n));print('%.6f'%(sum(x==0 for x in a)/n))
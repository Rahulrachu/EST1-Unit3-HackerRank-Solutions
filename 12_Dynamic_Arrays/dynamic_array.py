# HackerRank: https://www.hackerrank.com/challenges/dynamic-array/problem
n,q=map(int,input().split());arr=[[] for _ in range(n)];last=0;out=[]
for _ in range(q):
    t,x,y=map(int,input().split());i=(x^last)%n
    if t==1:
        arr[i].append(y)
    else:
        last=arr[i][y%len(arr[i])];out.append(str(last))
print('\n'.join(out))
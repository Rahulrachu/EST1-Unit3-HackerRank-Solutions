# HackerRank: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
n,d=map(int,input().split());e=list(map(int,input().split()));c=[0]*201;r=0
for x in e[:d]:
    c[x]+=1
def med2():
    s=0;a=None
    for v in range(201):
        s+=c[v]
        if d%2:
            if s>=d//2+1:
                return 2*v
        else:
            if a is None and s>=d//2:
                a=v
            if s>=d//2+1:
                return a+v
for i in range(d,n):
    if e[i]>=med2():
        r+=1
    c[e[i-d]]-=1;c[e[i]]+=1
print(r)
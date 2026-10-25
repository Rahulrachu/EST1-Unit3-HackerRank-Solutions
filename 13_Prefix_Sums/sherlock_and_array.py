# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-array/problem
for _ in range(int(input())):
    input();a=list(map(int,input().split()));t=sum(a);l=0;r='NO'
    for x in a:
        if 2*l==t-x:
            r='YES';break
        l+=x
    print(r)
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem
for _ in range(int(input())):
    s=input().strip();a=[ord(c) for c in s];d=[abs(a[i+1]-a[i]) for i in range(len(a)-1)]
    print('Funny' if d==d[::-1] else 'Not Funny')
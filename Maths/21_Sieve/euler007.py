# HackerRank: https://www.hackerrank.com/challenges/euler007/problem
L=110000;s=bytearray([1])*L;s[0]=s[1]=0
for i in range(2,int(L**0.5)+1):
    if s[i]:
        s[i*i::i]=bytearray(len(range(i*i,L,i)))
P=[i for i in range(L) if s[i]]
for _ in range(int(input())):
    print(P[int(input())-1])
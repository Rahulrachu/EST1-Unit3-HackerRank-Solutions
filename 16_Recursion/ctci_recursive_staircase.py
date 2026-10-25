# HackerRank: https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
w=[1,1,2]
for i in range(3,40):
    w.append(w[-1]+w[-2]+w[-3])
for _ in range(int(input())):
    print(w[int(input())])
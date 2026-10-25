# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem
s=input().lower()
print('pangram' if set('abcdefghijklmnopqrstuvwxyz')<=set(s) else 'not pangram')
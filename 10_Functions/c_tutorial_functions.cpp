// HackerRank: https://www.hackerrank.com/challenges/c-tutorial-functions/problem
#include<cstdio>
int max_of_four(int a,int b,int c,int d){int m=a;if(b>m)m=b;if(c>m)m=c;if(d>m)m=d;return m;}
int main(){int a,b,c,d;scanf("%d %d %d %d",&a,&b,&c,&d);printf("%d",max_of_four(a,b,c,d));return 0;}

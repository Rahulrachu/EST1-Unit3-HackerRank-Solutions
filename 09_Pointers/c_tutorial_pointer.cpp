// HackerRank: https://www.hackerrank.com/challenges/c-tutorial-pointer/problem
#include<cstdio>
#include<cstdlib>
void update(int*a,int*b){int s=*a+*b;int d=abs(*a-*b);*a=s;*b=d;}
int main(){int a,b;scanf("%d %d",&a,&b);update(&a,&b);printf("%d\n%d",a,b);return 0;}

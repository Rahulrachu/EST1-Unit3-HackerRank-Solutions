// HackerRank: https://www.hackerrank.com/challenges/small-triangles-large-triangles/problem
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
struct triangle{int a;int b;int c;};
double ar(struct triangle t){double p=(t.a+t.b+t.c)/2.0;return p*(p-t.a)*(p-t.b)*(p-t.c);}
int cmp(const void*x,const void*y){double u=ar(*(struct triangle*)x),v=ar(*(struct triangle*)y);return (u>v)-(u<v);}
int main(){int n;scanf("%d",&n);struct triangle*t=malloc(n*sizeof(struct triangle));for(int i=0;i<n;i++)scanf("%d%d%d",&t[i].a,&t[i].b,&t[i].c);qsort(t,n,sizeof(struct triangle),cmp);for(int i=0;i<n;i++)printf("%d %d %d\n",t[i].a,t[i].b,t[i].c);return 0;}

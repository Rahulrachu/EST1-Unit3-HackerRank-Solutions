// HackerRank: https://www.hackerrank.com/challenges/deque-stl/problem
#include<cstdio>
#include<deque>
int main(){int t;scanf("%d",&t);while(t--){int n,k;scanf("%d %d",&n,&k);int*a=new int[n];for(int i=0;i<n;i++)scanf("%d",&a[i]);std::deque<int>d;for(int i=0;i<n;i++){while(!d.empty()&&d.front()<=i-k)d.pop_front();while(!d.empty()&&a[d.back()]<=a[i])d.pop_back();d.push_back(i);if(i>=k-1)printf("%d ",a[d.front()]);}printf("\n");delete[]a;}return 0;}

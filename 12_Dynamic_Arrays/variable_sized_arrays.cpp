// HackerRank: https://www.hackerrank.com/challenges/variable-sized-arrays/problem
#include<cstdio>
#include<vector>
int main(){int n,q;scanf("%d %d",&n,&q);std::vector<std::vector<int>>a(n);for(int i=0;i<n;i++){int k;scanf("%d",&k);a[i].resize(k);for(int j=0;j<k;j++)scanf("%d",&a[i][j]);}while(q--){int i,j;scanf("%d %d",&i,&j);printf("%d\n",a[i][j]);}return 0;}

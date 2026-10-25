// HackerRank: https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem
#include<iostream>
int main(){int a,b;std::cin>>a>>b;const char*w[]={"","one","two","three","four","five","six","seven","eight","nine"};for(int i=a;i<=b;i++){if(i<=9)std::cout<<w[i]<<"\n";else if(i%2==0)std::cout<<"even\n";else std::cout<<"odd\n";}return 0;}

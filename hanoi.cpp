#include<stdio.h>

void move(int n,char getone,char putone)
{
printf("move disk %d from %c-->%c\n",n,getone,putone);
}
void hanoi(int n,char one,char two,char three)
{
if(n==1)move(n,one,three);
else{
hanoi(n-1,one,three,two);    
move(n,one,three);             
hanoi(n-1,two,one,three);    
}
}
void main()
{
int m;
printf("input the number of diskes:");
scanf("%d",&m);
printf("the step to moving %3d diskes:\n",m);
hanoi(m,'A','B','C');
}

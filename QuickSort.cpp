#include <iostream>
#include <algorithm>
using namespace std;
template <typename EleType>
int Quick_Sort(EleType A[],int left,int right)
{
	EleType tmp=A[(left+right)/2];
	int i=left;
	int j=right;
	do{
		
		while(A[i]<tmp && i<right) i++;
		while(A[j]>tmp && j>left) j--;
		if(i<=j){
			swap(A[i],A[j]);
			i++;
			j--;
		}
	}while(i<=j);
	//recursively sort
	if(left<j)Quick_Sort(A,left,j);
	if(i<right)Quick_Sort(A,i,right);
	return 1;
}

int main(){
	double A[]={22.9,10.8,18,2,45.7};
	Quick_Sort(A,0,4);
	for(int i=0;i<5;i++)
		cout<<A[i]<<" ";
	cout<<endl;
	return 0;
}
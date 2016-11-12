#include<stdio.h>

int left(int i)
{
	return i*2+1;
}

int right(int i)
{
	return i*2+2;
}

void max_heapify(int A[],int i,int length)
{
	int l=left(i);
	int r=right(i);
	int largest=-1;
	if(l<length && A[l]>A[i])
		largest=l;
	else
		largest=i;
	if(r<length && A[r]>A[largest])
		largest=r;
	if(largest!=i)
	{
		int temp;
		temp=A[i];
		A[i]=A[largest];
		A[largest]=temp;
		max_heapify(A,largest,length);
	}
}

void build_max_heap(int A[],int length)
{
	for(int i=length/2-1;i>=0;i--)
	{
		max_heapify(A,i,length);
	}
}

void heap_sort(int A[],int length)
{
	int n=length-1;
	int temp;
	while(n>=0)
	{
		printf("%d ",A[0]);
		temp=A[0];
		A[0]=A[n];
		A[n]=temp;
		n--;
		max_heapify(A,0,n+1);
	}
	printf("\n");
}


int main()
{
	int A[]={4,1,3,2,16,9,10,14,8,7};
	int length=sizeof(A)/sizeof(int);
	build_max_heap(A,length);
	for(int i=0;i<length;i++)
		printf("%d ",A[i]);
	printf("\n");
	heap_sort(A,length);
	return 0;
}
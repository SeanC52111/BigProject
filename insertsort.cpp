#include <iostream>
using namespace std;
int main()
{
	int a[10]={0,29,10,33,14,98,74,22,90,10};
	for (int i=2;i<=10;i++)
	{
		int j=i-1;
		a[0]=a[i];
		while(a[0]<a[j])
		{
			a[j+1]=a[j];
			a[j]=a[0];
			j--;
			for(int k=0;k<10;k++)
				cout<<a[k]<<" ";
			cout<<endl;
		}
	}
	
	return 0;
}


#include <iostream>
#include <cmath>
using namespace std;
int count=0;
int calbin()
{
	char c;
	cin>>c;
	
	if(c!='#'){
		return calbin()+(c-48)*pow(2,count++);
	}
	else
		return 0;
}
int main()
{
	cout<<calbin();
	return 0;
}


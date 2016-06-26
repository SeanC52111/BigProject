#include <iostream>
using namespace std;

char A[4][4]={{' ',' ',' ',' '},{' ','1',' ',' '},{' ',' ','1',' '},{' ',' ',' ',' '}}; 
int dir[8][2]={0,1,0,-1,1,0,-1,0,1,1,1,-1,-1,1,-1,-1};
int find;
int judge(int x,int y,int n);
void DFS(int x,int y,int n);
int main()
{
	int n;
	cin>>n;
	DFS(0,0,n);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
			cout<<A[i][j]<<" ";
		cout<<endl;
	}
	return 0;
}

void DFS(int x,int y,int n)//核心函数
{
	A[x][y]='o';//记录路径
	if(x==3&&y==3)//找到的话标记find为找到
	{find=1;return;}
	for(int i=0;i<8;i++)//探索四个方向
	{
		int sx=x+dir[i][0],sy=y+dir[i][1];
		if(judge(sx,sy,n)&&A[sx][sy]==' ')
		{
			cout<<sx<<" "<<sy<<endl;
			DFS(sx,sy,n);
			if(!find)//根据情况进行反标记
				A[sx][sy]=' ';//未找到就反标记
			else//找到的话就直接返回保存路径
				return;
		}
	}
}


int judge(int x,int y,int n)
{
	return x>=0 && x<n && y>=0 && y<n;
}

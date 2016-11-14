#include<stdio.h>
#include<malloc.h>
typedef struct{
	char data;
	int lchild;
	int rchild;
}TNode;

TNode Tree[9]={{'A',1,2},{'B',3,-1},{'C',4,5},{'D',-1,-1},
	{'E',-1,6},{'F',7,8},{'G',-1,-1},{'H',-1,-1},{'I',-1,-1}};

void inorder(TNode T)
{
	if(T.lchild!=-1)
		inorder(Tree[T.lchild]);
	printf("%c",T.data);
	if(T.rchild!=-1)
		inorder(Tree[T.rchild]);
}

int count(TNode T)
{
	int num1=0,num2=0;
	if(T.lchild==-1 && T.rchild==-1)
		return 1;
	if(T.lchild!=-1)
		num1=count(Tree[T.lchild]);
	if(T.rchild!=-1)
		num2=count(Tree[T.rchild]);

	return (num1+num2+1);
}

int countleaf(TNode T)
{
	int num1=0,num2=0;
	if(T.lchild==-1 && T.rchild==-1)
		return 1;
	if(T.lchild!=-1)
		num1=countleaf(Tree[T.lchild]);
	if(T.rchild!=-1)
		num2=countleaf(Tree[T.rchild]);
	return num1+num2;
}

int depth(TNode T)
{
	int leftdep=0,rightdep=0;
	if(T.lchild==-1 && T.rchild==-1)
		return 0;
	if(T.lchild!=-1)
		leftdep=depth(Tree[T.lchild]);
	if(T.rchild!=-1)
		rightdep=depth(Tree[T.rchild]);
	return (leftdep>rightdep)?(leftdep+1):(rightdep+1);
}

int main()
{
	inorder(Tree[0]);
	printf("\n");
	printf("count:%d\n",count(Tree[0]));
	printf("leaf node count:%d\n",countleaf(Tree[0]));
	printf("depth:%d\n",depth(Tree[0]));
	return 0;
}
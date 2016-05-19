/**
 * @(#)Propose.java
 *
 * Propose application
 *
 * @author Sean Chang 
 * @version 1.00 2016/3/30
 */
import java.util.*; 
public class Propose {
    public static void pro(int n,int[][]man,int[][]w)
    {
    	//inverse array w[][]
    	int tw[][]=new int[n][n];
    	int i,j;
    	for(i=0;i<n;i++)
    	{
    		for(j=0;j<n;j++)
    		{
    			int tm=w[i][j];
    			tw[i][tm]=j;
    		}
    	}
    	w=tw;
    	//set the initial mnext and wcur
    	int mnext[]=new int[n];
    	int wcur[]=new int[n];
    	for(i=0;i<wcur.length;i++)
    	{
    		wcur[i]=-1;
    	}
    	//set the initial stack of man
    	myStack mstack=new myStack();
    	for(i=0;i<n;i++)
    	{
    		mstack.push(i);
    	}
    	while(!mstack.isEmpty())
    	{
    		if(wcur[man[mstack.getFirst()][mnext[mstack.getFirst()]]]==-1)//the girl is free
    		{
    			wcur[man[mstack.getFirst()][mnext[mstack.getFirst()]]]=mstack.getFirst();
    			mnext[mstack.getFirst()]++;
    			mstack.pop();
    		}
    		//girl select between the current man and her fiance
    		else if(w[man[mstack.getFirst()][mnext[mstack.getFirst()]]][wcur[man[mstack.getFirst()][mnext[mstack.getFirst()]]]]>w[man[mstack.getFirst()][mnext[mstack.getFirst()]]][mstack.getFirst()])
    		{
    			int temp=wcur[man[mstack.getFirst()][mnext[mstack.getFirst()]]];
    			wcur[man[mstack.getFirst()][mnext[mstack.getFirst()]]]=mstack.getFirst();
    			mnext[mstack.getFirst()]++;
    			mstack.pop();
    			mstack.push(temp);
    		}
    		else{
    			mnext[mstack.getFirst()]++;
    		}
    	}
    	//output
    	for(i=0;i<wcur.length;i++)
    	{
    		System.out.println (i+" th girl marries "+wcur[i]+"th boy");
    	}
    	
    }
    public static int index(int[] t,int i)
    {
    	for(int j=0;j<t.length;j++)
    	{
    		if(t[j]==i)
    			return j;	
    	}
    	return -1;
    }
    public static void main(String[] args) {
    	//int man[][]={{0,1,3,2},{0,2,3,1},{3,0,2,1},{0,3,1,2}};
    	//int w[][]={{3,0,1,2},{3,2,1,0},{3,2,0,1},{2,3,0,1}};
    	//pro(4,man,w);
    	int num=0;
    	
    	do{
    		System.out.println ("please enter the number of man:");
    		Scanner rd=new Scanner(System.in);
    		num=rd.nextInt();
    	}while(num<1);
    	int man[][]=new int[num][num];
    	int w[][]=new int[num][num];
    	int i,j;
    	for(i=0;i<num;i++)
    	{
    		System.out.println ("第"+i+"位男士喜欢女生顺序:");
 			Scanner rd=new Scanner(System.in);
    		for(j=0;j<num;j++)
    		{
    			man[i][j]=rd.nextInt();	
    		}
    	}
    	for(i=0;i<num;i++)
    	{
    		System.out.println ("第"+i+"位女士喜欢男士顺序:");
 			Scanner rd=new Scanner(System.in);
    		for(j=0;j<num;j++)
    		{
    			w[i][j]=rd.nextInt();	
    		}
    	}
    	pro(num,man,w);
    }
    	
    	
}

//user defining stack
class myStack{
	private LinkedList<Integer> ld=new LinkedList<Integer>();
	public void push(int n)
	{
		ld.addFirst(n);
	}
	public int pop()
	{
		return ld.removeFirst();
	}
	public boolean isEmpty()
	{
		return ld.isEmpty();
	}
	public int getFirst()
	{
		return ld.getFirst();
	}
}
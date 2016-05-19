n=5
man=[[1,3,0,4,2],[2,1,4,3,0],[1,0,3,2,4],[0,4,1,2,3],[0,2,1,3,4]]
w=[[3,0,2,1,4],[1,0,4,3,2],[0,1,2,3,4],[4,0,2,1,3],[0,2,3,1,4]]
tw=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.insert(j,w[i].index(j))
    tw.insert(i,temp)
w=tw
mnext=[]
for j in range(n):
    mnext.insert(j,0)

wcur=[]
for k in range(n):
    wcur.insert(k,-1)
stack=[]
for l in range(n):
    stack.insert(l,l)

while(len(stack)>0):
    if(wcur[man[stack[0]][mnext[stack[0]]]]==-1):
        wcur[man[stack[0]][mnext[stack[0]]]]=stack[0]
        mnext[stack[0]]=mnext[stack[0]]+1
        stack.pop(0)
    elif(w[man[stack[0]][mnext[stack[0]]]][wcur[man[stack[0]][mnext[stack[0]]]]]>w[man[stack[0]][mnext[stack[0]]]][stack[0]]):
        temp=wcur[man[stack[0]][mnext[stack[0]]]]
        wcur[man[stack[0]][mnext[stack[0]]]]=stack[0]
        mnext[stack[0]]=mnext[stack[0]]+1
        stack.pop(0)
        stack.insert(0,temp)
    else:
        mnext[stack[0]]=mnext[stack[0]]+1
for p in range(len(wcur)):
    print("the {0:3d}'th girl  marries the {1:3d}'th boy".format(p,wcur[p])) 

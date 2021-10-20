from NonIntersectingRandomWalk import *
def MarbleRun(n,k,x=1000,y=1000,walkalgo=None,loud=False,visualize=False):
    validrun=False;
    while(not validrun):
        grid,pos,steps=RandomWalkNonIntersect(False,x,y,maxsteps=n*k,legalposcheck=PureLegalPosCheck)
        if(steps==n*k):
            validrun=True
    coords=[]
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if(grid[i][j]%n==1):
                grid[i][j]=1
                coords.append([i,j])
            else:
                grid[i][j]=0
    #pass coords to util.findColinearLine() and find longest line
        
        

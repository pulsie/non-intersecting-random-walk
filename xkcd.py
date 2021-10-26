from NonIntersectingRandomWalk import *
from util import *
def MarbleRun(n,k,x=1000,y=1000,loud=False,visualize=False):
    validrun=False;
    while(not validrun):
        grid,pos,steps=RandomWalkNonIntersect(False,x,y,maxsteps=n*k,legalposcheck=PureLegalPosCheck)
        if(steps==n*k):
            validrun=True
            if(loud):print("found")
        if(loud):print("tried with "+str(steps))
        if(loud):print(grid[0][0])
    coords=[]
    if(loud):print("run made")
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if(not n==1):
                if(grid[i][j]%n==1):
                    grid[i][j]=1
                    coords.append([i,j])
                else:
                    grid[i][j]=0
            else:
               if(not grid[i][j]==0):
                    grid[i][j]=1
                    coords.append([i,j]) 
    #pass coords to util.findColinearLine() and find longest line
    if(visualize):
        VisualizeGrid(grid,pos,loud) #TODO: make special marble visualizer
    if(loud):
        print(coords)
        print(pos)
        print(len(coords))
    return findColinearLineLength(coords)
if(__name__ == "__main__"):
    MarbleRun(2,2,x=10,y=10,loud=False,visualize=True)

import random
from copy import copy
from tkinter import *
def VisualizeGrid(grid,finalpos):
    #https://www.geeksforgeeks.org/create-table-using-tkinter/ was useful
    root=Tk()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            if(i==finalpos[0] and j==finalpos[1]):
                entry=Entry(root,fg='red')
                entry.grid(row=i, column=j)
                entry.insert(END,"FINAL")
            elif(grid[i][j]==0):
                entry=Entry(root,fg='white')
                entry.grid(row=i, column=j)
                entry.insert(END,"")
            else:
                entry=Entry(root,fg='green')
                entry.grid(row=i, column=j)
                entry.insert(END,grid[i][j])
    root.mainloop()
def OneAheadPosCheck(pos,grid,loud,step,maxsteps):
    '''
    return PureLegalPosCheck(pos,grid,loud) and       \
    (PureLegalPosCheck([pos[0]+1,pos[1]],grid,loud or \
    PureLegalPosCheck([pos[0]-1,pos[1]],grid,loud) or \
    PureLegalPosCheck([pos[0],pos[1]+1],grid,loud) or \
    PureLegalPosCheck([pos[0],pos[1]-1],grid,loud)))'''
    return PureLegalPosCheck(pos,grid,loud,step,maxsteps)             \
    and (PureLegalPosCheck([pos[0]+1,pos[1]],grid,loud,step,maxsteps) \
    or PureLegalPosCheck([pos[0]-1,pos[1]],grid,loud,step,maxsteps)   \
    or PureLegalPosCheck([pos[0],pos[1]+1],grid,loud,step,maxsteps)   \
    or PureLegalPosCheck([pos[0],pos[1]-1],grid,loud,step,maxsteps))  
def PureLegalPosCheck(pos, grid, loud,step,maxsteps):
    return pos[0]>-1 and pos[0]<len(grid) and pos[1]>-1 and pos[1]<len(grid[0]) and grid[pos[0]][pos[1]]==0
def SearchNAheadPosCheck(pos,grid,loud,step,maxsteps,n,fullRandomComp=False):
    #do things idk
    if(fullRandomComp):
        return SearchNAheadPosCheck(pos,grid,loud,step,maxsteps,floor(n,maxsteps-steps+1))
    if(n>0):
        return PureLegalPosCheck(pos,grid,loud,step+1,maxsteps)             \
        and (SearchNAheadPosCheck([pos[0]+1,pos[1]],grid,loud,step+1,n-1,maxsteps) \
        or PureLegalPosCheck([pos[0]-1,pos[1]],grid,loud,step+1,n-1,maxsteps)   \
        or PureLegalPosCheck([pos[0],pos[1]+1],grid,loud,step+1,n-1,maxsteps)   \
        or PureLegalPosCheck([pos[0],pos[1]-1],grid,loud,step+1,n-1,maxsteps))
    else:
        return PureLegalPosCheck(pos,grid,loud,step+1,maxsteps)
def RandomWalkNonIntersect(visualize,x,y,maxsteps=float("inf"),loud=False,legalposcheck=PureLegalPosCheck):
    steps=0;
    dirlist=[1,2,3,4] #i know i should use enum but idc
    grid=[]
    for i in range(0,x):
        grid.append([])
        for j in range(0,y):
            grid[i].append(0)
    currentpos=[x//2,y//2]
    grid[x//2][y//2]=1;
    while(steps<maxsteps):
        random.shuffle(dirlist)
        generatedDirection=False;
        steps=steps+1
        for j in dirlist:
            
            possiblenewpos=copy(currentpos)
            if(j==1):
                # go left
                possiblenewpos[0]=possiblenewpos[0]+1
            elif(j==2):
                # go up
                possiblenewpos[1]=possiblenewpos[1]+1
            elif(j==3):
                #go right
                possiblenewpos[0]=possiblenewpos[0]-1
            else:
                #go down
                possiblenewpos[1]=possiblenewpos[1]-1
            if(legalposcheck(possiblenewpos,grid,loud,steps,maxsteps)):
                    currentpos=possiblenewpos
                    if(loud):print(currentpos)
                    
                    generatedDirection=True
                    grid[currentpos[0]][currentpos[1]]=steps+1
                    break;
        if(not generatedDirection):
            if(loud):print("stuck")
            break;
    if(visualize):
        VisualizeGrid(grid,currentpos)

    if(loud):print("did "+str(steps)+" steps")
    
    return [grid,copy(currentpos),steps]


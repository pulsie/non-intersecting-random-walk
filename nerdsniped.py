import random
from copy import copy
from tkinter import *
def main(visualize,x,y,maxsteps):
    grid=[]
    for i in range(0,x):
        grid.append([])
        for j in range(0,y):
            grid[i].append(0)
    currentpos=[x//2,y//2]
    grid[x//2][y//2]=1;
    steps=0;
    dirlist=[1,2,3,4] #i know i should use enum but idc
    def legalpos(pos):
        if(pos[0]<0 or pos[1]<0):
            return False;
        if(pos[0]>len(grid)-1 or pos[1]>len(grid[0])-1):
            return False;
        if(not grid[pos[0]][pos[1]]==0):
            return False;
        try:
            if(grid[pos[0]+1][pos[1]]==0):
                return True
        except:
            print("edge hit")
        try:
            if(grid[pos[0]-1][pos[1]]==0):
                return True
        except:
            print("edge hit")
        try:
            if(grid[pos[0]][pos[1]+1]==0):
                return True
        except:
            print("edge hit")
        try:
            if(grid[pos[0]][pos[1]-1]==0):
                return True
        except:
            print("edge hit")
        
        
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
            if(legalpos(possiblenewpos)):
                    currentpos=possiblenewpos
                    print(currentpos)
                    
                    generatedDirection=True
                    grid[currentpos[0]][currentpos[1]]=steps+1
                    break;
        if(not generatedDirection):
            print("stuck")
            break;
    if(visualize):
        root=Tk()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if(i==currentpos[0] and j==currentpos[1]):
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

    print("did "+str(steps)+" steps")

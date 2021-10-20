from NonIntersectingRandomWalk import *
import numpy as np
import time
import gc
import csv
stepList=[]
execstart=time.time()
for i in range(0,100000):
    start=time.time()
    stepList.append(RandomWalkNonIntersect(False,2000,2000,loud=False,legalposcheck=OneAheadPosCheck)[2])
    end=time.time()
    print(str(end-start)+"time")
    print(i)
execend=time.time()
print("time taken: "+str(execend-execstart))
print(np.average(stepList))
# from https://www.kite.com/python/answers/how-to-write-a-list-to-a-file-in-python
output = open("output_smartalgo.txt", "w")
for element in stepList:
    output.write(str(element) + "\n")
output.close()
input("press enter to exit")

from collections import Counter
def findColinearLineLength(points):
    lineLengths=[]
    #longestLineLength=0;
    for pt in points:
        counter=Counter({})
        for pt2 in points:
            if(pt[0]==pt2[0] and pt[1]==pt2[1]):
                continue
            if(pt[0]==pt2[0]):
                slope=float("inf")
            else:
                slope=(pt2[1]-pt[1])/(pt2[0]-pt[0])
            counter[slope]+=1
        longestLineLength=counter.most_common(1)[0][1]+1
        print(longestLineLength)
        lineLengths.append(longestLineLength)
    return max(lineLengths)

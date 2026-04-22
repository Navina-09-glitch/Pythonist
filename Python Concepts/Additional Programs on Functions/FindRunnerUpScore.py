def getscores():
    scores=[]
    noc=int(input("enter number of scores"))
    if(noc<=0):
        return scores
    else:
        for x in range(1,noc+1):
            scores.append(int(input("enter score {}".format(x))))
        else:
            return scores
def getrunnerupscore():
    scores=getscores()
    if(len(scores)==0):
        print("no scores found")
    else:
        score=sorted(set(scores))
        print("Unique Score Values")
        print(score)
        print("Runner Up Score={}".format(scores[-2a]))
#main program
getrunnerupscore()
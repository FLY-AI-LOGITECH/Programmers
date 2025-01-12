def solution(bandage, health, attacks):
    answer = 0
    turn = attacks[-1][0]+1
    count=0
    maxh=health
    j=0
    for i in range(1,turn):
        if(i==attacks[j][0]):
            health-=attacks[j][1]
            count=0
            j+=1
            if(health<=0):
                return -1
        else:
            count+=1
            if(count==bandage[0]):
                health+=bandage[2]
                count=0
            health+=bandage[1]
            if(health>maxh):
                health=maxh
    return health
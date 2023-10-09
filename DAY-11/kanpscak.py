def knapsack(l,capacity):
    # print(list(l))
    # pwratio=[]
    # for i in range(0,len(weights)):
    #     pwratio.append(profits[i] / weights[i])
    # a=list(zip(weights,profits))
    l=list(l)
    l.sort(key=lambda x:x[1]/x[0],reverse=True)
    k=[]
    i=0
    profit=0
    while True:
        if capacity<=0:
            break
        k.append(l[i])
        i+=1
        capacity-=l[i][0]
        profit+=l[i][1]
    print(k)
    return profit
        
capacity=int(input())
weights=list(map(int,input().split()))
profits=list(map(int,input().split()))
l=zip(weights,profits)
print(knapsack(l,capacity))
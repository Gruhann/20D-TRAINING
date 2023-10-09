
def maxProfit(l):
    mprofit=0
    buy=l[0]
    for i in l:
        if i<buy:
            buy=i
        elif i-buy>mprofit:
            mprofit=i-buy
    return mprofit
n=list(map(int,input().split()))
print(maxProfit(n))

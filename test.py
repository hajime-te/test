
if __name__=="__main__":    
    n,S=list(map(int,input().split()))
    a=list(map(int,input().split()))
    l=0
    r=n+1
    while(r>l+1):
        k=-(-(l+r)//2)
        cost=0
        a_new=[a[i]+(i+1)*k for i in range(n)]
        a_new.sort()
        for i in range(k):
            cost+=a_new[i]
        if(cost<=S):
            l=k
        else:
            r=k
    a_new=[a[i]+(i+1)*l for i in range(n)]
    a_new.sort()
    cost=0
    for i in range(l):
        cost+=a_new[i]
    print(l,cost)

def nm(a,m):
    global n ,visit
    if a==m:
        for k in range(len(visit)):
            print(visit[k],end=' ')
        print()
    else:
        for i in range(1, n+1):

                visit.append(i)
                nm(a+1,m)
                visit.pop()




n,m = map(int,input().split())
visit=[]
nm(0,m)
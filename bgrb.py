

'''
def remove_dup(self, mylist=[]):
    mylist.sort()
    for i in mylist:
        if mylist[i] == mylist[i+1]:
          del i

    return (mylist)
#list=[1,2,3,2,]
#print((list.sort(reverse=False)))
#new=remove_dup(list)
#print(new)
'''


def trial(mylist):
    mylist.sort()
   # print(mylist)
    n = len(mylist)
    if n == 0 or n == 1:
        return mylist;



    #finalist=[None]*n
    #finalist=[]
    #finalist= (range(n))

    j=0
    #for i in mylist:
    for i in range (0,n-1):
        if mylist[i] != mylist[i+1]:
            mylist[j]=mylist[i]
            j+=1

    mylist[j] = mylist[n - 1]
    j += 1
    for i in range(0, j):
     mylist[j] = mylist[i]
    return mylist
list=[1,2,3,2,3,4]
#n=len(list)
print(trial(list))
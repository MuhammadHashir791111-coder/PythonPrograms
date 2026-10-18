
def ellist(list, indx=0):
    if (indx == len(list)):
        return #exit()
    print(list[indx])
    return ellist(list,indx+1)

list = ["a","b","2","3"]
print(ellist(list))
li = [1,2,3]

def adder(list):
    new_list = []
    for i in list:
        new_list.append(i+1)
    return new_list

print(adder(li))    
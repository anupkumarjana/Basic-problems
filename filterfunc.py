list1= [1,2,3,4,5,6,7,8,9]
def greater(num):
    return num>5
max= list(filter(greater, list1))
print(max)
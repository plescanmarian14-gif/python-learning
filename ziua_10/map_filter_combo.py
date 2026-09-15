list1=[1,2,3,4,5,6]
dublu=list(map(lambda x: x*2,list1))
print(dublu)
filtru=list(filter(lambda x: x%3==0,dublu))
print(filtru)
tot=list(filter(lambda x: x%3==0,map(lambda x: x*2,list1)))
print(tot)
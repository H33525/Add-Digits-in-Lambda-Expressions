from functools import reduce
   my_list= [1,2,3]

def accumulator(acc,item):

print(reduce(lambda acc,item: acc+item, my_list))
print(my_list)
import random
list = [1,2,3,4,5,6,7,8,9,14,6,4,3,3,5,3,2,4,4,4,44,4,55,]
def shuffle(list): 
  for i in range(0,len(list)):
    for i in range(0,10): 
      t1 = random.randint(0,len(list)-1)
      t2 = random.randint(0,len(list)-1)
      temp = list[t1] 
      list[t1] = list[t2]
      list[t2] = temp 
  return list 

print (list)

shuffle(list)
print (list)

total = 0

num = int(input())
if num % 5 == 0:
    total+=1
if num % 4 == 0:
    total+=1
num -=4
while num > 4:
    if num % 5 == 0:
        total+=1
    num-=4 
print(total)
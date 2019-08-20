#Program to find the even element in the list
num = 0
list1=[]
#using while loop
while(num < 10):
    a = int(input())
    list1.append(a)
    num+=1

#iterating each number in list
for num in list1:
    #checking condition
    if num % 2 == 0:
        print(num,end = " ")
        
    

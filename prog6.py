stack=[]
import sys
o=['(','[','{']
c=[')',']','}']
s=input()
for i in s:
       # print(stack)
	if i in o :
		stack.append(i)
	elif i in c :
		ch=stack[len(stack)-1]
		ch1=c[o.index(ch)]
		if ch1==i : 
			stack.pop()
		else : 
			print("invalid")
			exit()
			

if len(stack)==0 : print("valid")

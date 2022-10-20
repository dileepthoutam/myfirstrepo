f=open("prog1.txt","r")
text=f.read()
tab=0
sp=0
lines=0
char=0
spchar=0
num=0
for i in text:
	if(ord(i) in range(65,91) or ord(i) in range(97,123)):
		char+=1
	elif(ord(i)==32):
		sp+=1
	elif(i=='\n'):
		lines+=1
	elif(i=='\t'):
		tab+=1
	elif(ord(i) in range(48,58)):
		num+=1
	else:
		spchar+=1
	
print("characters: ",char)
print("digits: ",num)
print("spaces: ",sp)
print("lines: ",lines)
print("tabs: ",tab)
print("special characters: ",spchar)
f.close()



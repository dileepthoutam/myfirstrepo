f=open("prog1.txt","r")
text=f.read()
tcount,lcount=0,1
print("lcount","\t","tcount","lexim","\t","token")
for i in range(len(text)):
    tcount+=1
    if(text[i]=="="):
        token="Aop"
    elif text[i]=="+":
        token="Addop"
    elif text[i]=="-":
        token="Subop"
    elif text[i]=="*":
        token="Mulop"
    elif text[i]=="/":
        token="Divop"
    elif text[i].isalpha():
        token="id"
    elif text[i]=="\n":
        lcount+=1
    elif text[i].isdigit():
        num=text[i]
        i+=1
        while(i<len(text) and text[i].isdigit()):
            num+=text[i]
            i+=1
            print(lcount,"\t",tcount,"\t",num,"\t","num")
        break
    print(lcount,"\t",tcount,"\t",text[i],"\t",token)

	
		
		
		
		
		

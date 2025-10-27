f=open('textfile.txt','r')
count=0
count1=0
for line in f:
    if line.strip()!="":
       name= line.split()
       count1=len(name)
       count=count+1
       
     
print(count)

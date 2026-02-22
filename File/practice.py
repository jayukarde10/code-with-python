# f=open("practice.txt","w")
# f.write("hi everyone \n we are learning file \n using java\ni like programming in java")
# f.close()

# f=open("practice.txt","r")
# data=f.read()
# newdata=data.replace("java","python")
# print(newdata)

# f=open("practice.txt","w")
# f.write(newdata)

f=open("practice.txt","r")
data=f.read()
if(data.find("learning")!=-1): #Word not found -1
    print("found at ",data.find("learning"))
else:
    print("not found")
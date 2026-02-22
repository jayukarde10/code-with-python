#methods
#check at file

f=open("demo.txt","r+") # r+ read and write but it write by truncating only the space that it need that priviously available without deleting all
f.write("old changed line by r+")
# print(f.read()) #read after wrie , after the pointer

f.close()


print("______________________________")
f=open("demo.txt","w+")  #truncate all the file first

print(f.read())
f.write("after all get truncate")#check in file
#could not use read becuse pointer is at a end
f.close()

print("______________________")
f=open("demo.txt","a+") #could not read anything becuse pointer at end check file
f.write("new append at pointer is at end")
f.close()




#open ,read and close a file


# f = open("file_name","mode")

#file name --> sample.txt  , demo.docx
#mode--> r: read mode ,w: write mode


f=open("demo.txt","r")

data=f.read()
print(data)
print(type(data))
f.close()

# Mode	Meaning
# "r"	Read (error if file not exists)
# "w"	Write (creates / overwrites truncating first file then write)
# "a"	 open for write Append to the end to the existing file
# "x"	Create new file and open it for writing (error if exists)
# "rb"	Read binary
# "b"   binary mode
# "t"   text mode (defult)
# "wb"	Write binary
# "+"   open a disk file for updating (reading and writing)
        #a+ this append and read(defult)
        #w+ this write and read(defult ) 

print("----------------------")
f=open("demo.txt","r")

# data=f.read(5) #it read only first 5 char inluding step
# print(data)

line1=f.readline()  #it read the data that not get read priviously
print(line1)
line2=f.readline()
print(line2)
line3=f.readline() #after all get read it print nothing but space
print(line3)


print(type(data))
f.close()


# print("_______________________")
# f=open("demo.txt","w") #owerwrite the entire file
# f.write("new added line after truncating")
# f.close #check file

# f=open("demo.txt","a") #apeending in file
# f.write("\n new appended line without truncating")
# f.close


#to create a file 
f=open("newfilebyopenusingappend.txt","a")
f.close()



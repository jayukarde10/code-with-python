# Dictionary is a collection which is not indexed, unorder, ordered(in python 3.7+) and changeable. No duplicate key.
#ordered means The items are kept in the same order they were added.
#changeble(mutable)


dict={"key":"value"}

dict={"name":"jay",
      "age":22,
      "city":"delhi",
      "subjects":["maths","sci"], # list in dict
      "tup":(1,2,2),
       (1,2,3):"tup" }# only tuple becuse it is immutable not changeble , list  are changeble
                     # dict can use as nested dict also

print(dict)
print(dict["name"])
# print(dict[1]) not posible to call by index n0.


#to assign and add new
dict["name"]="JAY"

dict["surname"]="ukarde" #add new key value pair
print(dict)

#to delete 
del dict["age"] 
dict.pop("city") 
dict.popitem() #removes the last inserted key-value pair


null_dict={} #empty dict

#nested dict
student={
    "key":"value",
    "name":"jay",
    "age":22,
    "subjects":{
        "maths":90,
        "sci":80
    }
}

print(student["subjects"]["sci"])


#change in nested dict
student["subjects"]["sci"]=90
print(student["subjects"])

#methods
print("methods")
print(student.keys()) #return all keys 
print(len(student)) #return length 
print(student.values())#return all values
print(student.items())#return (key, val) pair
print(student.get("key"))# returns the key according to value
student.update({"city":"mumbai","dist":"maharashtra"})
print(student)## update and insert in dict




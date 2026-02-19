# Dictionary is a collection which is not indexed, unorder, ordered(in python 3.7+) and changeable. No duplicate key.
#ordered means The items are kept in the same order they were added.
#changeble(mutable)


dict={"key":"value"}

dict={"name":"jay",
      "age":22,
      "city":"delhi",
      "subjects":["maths","sci"], # list in dict
      "tup":(1,2,2),
       (1,2,3):"tup" }# only tuple becuse it is immutable not changeble , list & dict are changeble


print(dict)
print(dict["name"])
# print(dict[1]) not posible to call by index n0.


#to assign and add new
dict["name"]="JAY"

dict["surname"]="ukarde" #add new key value pair
print(dict)

null_dict={} #empty dict




 
#syntax if elif else
# if(condition):
#     statement
# elif(condition):   condition can be == < > <= >= 
#     statement
# else:
#     statement

#short ternary
#<var>=<val1>if<condition>else<val>
#<var>="yes"if food=="cake" else "no"
#or
#print("")if<condition>else print("")
#or
#<var>=(false_val,true_val)[<condition>]
#Ex .. vote=("yes","no")[age<=18]

#Ex.. tax=sal*(0.1,0.2)[sal>500000]  direct finding tax






age=int(input("age :"))
if(age<18):
    print("minor")
elif((age>=18)&(age<=30)):
    print("adult")
elif(age>60):
    print("why are you wasting oxygen")
elif(age>30):
    print("living")

else:
    print("....")

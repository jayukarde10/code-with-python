##static method it use if there are no use of self in method

class student():
    
    @staticmethod #decorator
    def college():
        print("hello")

s1=student()
s1.college()
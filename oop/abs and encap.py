##abstraction is hiding the implementation details and showing only functionality to the user
##abstraction is achieved by abstract class and interface

class car():
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.brake=False
        self.clutch=True
        print("car is start")
car1=car()
car1.start()
#avoiding to display unnessesory info from user is abstraction

#encapsulation
# capsuling/wrapping data and function into single unit
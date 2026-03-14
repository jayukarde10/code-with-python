class car:
    def __init__(self,no):
        self.no=no
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyota(car):
    def __init__(self, no,brand):
        super().__init__(no)
        self.brand=brand

class fortuner(toyota):
    def __init__(self, no, brand,type):
        super().__init__(no, brand)
        self.type=type
        super().start() #direct call of method

car1=fortuner(1,"br","diesel")
print(car1.type)
print(car1.brand)
print(car1.start())
print(car1.no)

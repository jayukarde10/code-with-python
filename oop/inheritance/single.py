class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyota(car):
    def __init__(self,brand):
        self.brand=brand

car1=toyota("br")
print(car1.brand)
print(car1.start())

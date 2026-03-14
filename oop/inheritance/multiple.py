class A:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class B:
    def __init__(self,height):
        self.height=height
        

class C(A, B):
    def __init__(self, name, color,height, weight):
        A.__init__(self, name, color)
        B.__init__(self,height)
        self.weight=weight

s=C("jay","brown",175,70)
print(s.weight)
print(s.name)
print(s.height)
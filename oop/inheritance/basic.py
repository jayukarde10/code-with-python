#inheritance syntax
# class parent:
#       .........
# class child(parent):
#       .........

class parent:
    color="brown"
    height=175
class child(parent):
    name="jay"
s=child()
print(s.color)
print(s.height)

#we can inherit property , attribute,method

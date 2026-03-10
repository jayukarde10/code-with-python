class student:
   def __init__(self,name,mark):
      self.name=name
      self.mark=mark
   def avg(self):
      avg=sum(self.mark)/3
      print("hi",self.name,"your avg is",avg)

s1=student("jay",[70,90,86])
s1.avg()
s1.name="ukarde" #to change a name only in method in same object 
s1.avg()
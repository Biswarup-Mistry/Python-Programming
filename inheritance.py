class Person:
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age=age
  def printage(self):   
  	print("and (parent)age is : ",self.age)
  def printname(self):
    print(self.firstname, self.lastname)
  #def printage1(self):   
  #	print("and (child)age is : ",self.age)
  


class Student(Person):
  #def __init__(abc, fname, lname, age):
  	pass
  #	Person.__init__(abc, fname, lname, age)

  


x = Student("Mike", "Olsen", 34)
x.printname()
x.printage()
#x.printage1()

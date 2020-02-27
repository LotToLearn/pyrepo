#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")

  def method2(self, someString):
    print("anotherClass method2")

class Person:
  name="Bob"
  age=23
  sex="Hope"
  def __init__(self):
    self.name = "Noah"
    self.age = 23
    self.sex = "Male"

def main():
  c = myClass()
  c.method1()
  c.method2("This is a string")

  c2 = anotherClass()
  c2.method1()
  c2.method2("This is a string")

  a = Person()
  print(a.name, a.age, a.sex)
  print(Person.sex, Person.age, Person.name)


  
if __name__ == "__main__":
  main()








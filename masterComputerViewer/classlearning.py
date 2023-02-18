class Person:
  def __init__(self, name, age):
    self.identity = name
    self.age = age

p1 = Person("John", 36)

print(p1.identity)
print(p1.age)
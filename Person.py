class Person:

    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def greetings(self):
        return 'Hello, my name is {}, I\'m {} years old.\n'.format(self.name, self.age)


# this calls on the structure of Person, defines a specific return method. call it using Student.greetings(p2)
class Student(Person):

    def greetings(self):
        return 'My name is {}. I\'m a student.\n'.format(self.name)


p1 = Person('Emma', 28)
p2 = Person('Omar', 40)
p3 = Person('John', 50)
p4 = Person('Corin', 50)
p5 = Person('Fred', 43)


print(p1.greetings())
print(p2.greetings())

# print the age difference using the abs() method which returns the absolute number
print(f'The difference between our ages is {abs(p1.age - p2.age)} years')

print('The number of instances of Person Class are: {}'.format(Person.count))

s1 = Student('John The Baptist', 6)

print(Student.greetings(p2))

print(s1.greetings())


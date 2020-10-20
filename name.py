class Name:

    def __init__(self, name):
        self.name = name

    def greetings(self):
        return 'Hello {}, it is lovely to meet you.'.format(self.name)


name1 = Name(input('Hello. What is your name? '))

print(name1.greetings())


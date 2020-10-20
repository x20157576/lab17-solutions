class AgeWeight:

    def __init__(self, age, height, rw):
        self.age = age
        self.height = height
        self.rw = rw

    def iw(self):
        return 'Based on your age of {} and your height of {}, your ideal weight is {}kgs.'\
            .format(self.age, self.height, self.rw)


age1 = int(input('Hello, What is your Age? '))
height1 = int(input('and could I get your Height (in cm)? '))
rw1 = (height1 - 100 + age1 % 10) * 0.90

p1 = AgeWeight(age1, height1, rw1)
print(p1.iw())

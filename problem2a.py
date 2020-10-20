# Problem 2 - One possible solution

# Input: the age and height of a person
# Process: calculate the recommended weight
# Output: display the recommended weight


class Weight:

    def __init__(self, my_age, my_height):
        self.age = my_age
        self.height = my_height


    def compute_recommended_weight(self):
        self.weight = (self.height - 100 + self.age % 10) * 0.90
        return self.weight



print('enter age')
a = int(input())

print('enter height')
h = float(input())

w = Weight(a, h)
print('recommended weight: ', w.compute_recommended_weight())



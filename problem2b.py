# Problem 2 - Another possible solution

# Input: the age and height of a person
# Process: calculate the recommended weight
# Output: display the recommended weight


class Weight:

    @classmethod
    def compute_recommended_weight(cls, age, height):
        weight = (height - 100 + age % 10) * 0.90
        return weight



print('enter age')
a = int(input())

print('enter height')
h = float(input())

w = Weight.compute_recommended_weight(a, h)
print('recommended weight: ', w)



# Problem 3 - one possible solution

# Input: the quantity of each of the following items caps, shirts, and hoodies
# Process: calculate the total cost of the items
# Output: display the total cost


class Shop:
    CAP_PRICE  = 5 #example of class variable
    SHIRT_PRICE = 10
    HOODIES_PRICE = 20

    def __init__(self, caps_number, hoodies_number, shirts_number):
        self.caps_no = caps_number
        self.hoodies_no = hoodies_number
        self.shirts_no = shirts_number

    def calculate_total_cost(self):
        self.cost = self.shirts_no * Shop.SHIRT_PRICE + self.caps_no * Shop.CAP_PRICE + self.hoodies_no * Shop.HOODIES_PRICE
        return self.cost



print('Welcome to the Student Union Shop\nHow many caps you\'d like to buy?')
caps = int(input())

print('How many shirts you\'d like to buy?')
shirts = int(input())

print('How many hoodies you\'d like to buy?')
hoodies = int(input())

s = Shop(caps, hoodies, shirts)
cost = s.calculate_total_cost()
print('total cost is: ', cost)
      


		
        

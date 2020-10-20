# Problem 4 - One possible solution

# Input: basic pay rate, number of regular hours, number of overtime hours
# Process: calculate the 3 type of payments
# Output: display the 3 type of payments


class Payment:

    def __init__(self, basic_pay_rate, regular_hours, overtime_hours):
        self.basic_pay_rate = basic_pay_rate
        self.regular_hours = regular_hours
        self.overtime_hours = overtime_hours


    def calculate_basic_pay(self):
        self.basic_pay = self.basic_pay_rate * self.regular_hours
        return self.basic_pay

    def calculate_overtime_pay(self):
        self.overtime_pay = 1.5 * self.basic_pay_rate * self.overtime_hours
        return self.overtime_pay

    def calculate_total_pay(self):
        return self.calculate_basic_pay() + self.calculate_overtime_pay() 

    




print("enter details 1st job offer\nbasic pay rate")
pay_rate = float(input())

print("enter the number of regular hours")
standard_hours = int(input())

print("enter the number of overtime hours")
overtime_hours = int(input())


p1 = Payment(pay_rate, standard_hours, overtime_hours)
print("basic payment: ", p1.calculate_basic_pay())
print("overtime payment: ", p1.calculate_overtime_pay())
print("total payment: ", p1.calculate_total_pay())




print("\nenter details 2nd job offer\nbasic pay rate")
pay_rate = float(input())

print("enter the number of regular hours")
standard_hours = int(input())

print("enter the number of overtime hours")
overtime_hours = int(input())


p2 = Payment(pay_rate, standard_hours, overtime_hours)
print("basic payment: ", p2.calculate_basic_pay())
print("overtime payment: ", p2.calculate_overtime_pay())
print("total payment: ", p2.calculate_total_pay())

                            




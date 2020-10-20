class Shopping:

    def __init__(self, total):
        self.total = total

    def showtotal(self):
        return '\nFantastic! The total in your shopping basket is only ${}.\nwhat a bargain!'.format(self.total)


tshirt = 12
hoodie = 17
caps = 5

tshirtno = int(input('T-shirts are ${} how many would you like? : '.format(tshirt)))
hoodieno = int(input('We are also selling hoodies for ${}, how many would you like? : '.format(hoodie)))
capsno = int(input('lastly, caps are only ${} so you will have to get some, how many would like? : '.format(caps)))
subtotal = (tshirt * tshirtno) + (hoodie * hoodieno) + (caps * capsno)

p1 = Shopping(subtotal)
print(p1.showtotal())

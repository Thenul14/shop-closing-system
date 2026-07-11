from till import Till
from calculator import Calculator
from cardmachine import CardMachine

till1 = Till(20,1,1,1,1,1,1,1,1,1,1,1)
till2 = Till(10,1,1,1,1,1,1,1,1,1,1,1)

print(till1.get_fifty())
print("after updates:",till1.get_fifty())



cardMachine1 = CardMachine(400,10)
cardMachine2 = CardMachine(400,10)
print("avg of single transaction: ", cardMachine1.avg_amount())

calculator2 = Calculator(till1=till1, cardmachine1=cardMachine1, till2=till2, cardmachine2=cardMachine2)
print(calculator2.total_funds())

A,B,C,D,E = calculator2.calcualte_ABCED()
print("A IS",A, "\nB IS",B, "\nC IS",C, "\nD IS",D, "\nE IS", E)
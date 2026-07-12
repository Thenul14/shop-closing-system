from till import Till
from cardmachine import CardMachine
from datetime import datetime

class Calculator:
    def __init__(self, till1 : Till,  cardmachine1 : CardMachine, till2 : Till=None, cardmachine2 : CardMachine=None):
        self.till1 = till1
        self.till2 = till2
        self.cardmachine1 = cardmachine1
        self.cardmachine2 = cardmachine2

    #calculates total cash in a single till
    def total_cash_single_till(self):
        fifties = self.till1.get_fifty()
        twenties = self.till1.get_twenty()
        tens = self.till1.get_ten()
        fives = self.till1.get_five()
        twos = self.till1.get_two()
        ones = self.till1.get_one()
        fiftypies = self.till1.get_fiftyp()
        twentypies = self.till1.get_twentyp()
        tenps = self.till1.get_tenp()
        fiveps = self.till1.get_fivep()
        twops = self.till1.get_twop()
        oneps = self.till1.get_onep()

        return ((fifties * 50) + (twenties * 20) + (tens * 10) + (fives * 5) + (twos * 2) + (ones * 1) + (fiftypies * 0.5) + (twentypies * 0.2) + (tenps * 0.1) + (fiveps * 0.05) + (twops * 0.02) + (oneps * 0.01))

    #calculates total cash on two tills
    def total_cash_two_tills(self):
        fifties = self.till1.get_fifty() + self.till2.get_fifty()
        twenties = self.till1.get_twenty() + self.till2.get_twenty()
        tens = self.till1.get_ten() + self.till2.get_ten()
        fives = self.till1.get_five() + self.till2.get_five()
        twos = self.till1.get_two() + self.till2.get_two()
        ones = self.till1.get_one() + self.till2.get_one()
        fiftypies = self.till1.get_fiftyp() + self.till2.get_fiftyp()
        twentypies = self.till1.get_twentyp() + self.till2.get_twentyp()
        tenps = self.till1.get_tenp() + self.till2.get_tenp()
        fiveps = self.till1.get_fivep() + self.till2.get_fivep()
        twops = self.till1.get_twop() + self.till2.get_twop()
        oneps = self.till1.get_onep() + self.till2.get_onep()

        

        return ((fifties * 50) + (twenties * 20) + (tens * 10) + (fives * 5) + (twos * 2) + (ones * 1) + (fiftypies * 0.5) + (twentypies * 0.2) + (tenps * 0.1) + (fiveps * 0.05) + (twops * 0.02) + (oneps * 0.01))
    
    def total_cash(self):
        if self.till2:
            return self.total_cash_two_tills()
        else:
            return self.total_cash_single_till()
        
    def total_cash_on_machines(self):
        if self.cardmachine2:
            return self.cardmachine1.get_total() + self.cardmachine2.get_total()
        else:
            return self.cardmachine1.get_total()
        
    
    def total_funds(self):
        cashTotal = self.total_cash()
        
        cardTotal = self.total_cash_on_machines()

        return cashTotal + cardTotal


    def calcualte_ABCED(self):
        A = self.total_cash()
        B = self.total_funds()
        C = B - A
        today = datetime.now().day
        if self.till2:
            D = (A - 200) + (today / 100)
            
        else:
            D = (A - 100) + (today / 100)
        E = B - C - D

        return A, B, C, D, E
class CardMachine:
    def __init__(self, total:float, noOfTransactions:int):
        self.total = total
        self.noOfTransactions = noOfTransactions

    def get_total(self):
        return self.total
    
    def get_noOfTransactions(self):
        return self.noOfTransactions
    
    def set_total(self,newTotal):
        self.total = newTotal

    def set_noOfTransactions(self, newTransactions):
        self.noOfTransactions = newTransactions

    def avg_amount(self):
        return self.total/self.noOfTransactions
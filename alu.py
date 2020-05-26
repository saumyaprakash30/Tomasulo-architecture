class ALU:
    def __init__(self):
        self.adder=[]
        self.multiplier=[]
        self.ADDTime = 4
        self.SUBTime = 4
        self.MULTime = 16
        self.DIVTime = 40
    
    def addADDSUB(self,ins,initialClock):
        self.adder.append([ins,initialClock])
    
    def addMULDIV(self,ins,initialClock):
        self.multiplier.append([ins,initialClock])

    # def checkStatus(self)
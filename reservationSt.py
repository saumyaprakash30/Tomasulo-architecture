class ReservationSt:
    def __init__(self):
        self.astation = []  #add sum station
        self.mstation = []  #mul div station
        self.aSize = 3
        self.mSize = 2

    def isFull(self,station):
        if(station=='add'):
            if(len(self.astation)==3):
                return True
            else:
                return False
        else:
            if(len(self.mstation)==2):
                return True
            else:
                return False

    def isEmpty(self,station):
        if(station=='add'):
            if(len(self.astation)==0):
                return True
            else:
                return False
        else:
            if(len(self.mstation)==0):
                return True
            else:
                return False
    
    def addInstruction(self,ins,clock):
        if(ins.split(" ")[0]=='ADD'  or ins[0]=='SUB'):
            print("add ADD")
            self.astation.append([ins,clock])  
        if(ins.split(" ")[0]=='MUL' or ins[0]=='DIV'):
            self.mstation.append([ins,clock])
        
    def removeInstruction(self,ins,clock):
        if(ins.split(" ")[0]=='ADD'  or ins[0]=='SUB'):
            for i in self.astation:
                if(i[0]==ins):
                    self.astation.remove(i)
        if(ins.split(" ")[0]=='MUL' or ins[0]=='DIV'):
            for i in self.mstation:
                if(i[0]==ins):
                    self.mstation.remove(i)

    def printResStation(self):
        print("add sub:")
        for i in self.astation:
            print(i)
        print("mul div:")
        for i in self.mstation:
            print(i)

# sample
# obj = ReservationSt()
# obj.addInstruction("ADD F1 R1 R2",2)
# obj.addInstruction("MUL F2 R2 R3",3)
# obj.printResStation()
# obj.removeInstruction("ADD F1 R1 R2",4)
# obj.printResStation()
# print(obj.isEmpty("add"))
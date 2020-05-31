class ALU:
    def __init__(self):
        self.adder=[]
        self.multiplier=[]
        self.divider=[]
        self.ADDTime = 4
        self.SUBTime = 4
        self.MULTime = 16
        self.DIVTime = 40
    
    def addADDSUB(self,_id,ins,initialClock):
        self.adder.append([_id,ins,initialClock,0])
    
    def addMULDIV(self,_id,ins,initialClock):
        if ins[0]=='DIV':
            self.divider.append([_id,ins,initialClock,0])
        else:
            self.multiplier.append([_id,ins,initialClock,0])

    def removeIns(self,_id):
        for i in self.adder:
            if i[0]==_id:
                self.adder.remove(i)
        for i in self.multiplier:
            if i[0]==_id:
                self.multiplier.remove(i)
        for i in self.divider:
            if i[0]==_id:
                self.divider.remove(i)
        
    def setAllBusyBit(self,fpr,ins,val):
        if ins[1].find("F")!=-1:
            fpr.setBusyBit(ins[1],val)
        if ins[2].find("F")!=-1:
            fpr.setBusyBit(ins[2],val)
        if ins[3].find("F")!=-1:
            fpr.setBusyBit(ins[3],val)
        # print("fprPrint inside alu",fpr.printFPRegisters())

    def incClock(self,fpr):
        for i,ival in enumerate(self.adder):
            if(ival[3]!=self.ADDTime):
                self.adder[i][3]+=1
            else:
                self.setAllBusyBit(fpr,ival[1],0)
                self.removeIns(ival[0])
        for i,ival in enumerate(self.multiplier):
            if(ival[3]!=self.MULTime):
                self.multiplier[i][3]+=1
            else:
                self.setAllBusyBit(fpr,ival[1],0)
                self.removeIns(ival[0])
        for i,ival in enumerate(self.divider):
            if(ival[3]!=self.DIVTime):
                self.divider[i][3]+=1
            else:
                self.setAllBusyBit(fpr,ival[1],0)
                self.removeIns(ival[0])
        return fpr
        
            
    def printALU(self):
        print("-----ALU-----\n")
        print("adderSubtractor:")
        for i in self.adder:
            print(i)
        print("Multiplier:")
        for i in self.multiplier:
            print(i)
        print("Divider:")
        for i in self.divider:
            print(i)
        print("-----ALU end-----\n")
    
    def isAllEmpty(self):
        if len(self.adder)==0 and len(self.multiplier)==0 and len(self.divider)==0:
            return True
        return False
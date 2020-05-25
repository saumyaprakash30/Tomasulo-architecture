class fpRegister:
    def __init__(self):
        file = open('./fpRegister.txt')
        self.registers = []
        val = file.readlines()
        for i in val:
            self.registers.append([int(i),0])

    def setBusyBit(self,fpReg,val):
        rAddress = fpReg.split("F")[1];
        if(rAddress<len(self.registers)):
            self.registers[rAddress][1] = val
        else:
            print("FPAddress out of index in setBusyBit")
            
    
    def printFPRegisters(self):
        print("FPRegister",self.registers)

    def setRegisterValue(self,fpReg,val):
        rAddress = fpReg.split("F")[1];
        if(rAddress<len(self.registers)):
            self.registers[rAddress][0] = val;
        else:
            print("FPAddress out of index in setRegVal")

    def getBusyBit(self,fpReg):
        rAddress = fpReg.split("F")[1];
        return self.registers[rAddress][1]

    def getRegisterData(self,fpReg):
        rAddress = fpReg.split("F")[1];
        return self.registers[rAddress][0]
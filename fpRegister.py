class fpRegister:
    def __init__(self):
        file = open('./fpRegister.txt')
        self.registers = []
        val = file.readlines()
        for i in val:
            self.registers.append([int(i),0])

    def setBusyBit(self,fpReg,val):
        rAddress = int(fpReg.split("F")[1]);
        if(rAddress<len(self.registers)):
            self.registers[rAddress][1] = val
        else:
            print("FPAddress out of index in setBusyBit")
            
    
    def printFPRegisters(self):
        print("--------FP Reg.--------")
        print(self.registers)
        print("--------FP Reg. end --------\n")

    def setRegisterValue(self,fpReg,val):
        rAddress = int(fpReg.split("F")[1]);
        if(rAddress<len(self.registers)):
            self.registers[rAddress][0] = val;
        else:
            print("FPAddress out of index in setRegVal")

    def getBusyBit(self,fpReg):
        rAddress = int(fpReg.split("F")[1]);
        # print(fpReg,rAddress,self.registers)
        return self.registers[rAddress][1]

    def getRegisterData(self,fpReg):
        rAddress = int(fpReg.split("F")[1]);
        return self.registers[rAddress][0]
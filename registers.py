'''
Author: Saumya Prakash(ced17i043) and Bazif Rasool(ced17i015)
'''

class Registers:
    def __init__(self):
        file = open('./register.txt')
        f = (file.readlines())
        self.registers=[]
        for i,ival in enumerate(f):
            self.registers.append([int(ival),0])
    
    def setBusyBit(self,reg,val):
        rAddress = int(reg.split("R")[1]);
        if(rAddress<len(self.registers)):
            self.registers[rAddress][1] = val
        else:
            print("RAddress out of index in setBusyBit")

    def getBusyBit(self,reg):
        rAddress = int(reg.split("R")[1]);
        # print(fpReg,rAddress,self.registers)
        return self.registers[rAddress][1]

    def setRegister(self,reg,val):
        
        regAddress = int(reg.split("R")[1])
        self.registers[regAddress][0] = val
    
    def printRegisters(self):
        print("----------Registers--------")
        print(self.registers)
        print("----------Registers end--------\n")

    def getRegisterVal(self,reg):
        
        regAddress = int(reg.split("R")[1])
        return self.registers[regAddress][0]

# test
# obj = Registers()
# obj.printRegisters()
# # print(obj.registers[1])
# obj.setBusyBit('R2',1);
# print(obj.getRegisterVal('R2'))
# obj.printRegisters()

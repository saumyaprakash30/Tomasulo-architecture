class Registers:
    def __init__(self):
        file = open('./register.txt')
        f = (file.readlines())
        self.registers={}
        for i,ival in enumerate(f):
            self.registers[i]=int(ival)

    def setRegister(self,reg,val):
        
        regAddress = int(reg.split("r")[1])
        self.registers[regAddress] = val
    
    def printRegisters(self):
        print("Registers",self.registers)

    def getRegisterVal(self,reg):
        
        regAddress = int(reg.split("r")[1])
        return self.registers[regAddress]
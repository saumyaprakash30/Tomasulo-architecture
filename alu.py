'''
Author: Saumya Prakash(ced17i043) and Bazif Rasool(ced17i015)
'''

class ALU:
    def __init__(self):
        self.adder=[]
        self.multiplier=[]
        self.divider=[]
        self.ADDTime = 8
        self.SUBTime = 8
        self.MULTime = 13
        self.FADDTime = 23
        self.FSUBTime = 23
        self.FMULTime = 26
        self.DIVTime = 40
        self.SHTime = 6
        self.NANDTime = 3
        self.HLTTime = 6
        self.CMPTime =3
    
    def addADDSUB(self,_id,ins,initialClock,countClock,resStClock):
        self.adder.append([_id,ins,initialClock,0,resStClock])
    
    def addMULDIV(self,_id,ins,initialClock,countClock,resStClock):
        if ins[0]=='DIV':
            self.divider.append([_id,ins,initialClock,0,resStClock])
        else:
            self.multiplier.append([_id,ins,initialClock,0,resStClock])

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
        
    def setAllBusyBit(self,r,ins,val):
        if ins[0]=="CMP":
            if ins[1].find("R")!=-1:
                r.setBusyBit(ins[1],val)
            if ins[2].find("R")!=-1:
                r.setBusyBit(ins[2],val)
        else:
            if ins[1].find("F")!=-1:
                r.setBusyBit(ins[1],val)
            if ins[2].find("F")!=-1:
                r.setBusyBit(ins[2],val)
            if ins[3].find("F")!=-1:
                r.setBusyBit(ins[3],val)
            if ins[1].find("R")!=-1:
                r.setBusyBit(ins[1],val)
            if ins[2].find("R")!=-1:
                r.setBusyBit(ins[2],val)
            if ins[3].find("R")!=-1:
                r.setBusyBit(ins[3],val)
        # print("fprPrint inside alu",fpr.printFPRegisters())

    def incClock(self,fpr,reg,processedIns):
        for i,ival in enumerate(self.adder):
            if ival[1][0]=='FADD' or ival[1][0]=='FSUB':
                if(ival[3]!=self.FADDTime):
                    self.adder[i][3]+=1
                else:
                    if ival[1][0]=='FADD':
                        fpr.setRegisterValue(ival[1][1],float(fpr.getRegisterData(ival[1][2]))+float(fpr.getRegisterData(ival[1][3])))
                    else:
                        fpr.setRegisterValue(ival[1][1],float(fpr.getRegisterData(ival[1][2]))-float(fpr.getRegisterData(ival[1][3])))
                    self.setAllBusyBit(fpr,ival[1],0)
                    processedIns.append(ival)
                    self.removeIns(ival[0])
            elif ival[1][0]=='ADD' or ival[1][0]=='SUB' or ival[1][0]=='ADC' or ival[1][0]=='SBB':
                if(ival[3]!=self.ADDTime):
                    self.adder[i][3]+=1
                else:
                    if ival[1][0]=='ADD':
                        reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2]))+int(reg.getRegisterVal(ival[1][3])))
                    if ival[1][0]=='ADC':
                        reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2]))+int(reg.getRegisterVal(ival[1][3]))+1)
                    if ival[1][0]=='SUB':
                        reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2]))-int(reg.getRegisterVal(ival[1][3])))
                    if ival[1][0]=='SBB':
                        reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2]))-int(reg.getRegisterVal(ival[1][3]))-1)
                    self.setAllBusyBit(reg,ival[1],0)
                    processedIns.append(ival)
                    self.removeIns(ival[0])
            elif ival[1][0]=='SHR' or ival[1][0]=='LHR':
                if(ival[3]!=self.SHTime):
                    self.adder[i][3]+=1
                else:
                    if ival[1][0]=='SHR':
                        reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2])) >> int(reg.getRegisterVal(ival[1][3])))
                    if ival[1][0]=='LHR':
                        reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2])) << int(reg.getRegisterVal(ival[1][3])))
                    self.setAllBusyBit(reg,ival[1],0)
                    processedIns.append(ival)
                    self.removeIns(ival[0])
            elif ival[1][0]=='NAND' or ival[1][0]=='XOR':
                if(ival[3]!=self.NANDTime):
                    self.adder[i][3]+=1
                else:
                    if ival[1][0]=='NAND':
                        reg.setRegister(ival[1][1],~(int(reg.getRegisterVal(ival[1][2])) & int(reg.getRegisterVal(ival[1][3]))))
                    if ival[1][0]=='XOR':
                        reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2])) ^ int(reg.getRegisterVal(ival[1][3])))
                    self.setAllBusyBit(reg,ival[1],0)
                    processedIns.append(ival)
                    self.removeIns(ival[0])
            elif ival[1][0]=='CMP':
                if(ival[3]!=self.CMPTime):
                    self.adder[i][3]+=1
                else:
                    reg.setRegister(ival[1][1],~(int(reg.getRegisterVal(ival[1][2]))))
                    self.setAllBusyBit(reg,ival[1],0)
                    processedIns.append(ival)
                    self.removeIns(ival[0])


        for i,ival in enumerate(self.multiplier):
            if ival[1][0]=='FMUL':
                if(ival[3]!=self.FMULTime):
                    self.multiplier[i][3]+=1
                else:
                    fpr.setRegisterValue(ival[1][1],float(fpr.getRegisterData(ival[1][2]))*float(fpr.getRegisterData(ival[1][3])))
                    self.setAllBusyBit(fpr,ival[1],0)
                    processedIns.append(ival)
                    self.removeIns(ival[0])

            if ival[1][0]=='MUL':
                if(ival[3]!=self.MULTime):
                    self.multiplier[i][3]+=1
                else:
                    reg.setRegister(ival[1][1],int(reg.getRegisterVal(ival[1][2]))*int(reg.getRegisterVal(ival[1][3])))
                    self.setAllBusyBit(reg,ival[1],0)
                    processedIns.append(ival)
                    self.removeIns(ival[0])

        for i,ival in enumerate(self.divider):
            if(ival[3]!=self.DIVTime):
                self.divider[i][3]+=1
            else:
                fpr.setRegisterValue(ival[1][1],float(fpr.getRegisterData(ival[1][2]))*float(fpr.getRegisterData(ival[1][3])))
                self.setAllBusyBit(reg,ival[1],0)
                processedIns.append(ival)
                self.removeIns(ival[0])
        return fpr,reg,processedIns
        
            
    def printALU(self):
        print("-----ALU-----")
        print("adderSubtractorLogic:")
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
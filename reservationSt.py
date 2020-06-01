'''
Author: Saumya Prakash(ced17i043) and Bazif Rasool(ced17i015)
'''
class ReservationSt:
    def __init__(self):
        self.astation = []  #add sum station
        self.mstation = []  #mul div station
        self.aSize = 3
        self.mSize = 2
        self.count =1   # assign _id

    def isFull(self,station):
        if(station=='ADD' or station=='SUB'):
            if(len(self.astation)==3):
                return True
            else:
                return False
        else:
            if(len(self.mstation)==2):
                return True
            else:
                return False

    def isBothEmpty(self):
        if len(self.astation) + len(self.mstation) >0:
            return False
        return True

    def isEmpty(self,station):
        if(station=='ADD' or station=='SUB'):
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
        # print("addins",ins)
        if(ins[0]=='ADD'  or ins[0]=='SUB' or ins[0]=='FADD' or ins[0]=='FSUB' or ins[0]=='SBB' or ins[0]=='ADC' or ins[0]=='SHR' or ins[0]=='LHR'or ins[0]=='NAND' or ins[0]=='XOR' or ins[0]=='CMP' ):
            # print("added ADDSUB")
            self.astation.append([self.count,ins,clock])
            self.count+=1
        if(ins[0]=='MUL' or ins[0]=='DIV' or ins[0]=='FMUL'):
            # print("added MULDIV")
            self.mstation.append([self.count,ins,clock])
            self.count+=1
        
    def removeInstruction(self,_id,clock):
        # if(ins[0]=='ADD'  or ins[0]=='SUB'):
        #     for i in self.astation:
        #         if(i[0]==ins):
        #             self.astation.remove(i)
        # if(ins[0]=='MUL' or ins[0]=='DIV'):
        #     for i in self.mstation:
        #         if(i[0]==ins):
        #             self.mstation.remove(i)
        for i in self.astation:
            if _id == i[0]:
                self.astation.remove(i)
        for i in self.mstation:
            if _id == i[0]:
                self.mstation.remove(i)


    def printResStation(self):
        print("-----reservation St.------")
        print("add sub Logic:")
        for i in self.astation:
            print(i)
        print("mul div:")
        for i in self.mstation:
            print(i)
        print("-----reservation St. end------\n")



# # sample
# obj = ReservationSt()
# obj.addInstruction(["ADD" ,"F1", "R1", "R2"],2)
# # obj.addInstruction("MUL F2 R2 R3",3)
# # obj.printResStation()
# obj.removeInstruction(1,4)
# # obj.addInstruction("DIV F2 R2 R3",3)
# obj.printResStation()
# print(obj.isEmpty("add"))
#opens Inst.txt reads instructions and remove whitespaces
'''
Author: Saumya Prakash(ced17i043) and Bazif Rasool(ced17i015)
'''
class i_f:
    def __init__(self):
        inst = open("Inst.txt","r").readlines()
        self.ic_count=0
        self.instructions = []
        #clock cycles for each instructions
        self.add_inst = 4
        self.sub_inst = 4
        self.mul_inst = 16
        self.div_inst = 40
        #ldr and str timings are low as assumes data in cache
        self.ldr_inst = 3
        self.str_inst = 3
        for each in inst:
            temp = each.split("\n")
            for every in temp:
                if len(every)!=0:
                    self.instructions.insert(len(self.instructions),every)
    #this function returns as a list next instruction with op at [0],regs at [1].. so on

    def isEmpty(self):
        if self.ic_count == len(self.instructions):
            return True
        return False

    def get_next_instruction(self):
        self.ic_count = self.ic_count +1
        return self.instructions[self.ic_count-1].split(" ")

    def getNextInstructionString(self):
        self.ic_count = self.ic_count +1
        return self.instructions[self.ic_count-1]
    
    def decIc_count(self):
        self.ic_count = self.ic_count-1

    def getAllIns(self):
        return self.instructions
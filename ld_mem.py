from fpRegister import *
from registers import *

def mem_raccess(src):
    regs = Registers()
    mem_addr=int(regs.getRegisterVal(src))
    mem_arr=open("mem_vals.txt","r").readlines()
    return mem_arr[mem_addr]

def mem_waccess(dest,value):
    regs = Registers()
    mem_addr=int(regs.getRegisterVal(dest))
    f=open("mem_vals.txt","r+")
    mem_arr=f.readlines()
    mem_arr[mem_addr]=str(value)+"\n"
    print(mem_arr[mem_addr])
    f.seek(0)
    f.truncate(0)
    f.writelines(mem_arr)

class ldr_str:
    def __init__(self,F,R):
        self.wait_time=4
        self.Fr = F
        self.Rr = R
        self.buffer = []
    def wait(self,t):
        for i in range(0,t):
            print(i)

    def pass_to_load(self,dest,src,clock):
        #checks if register is already busy then does noting on that clock
        if len(self.buffer) >0 :
            for each in self.buffer:
                if each[0] == dest:
                    return
        #register requested is free then do the following
        print(src,dest)
        #float ops:
        if "F" in dest:
            self.Fr.setBusyBit(dest,1)
            self.buffer.append([dest,src,clock])
            value=mem_raccess(src)
            self.Fr.setRegisterValue(dest,float(value))
        if "R" in dest:
            self.Rr.setBusyBit(dest,1)
            self.buffer.append([dest,src,clock])
            value=mem_raccess(src)
            self.Rr.setRegisterValue(dest,float(value))
       # checks for finished ldr and sets busy bits to only those 0
       #removes them from ldr lists
        

    def pass_to_str(self,dest,src,clock):
        value=self.Fr.getRegisterData(src)
        mem_waccess(dest,value)

    def ldr_str_main(self,instruction_ip,clock):
        ins = instruction_ip
        for i,each in enumerate(self.buffer):
            if clock-each[2] >= self.wait_time :
                if "F"in each[0]:
                    self.Fr.setBusyBit(each[0],0)
                    self.buffer.pop(i)
                if "R" in each[0]:
                    self.Rr.setBusyBit(each[0],0)
                    self.buffer.pop(i)
        if "LDR" in ins[0]:
            self.pass_to_load(ins[1],ins[2],clock)
        if "STR" in ins[0]:
            self.pass_to_str(ins[1],ins[2],clock)

#test
l = ldr_str(fpRegister(),Registers())
l.ldr_str_main(["LDR","F0","R0"],0)

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
    def __init__(self,F):
        self.wait_time=4
        self.Fr = F
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
        self.Fr.setBusyBit(dest,1)
        self.buffer.append([dest,src,clock])
        value=mem_raccess(src)
        self.Fr.setRegisterValue(dest,value)
       # checks for finished ldr and sets busy bits to only those 0
       #removes them from ldr lists
        for i,each in enumerate(self.buffer):
            if each[2] - clock <= self.wait_time :
                self.Fr.setBusyBit(each[0],0)
                self.buffer.pop(i)

    def pass_to_str(self,dest,src,clock):
        value=self.Fr.getRegisterData(src)
        mem_waccess(dest,value)

    def ldr_str_main(self,instruction_ip,clock):
        ins=instruction_ip.split(" ")
        if "LDR" in ins[0]:
            self.pass_to_load(ins[1],ins[2].split("\n")[0],clock)
        if "STR" in ins[0]:
            self.pass_to_str(ins[1],ins[2].split("\n")[0],clock)
        self.clk +=1
#test


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
    def __init__(self):
        self.wait_time=4
        self.Fr = fpRegister()
    def wait(self,t):
        for i in range(0,t):
            print(i)

    def pass_to_load(self,dest,src):
        self.Fr.setBusyBit(dest,1)
        self.wait(self.wait_time)
        value=mem_raccess(src)
        self.Fr.setRegisterValue(dest,value)
        self.Fr.setBusyBit(dest,0)
        print(Fr.getRegisterData("F0"))
        return dest,src
    def pass_to_str(self,dest,src):
        #this wait block is there to ensure no reads happens to that addr while writing altough fp register need not be marked busy
        value=self.Fr.getRegisterData(src)
        mem_waccess(dest,value)
        self.wait(self.wait_time)
    def ldr_module(self,instruction_ip):
        ins=instruction_ip.split(" ")
        if "LDR" in ins[0]:
            self.pass_to_load(ins[1],ins[2].split("\n")[0])
        if "STR" in ins[0]:
            self.pass_to_str(ins[1],ins[2].split("\n")[0])
obj = ldr_str()
obj.ldr_module("LDR F0 R0")

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
        self.store_buff = []
    def wait(self,t):
        for i in range(0,t):
            print(i)

    def pass_to_load(self,dest,src,clock):
        #checks if register is already busy then does noting on that clock
        if len(self.buffer) >0 or len(self.store_buff)>0 :
            for each in self.buffer:
                if each[0] == dest:
                    return -1
            for each in self.store_buff:
                if each[0] == dest or each[0] == src:
                    return -1
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
            self.Rr.setRegister(dest,float(value))
       # checks for finished ldr and sets busy bits to only those 0
       #removes them from ldr lists
        

    def pass_to_str(self,dest,src,clock):
        for each in self.store_buff:
            if each[0] == dest:
                return -1
        if "F" in src :
            if self.Fr.getBusyBit(src) == 0 and self.Rr.getBusyBit(dest)==0:
                self.Rr.setBusyBit(src,1)
                value=self.Fr.getRegisterData(src)
                mem_waccess(dest,value)
                self.store_buff.append([dest,src,clock])
            else :
                return -1
        if "R" in src :
            if self.Rr.getBusyBit(src) == 0 and self.Rr.getBusyBit(dest)==0:
                self.Rr.setBusyBit(src,1)
                value=self.Rr.getRegisterVal(src)
                mem_waccess(dest,value)
                self.store_buff.append([dest,src,clock])
            else :
                return -1


        

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
        for i,each in enumerate(self.store_buff):
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

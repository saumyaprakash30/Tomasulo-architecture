'''
Author: Saumya Prakash(ced17i043) and Bazif Rasool(ced17i015)
'''

from fpRegister import *
from registers import *
from alu import *
from reservationSt import *
from insFetch import *
from ld_mem import *


fpr = fpRegister()
reg = Registers()
alu = ALU()
rstation = ReservationSt()
ifetch =i_f()
mem = ldr_str(fpr,reg)

clock=0

def setAllBusyBit(ins,val):
    if ins[0]=="CMP":
        if ins[1].find("R")!=-1:
            reg.setBusyBit(ins[1],val)
        if ins[2].find("R")!=-1:
            reg.setBusyBit(ins[2],val)
    else:
        if ins[1].find("F")!=-1:
            fpr.setBusyBit(ins[1],val)
        if ins[2].find("F")!=-1:
            fpr.setBusyBit(ins[2],val)
        if ins[3].find("F")!=-1:
            fpr.setBusyBit(ins[3],val)
        if ins[1].find("R")!=-1:
            reg.setBusyBit(ins[1],val)
        if ins[2].find("R")!=-1:
            reg.setBusyBit(ins[2],val)
        if ins[3].find("R")!=-1:
            reg.setBusyBit(ins[3],val)

def controlResStation():
    # for each ins
        #check all operand free
        # call appropriate func that return complition status
        # status -> remove ins from resStation or continue
    
    station = rstation.astation + rstation.mstation
    station.sort()
    for i in station:
        
        res = operandBusyCheck(i[1])
        print("res",res)
        if(res==False):
            if i[1][0]=='ADD' or i[1][0]=='SUB' or i[1][0]=='SBB' or i[1][0]=='ADC' or i[1][0]=='FADD' or i[1][0]=='FSUB' or i[1][0]=='SHR' or i[1][0]=='LHR' or i[1][0]=='NAND' or i[1][0]=='XOR' or i[1][0]=='CMP'  :
                alu.addADDSUB(i[0],i[1],clock)
            elif i[1][0]=='MUL' or i[1][0]=='DIV' or i[1][0]=='FMUL':
                alu.addMULDIV(i[0],i[1],clock)
            setAllBusyBit(i[1],1)
            rstation.removeInstruction(i[0],clock)

    rstation.printResStation()
    global fpr,reg
    fpr,reg = alu.incClock(fpr,reg)
    alu.printALU()
    fpr.printFPRegisters()
    reg.printRegisters()

    

    

def operandBusyCheck(ins):
    busy = False    #not busy
    if ins[0]=='CMP':
        if ins[1].find("R")!=-1:
            if reg.getBusyBit(ins[1])==1:
                return True
        if ins[2].find("R")!=-1:
            if reg.getBusyBit(ins[2])==1:
                return True
    else:
        if ins[1].find("F")!=-1:
            if fpr.getBusyBit(ins[1])==1:
                return True
        if ins[2].find("F")!=-1:
            if fpr.getBusyBit(ins[2])==1:
                return True
        if ins[3].find("F")!=-1:
            if fpr.getBusyBit(ins[3])==1:
                return True
        if ins[1].find("R")!=-1:
            if reg.getBusyBit(ins[1])==1:
                return True
        if ins[2].find("R")!=-1:
            if reg.getBusyBit(ins[2])==1:
                return True
        if ins[3].find("R")!=-1:
            if reg.getBusyBit(ins[3])==1:
                return True
    return busy
    


while(True):

    # inc clock
    # ins fetch
    # check resStation 
    # call controlResStation
    # add to resStation
    
    clock+=1
    print("--------------------clock : ",clock,"-------------------\n")
    mem.ldr_str_main(["na","na","na"],clock)
    if ifetch.isEmpty()==False:

        ins = ifetch.get_next_instruction()
        mem_stat = mem.ldr_str_main(ins,clock)
        print("ins",ins)
        
        if ins[0]=='HLT':
            clock+=5;
            break;
        if mem_stat == -1:
            ifetch.decIc_count()

        if rstation.isFull(ins[0])==True:
            ifetch.decIc_count()
        else:
            rstation.addInstruction(ins,clock)
    
    controlResStation()
    
    #end process
    if rstation.isBothEmpty() and ifetch.isEmpty() and alu.isAllEmpty():
        break

    # break
    # print("inwhile")

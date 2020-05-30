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
load_store =ldr_str(fpr)

clock=0

def controlResStation():
    # for each ins
        #check all operand free
        # call appropriate func that return complition status
        # status -> remove ins from resStation or continue
    
    for i in rstation.astation:
        #operand check
        res = operandBusyCheck(i[1])
        if(res==False):
            alu.addADDSUB(i[0],i[1],clock)
    for i in rstation.mstation:
        res = operandBusyCheck(i[1])
        if(res==False):
            alu.addMULDIV(i[0],i[1],clock)


    print(".")

def operandBusyCheck(ins):
    busy = False    #not busy
    if ins[1].find("F")!=-1:
        if fpr.getBusyBit(ins[1])==1:
            return True
    if ins[2].find("F")!=-1:
        if fpr.getBusyBit(ins[2])==1:
            return True
    if ins[3].find("F")!=-1:
        if fpr.getBusyBit(ins[3])==1:
            return True
    return busy
    


while(True):

    # inc clock
    # ins fetch
    # check resStation 
    # call controlResStation
    # add to resStation
    clock+=1
    ins = ifetch.get_next_instruction()
    x=load_store.ldr_str_main(ins,clock)
    if rstation.isFull(ins[0])==True:
        ifetch.decIc_count()
    else:
        rstation.addInstruction(ins,clock)
    controlResStation()
    


    # break
    print("inwhile")

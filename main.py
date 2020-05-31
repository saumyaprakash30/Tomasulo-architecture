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

def setAllBusyBit(ins,val):
    # print("setallbit",ins)
    if ins[1].find("F")!=-1:
        fpr.setBusyBit(ins[1],val)
    if ins[2].find("F")!=-1:
        fpr.setBusyBit(ins[2],val)
    if ins[3].find("F")!=-1:
        fpr.setBusyBit(ins[3],val)

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
            setAllBusyBit(i[1],1)
            rstation.removeInstruction(i[0],clock)
    for i in rstation.mstation:
        res = operandBusyCheck(i[1])
        if(res==False):
            alu.addMULDIV(i[0],i[1],clock)
            setAllBusyBit(i[1],1)
            rstation.removeInstruction(i[0],clock)
    rstation.printResStation()
    global fpr
    fpr = alu.incClock(fpr)
    alu.printALU()
    fpr.printFPRegisters()

    

    

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
    print("--------------------clock : ",clock,"-------------------\n")
    if ifetch.isEmpty()==False:

        ins = ifetch.get_next_instruction()
        load_store.ldr_str_main(ins,clock)
        print("ins",ins)
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

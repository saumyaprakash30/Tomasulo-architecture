from fpRegister import *
from registers import *

# testing
fpr = fpRegister()
fpr.setBusyBit(2,1)
fpr.printFPRegisters()
fpr.setRegisterValue(2,10)
fpr.setBusyBit(2,0)
fpr.printFPRegisters()

reg = Registers()
reg.printRegisters()
print(reg.getRegisterVal('r2'))
reg.setRegister('r1',12)
reg.printRegisters()

# testing end
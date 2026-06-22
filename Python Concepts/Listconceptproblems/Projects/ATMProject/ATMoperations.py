from ATMExceptions import DepositError,WithdrawError,InsuffFundsError
bal=500.00 #bal is global var
def deposit():
    damt=float(input("Enter Deposit Amount")) #may raise valueerror
    if (damt<0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tyour account xxxxxxx123 credited with INR:{}".format(damt))
        print("\tNow available balance in your account xxxxxxx123 INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter Withdraw Amount")) #May Raise ValueError
    if (wamt<0):
        raise WithdrawError
    elif(wamt+500)>bal:
        raise InsuffFundsError
    else:
        bal=bal-wamt
        print("\tyour account xxxxxxx123 debited with INR:{}".format(wamt))
        print("\tNow Avaialable bal in your account xxxxxxx123 INR:{}".format(bal))
    def baleng():
        print("\tNow Avaialable balance in your account xxxxxxx123 INR:{}".format(bal))

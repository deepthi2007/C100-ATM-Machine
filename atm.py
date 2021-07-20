class ATM :
    def __init__ (self,pin,code) :
        self.pin = pin
        self.passcode = code
    
    def deposit (self) :
        deposit = input("Enter the cash you want to deposite :- ")
        print("deposite successfully done")

    def withDrawle (self) :
        withDrawle = input("Enter the cash you want to With Drawel :- ")
        print("With Drawel successfully done.")

    def transfer (self) :
        transfer = input("Enter the cash you want to transnfer and account name :- ")
        print("Transfer successfully done")

    def payment (self) :
        payment = input("Enter the cash you want to pay :- ")
        print("Payemnt successfully done")


print("Welcome to Deepthi's ATM")

pin = input("Please enter your Atm Card Pin :- ")
passcode = input("Please enter your passcode :- ")

atm1 = ATM(pin,passcode)

print("Press these buttons for using the ATM :")
print("          1 - Make a Deposite")
print("          2 - Make a With Drawel")
print("          3 - Make a Transfer to another account")
print("          4 - Make a Bill Payment")

operation = input("Press the key for performing a fuction :")

if operation == "1" :
    atm1.deposit()
elif operation == "2" :
    atm1.withDrawle()
elif operation == "3" :
    atm1.transfer()
elif operation == "4" :
    atm1.payment()
else :
    print("Please select the numbers between 1-4 only")

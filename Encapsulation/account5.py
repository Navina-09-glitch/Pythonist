#Program for Demonstrating Data Encapsulation
class Account: #mean we made class private so it is not possible to import account
    #class name is made as encapsulated.
    def __init__(self):
        self.acno=1234
        self.cname="Rossum"
        self.bal=4.5
        self.pin=4567
        self.bname="SBI"


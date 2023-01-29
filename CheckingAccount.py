class CheckingAccount:
    def __init__(self, name, address, acctNum, balance):
        self.name = name
            #accountholder's name
        self.address = address
            #accountholder's address
        self.acctNum = acctNum
            #account number
        self.__balance = balance
            #account balance - private to class
    def debit(self, total):
        #to avoid overdraft, we want to first check that balance is not less than debit total 
        if self.__balance < total:
            print ("Transaction declined. Insufficient funds.")
        else:
            self.__balance = self.__balance - total
            print("You have successfully paid ${:.2f} from account #{}.".format(total, self.acctNum))
    def credit(self, total):
        self.__balance = self.__balance + total
        print("You have successfully credited ${:.2f} to your account #{}.".format(total, self.acctNum))
    def getBalance(self):
        print("Hello, {}. Your account #{} has a balance of ${:.2f}.".format(self.name, self.acctNum, self.__balance))


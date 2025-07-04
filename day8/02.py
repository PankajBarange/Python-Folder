class bank:
    BankName = "HDFC Bank"

    def getStatus(self):
        print(f"The Bank Name = {self.BankName}")
        print(f"The Acc Balance = {self.acc_balance}")
        print("==================================\n")

    def deposit(self,amount):
        self.acc_balance = self.acc_balance + amount    
        print("Your amount has been credited!")
        print("================================\n")


    def withdraw(self, amount):
        if self.acc_balance > amount:
            self.acc_balance = self.acc_balance - amount
            print("Your amound has been debited")
            print("=================================\n")
        else:
            print("Insufficient Amount")



b1 = bank()
b1.acc_balance = 500
b1.getStatus()

b1.deposit(int(input("Enter your amount")))
b1.getStatus()


b1.withdraw(int(input("Enter your amount")))
b1.getStatus()

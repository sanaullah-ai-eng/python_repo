class Bank:
    def __init__(self , Name:str , balance:int)->None:
        self.Name=Name
        self.__balance=balance
    def deposite(self , amount:int):
        if amount<0 : 
            print("invalid amount")
        else:
            self.__balance+=amount
    def get_balance(self):
        return self.__balance

b1= Bank("sana" , 1000)
print(b1.get_balance())
b1.deposite(100)
print(b1.get_balance())


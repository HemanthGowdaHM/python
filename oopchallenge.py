# class BankAccount:
    
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def check_balance(self):
#         print(self.balance)
        
#     def deposit(self,dept_Amount):
#         self.balance += dept_Amount
#         print(f"{dept_Amount} is successfully deposited ")
        
#     def with_draw(self,WD_Amount):
#         if self.balance >= WD_Amount:
#             self.balance -= WD_Amount
#             print(f" {WD_Amount} withdraw successfull ..")
#         else:
#             print("insufficent funds")
    
#     def __str__(self):
#         return f"owner : {self.owner} \n Blance: {self.balance}"
    
# Acc1 = BankAccount("Ram",500)

# Acc1.check_balance()
# Acc1.deposit(200)
# # Acc1.with_draw(200)
# # Acc1.with_draw(1000)
# print(str(Acc1))
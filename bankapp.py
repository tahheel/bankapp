# BASIC UP TO GENERATION OF ACCOUNT NUMBERS

# import random

# class User():
    
#     def __init__(self, name, age, email, phone):
        
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):


#     def __init__(self, name, age, email, phone): # INITIALIZE CHILD CLASS

#         super().__init__(name, age, email, phone) # INITIALIZE ATTRIBUTES FROM PARENT CLASS
#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)

#         return str(account_num)



# x = Account("atha", 23, "inyangete@gmail.com", "08032134387")
# print(x.account_no)


# import random

# class User():
    
#     def __init__(self, name, age, email, phone):
        
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):


#     def __init__(self, name, age, email, phone): # INITIALIZE CHILD CLASS

#         super().__init__(name, age, email, phone) # INITIALIZE ATTRIBUTES FROM PARENT CLASS
#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)

#         return str(account_num)

#     def deposit(self, amount, comment = ""):

#         self.balance += amount # ADD DEPOSIT VALUE TO BALANCE
#         self.store_history("credit", amount, comment)

#         print(f"Welldone {self.name} your deposit of ₦{amount} was successful your new balance is ₦{self.balance}.")

#     def withdraw(self, amount, comment = ""):

#         self.balance -= amount # ADD DEPOSIT VALUE TO BALANCE
#         self.store_history("debit", amount, comment)

#         print(f"Welldone {self.name} your withdrawal of ₦{amount} was successful your new balance is ₦{self.balance}.")

#     def transfer(self, amount, recipient, comment = ""):

#         self.balance -= amount # REMOVE TRANSFER AMOUNT FROM SENDER'S BALANCE
#         recipient.balance += amount # ADD TRANSFER AMOUNT FROM RECIPIENT'S BALANCE

#         self.store_history("transfer", amount, comment, recipient.name)

#         print(f"Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was successful your new balance is ₦{self.balance}.")

#     def store_history(self, type, amount, comment, reciever = "same as sender"):
#         file = open("financial_statement.csv", "a")
#         file.write(f"{type},{self.name},{amount},{comment},{reciever}\n")

#         print(type, amount, comment, reciever)
        



        
# atha = Account("blake", 23, "inyangete@gmail.com", "08032134387")
# print(atha.account_no)
# atha.deposit(120000)
# atha.withdraw(3000)

# bolu = Account("seun", 33, "bolu@gmail.com", "08089129387")
# atha.transfer(10000, bolu, "Flexing.")


## REFACTORED TO HAVE TRANSACTION USING DEPOSIT AND WITHDRAW METHODS INSTEAD OF WRITING NEW CODE AND ADDED 



# import random

# class User():
    
#     def __init__(self, name, age, email, phone):
        
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):


#     def __init__(self, name, age, email, phone): # INITIALIZE CHILD CLASS

#         super().__init__(name, age, email, phone) # INITIALIZE ATTRIBUTES FROM PARENT CLASS
#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)

#         return str(account_num)

#     def deposit(self, amount, comment = "no comment", source = False):

#         transaction_label = "credit"

#         if source:
#             transaction_type = "transfer"
#             source = source.name
#         else:
#             transaction_type = "deposit"
#             source = self.name

#         self.balance += amount # ADD DEPOSIT VALUE TO BALANCE
#         self.store_history(transaction_type, transaction_label, amount, self.name, comment, source)

#         print(f"Welldone {self.name} your deposit of ₦{amount} was successful your new balance is ₦{self.balance}.")

#     def withdraw(self, amount, comment = "no comment", collector = False):

#         transaction_label = "debit"

#         if collector:
#             transaction_type = "transfer"
#             collector = collector.name
#         else:
#             transaction_type = "withdrawal"
#             collector = self.name

#         self.balance -= amount # DEDUCT VALUE FROM BALANCE
#         self.store_history(transaction_type, transaction_label, amount, self.name, comment, collector)

#         print(f"Welldone {self.name} your withdrawal of ₦{amount} was successful your new balance is ₦{self.balance}.")

#     def transfer(self, amount, recipient, comment = ""):

#         self.withdraw(amount, comment, recipient)
#         recipient.deposit(amount, comment, self)

#         print(f"Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was successful your new balance is ₦{self.balance}.")

#     def store_history(self, transaction_type, transaction_label, amount, source, comment, reciever = "same"):
#         file = open("financial_statement.csv", "a")
#         file.write(f"{transaction_type}, {transaction_label},{amount},{source},{reciever},{comment}\n")

#         print(transaction_type, amount, comment, reciever)


        
# atha = Account("atha", 23, "inyangete@gmail.com", "08032134387")
# print(atha.account_no)
# atha.deposit(120000)
# atha.withdraw(3000)

# bolu = Account("bolu", 33, "bolu@gmail.com", "08089129387")
# atha.transfer(10000, bolu, "Flexing.")





import random

class User():
    
    def __init__(self, name, age, email, phone):
        
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

class Account(User):


    def __init__(self, name, age, email, phone): # INITIALIZE CHILD CLASS

        super().__init__(name, age, email, phone) # INITIALIZE ATTRIBUTES FROM PARENT CLASS
        self.balance = 0
        self.account_no = self.generate_acct_no()

    def generate_acct_no(self):

        account_num = random.randint(3000000000, 3000009999)

        return str(account_num)

    def deposit(self, amount, comment = "no comment", source = False):

        transaction_label = "credit"

        if source:
            transaction_type = "transfer"
            source = source.name
        else:
            transaction_type = "deposit"
            source = self.name

        self.balance += amount # ADD DEPOSIT VALUE TO BALANCE
        self.store_history(transaction_type, transaction_label, amount, self.name, comment, source)

        print(f"Welldone {self.name} your deposit of ₦{amount} was successful your new balance is ₦{self.balance}.")

    def withdraw(self, amount, comment = "no comment", collector = False):

        transaction_label = "debit"

        if collector:
            transaction_type = "transfer"
            collector = collector.name
        else:
            transaction_type = "withdrawal"
            collector = self.name

        self.balance -= amount # DEDUCT VALUE FROM BALANCE
        self.store_history(transaction_type, transaction_label, amount, self.name, comment, collector)

        print(f"Welldone {self.name} your withdrawal of ₦{amount} was successful your new balance is ₦{self.balance}.")

    def transfer(self, amount, recipient, comment = ""):

        self.withdraw(amount, comment, recipient)
        recipient.deposit(amount, comment, self)

        print(f"Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was successful your new balance is ₦{self.balance}.")

    def store_history(self, transaction_type, transaction_label, amount, source, comment, reciever = "same"):
        file = open("financial_statement.csv", "a")
        file.write(f"{transaction_type}, {transaction_label},{amount},{source},{reciever},{comment}\n")

        print(transaction_type, amount, comment, reciever)


        
taheel = Account("taheel", 29, "taheel@gmail.com", "0803444444")
print(taheel.account_no)
taheel.deposit(120000)
taheel.withdraw(3000)

ogechi = Account("ogechi", 33, "ogechi@gmail.com", "08089129387")
taheel.transfer(10000, ogechi, "Flexing.")

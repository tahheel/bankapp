# BASICS OF GENERATION OF ACCOUNT NUMBER

# import random

# class User():

#     def __init__(self,name,age,email,phone):

#         self.name = name
#         self. age = age
#         self. email = email
#         self.phone = phone

# class Account(User):

#     balance = 0
#     account_no = ''

#     def __init__(self,name,age,email,phone):
#         # INITIALZE CHILD CLASS
#         self.balance = 0
#         self.generate_acct_no

#         super().__init__(name,age,email,phone)
#          # INITIALIZE ATTRIBUTES FROM PARENT CLASS
        
#     def generate_acct_no(self): 

#         account_num = random.randint(20000000000,30000000000)

#         return str(account_num)


# x = Account('taheel',55,'taheel02@yahoo.com','0805555555')
# print(x.generate_acct_no())




# import random

# class User():

#     def __init__(self,name,age,email,phone):

#         self.name = name
#         self. age = age
#         self. email = email
#         self.phone = phone

# class Account(User):

#     balance = 0
#     account_no = ''

#     def __init__(self,name,age,email,phone):
#         # INITIALZE CHILD CLASS
#         self.balance = 0
#         self.generate_acct_no

#         super().__init__(name,age,email,phone)
#          # INITIALIZE ATTRIBUTES FROM PARENT CLASS
        
#     def generate_acct_no(self): 

#         account_num = random.randint(20000000000,30000000000)



# BASIC OF GENERATION OF ACCOUNT NUMBER

import random

# class User():

#     def __init__(self,name,age,email,phone):

#         self.name = name
#         self. age = age
#         self. email = email
#         self.phone = phone

# class Account(User):

#     balance = 0
#     account_no = ''

#     def __init__(self,name,age,email,phone):
#         # INITIALZE CHILD CLASS
#         self.balance = 0
#         self.generate_acct_no

#         super().__init__(name,age,email,phone)
#          # INITIALIZE ATTRIBUTES FROM PARENT CLASS
        
#     def generate_acct_no(self): 

#         account_num = random.randint(20000000000,30000000000)

#         return str(account_num)
        
#     def deposit(self, amount,comment = ''):

#         self.balance += amount #add deposit amount to value
#         self.store_history('credit',amount,comment)

#         print(f'weldone {self.name},your deposit of #{amount} was successful.Your new balance is #{self.balance}')


#     def withdraw(self,amount,comment = ''):

#         self.balance -= amount # ADD DEPOSITED VALUE TO BALANCE
#         self.store_history('debit',amount,comment,recipient.name)

#         print(f'weldone {self.name},your withdrawal of #{amount} was successful and your new balance is #{self.balance}.')

#     def store_history(self,type,amount,comment,reciever = None):
#         file = open('finanacial_statment.csv','a')
#         file.write(f'{type},{self.name},{amount},{comment},{reciever}\n')

#         print(type,amount,comment,reciever)    
    
#     def transfer(self,amount,recipient,comment = ''):

#         self.balance -= amount #REMOVE TRANSFER FROM SENDER'S BALANCE
#         recipient.balance += amount # ADD TRANSFER AMOUNT TO RECIPIENT'S BAL
#         self.store_history('transfer',amount,comment,recipient.name)

#         print(f'Congrats {self.name} your transfer of {amount} to {recipient.name} was successful,your new balance is #{self.balance}.')



# taheel = Account('taheel',55,'taheel02@yahoo.com','0805555555')
# print(taheel.account_no)
# taheel.deposit(30000)
# taheel.withdraw(2500)
# ogechi = Account('ogechi',33,'ogey@yahoo.com','08034444444')
# taheel.transfer(5000,ogechi,'chillaxin.')




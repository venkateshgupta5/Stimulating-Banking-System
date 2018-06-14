import random
from abc import ABCMeta, abstractmethod

class Account(metaclass = ABCMeta):
	def createNewSavingAccount():
		return 0

	@abstractmethod
	def validUser():
		return 0

	@abstractmethod
	def withdraw():
		return 0

	@abstractmethod
	def deposit():
		return 0

	@abstractmethod
	def showBalance():
		return 0 

class Banking:

	def __init__(self):
		self.savingsAccount={}

	def createNewSavingAccount(self, name, initialdeposit):
		self.accountnumber = random.randint(10000,99999)
		self.savingsAccount[self.accountnumber]=[name, initialdeposit]
		print("Account created. Note down your account number")
		print(self.accountnumber)

	def validUser(self, name, actno):
		if actno in self.savingsAccount.keys():
			if self.savingsAccount[actno][0] == name:
				print("Authentication Successful")
				self.accountnumber = actno
				return True
			else:
				print("Authentication Unsucessful ----> ")
				return False
		else:
			print("Authentication Failed")
			return False

		# else:
		# 	print("Invalid User")

	# def accessAccount(self):
	# 	print("Your name is :- ", self.name)
	# 	print("Your account number is :- ",self.number)
	# 	print("Your account balance is :- ",self.deposit)

	def withdraw(self, withdrawAmt):
		if withdrawAmt >= self.savingsAccount[self.accountnumber][1]:
			print("Insufficient Balance")

		else:
			self.savingsAccount[self.accountnumber][1] -= withdrawAmt
			print("Withdrawal Successful.")
			self.showBalance()

	def deposit(self, depositAmt):
		self.savingsAccount[self.accountnumber][1] += depositAmt
		print("Amount Deposited Successfully")
		self.showBalance()

	def showBalance(self):
		print("Your account balance is :-", self.savingsAccount[self.accountnumber][1])

bank = Banking()

while True:
	print("Select your option :- ")
	print("1. Create a new account with us")
	print("2. Access your account")
	print("3. Close")

	us = int(input())
	if us is 1:
		print("Enter your name --->")
		name = input()
		print("Enter the amount you want to deposit ")
		amount = int(input())
		bank.createNewSavingAccount(name, amount)

	elif us is 2:
		
		print("Enter your name")
		name = input()
		print("Enter your account number")
		acctno = int(input())

		boolean = bank.validUser(name, acctno) 

		if boolean is True:
			while  True:
			
				print("1. To withdraw amount")
				print("2. To deposit amount")
				print("3. To see balance")
				print("4. Quit")
		    

				ch = int(input())
				if ch is 1:
					print("Enter the amount to withdraw ")
					amount = int(input())
					bank.withdraw(amount)

				elif ch is 2:
					print("Enter amount to deposit ")
					amount = int(input())
					bank.deposit(amount)

				elif ch is 3:
					bank.showBalance()
				elif ch is 4:
					break

	elif us is 3:
		quit()






		

	
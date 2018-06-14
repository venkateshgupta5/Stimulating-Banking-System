import random
class Banking:

	z =[]
	print(z)


	def createNewSavingAccount(self, name, deposit):
		self.name = name
		self.balance = deposit
		self.number = random.randint(10000,99999)
		self.z.append(self.number)
		print("Hey {}. Your account number is {}. Current Balance {}.".format(self.name, self.number, self.balance))

	def validUser(self, actno):
		self.actno = actno
		if self.actno in self.z:
			return True
		# else:
		# 	print("Invalid User")

	def accessAccount(self):
		print("Your name is :- ", self.name)
		print("Your account number is :- ",self.number)
		print("Your account balance is :- ",self.deposit)

	def withdraw(self, withdrawAmt):
		self.withdrawAmt = withdrawAmt
		if self.withdrawAmt <= self.balance:
			self.balance = self.balance - self.withdrawAmt
			print("You withdrew :- ", self.withdrawAmt)
			print("Your balance is ", self.balance)
		else:
			print("You don\'t have sufficient balance")

	def deposit(self, depositAmt):
		self.deposit = depositAmt
		balance = self.deposit + balance
		print("You deposited :- ",self.deposit)
		print("Your updated balance is :- ",self.balance)

	def showBalance(self):
		print("Your account balance is :-", self.balance)

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

	if us is 2:
		print("Enter your account number")
		acctno = int(input())
		if bank.validUser(acctno) is False:
			print("Invalid User")

		else:
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

			else:
				quit()

	else:
		quit()





		

	
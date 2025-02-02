# 1
class String:
	def __init__(self):
		self.s = ""
	
	def getString(self):
		self.s = input("Enter string: ")
	
	def printString(self):
		print(self.s.upper())

# 2
class Shape:
	def area(self):
		return 0
class Square(Shape):
	def __init__(self, length):
		self.length = length
	
	def area(self):
		return self.length ** 2

# 3
class Rectangle(Shape):
	def __init__(self, length, width):
		self.length = length
		self.width = width
	
	def area(self):
		return self.length * self.width

# 4
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def show(self):
		print(f"({self.x}, {self.y})")
	
	def move(self, x, y):
		self.x = x
		self.y = y
	
	def dist(self, point2):
		return ((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2) ** 0.5

# 5
class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance
	
	def deposit(self, value):
		self.balance += value
		print(f"Deposited {value}, balance is {self.balance}")
	
	def withdraw(self, value):
		if value <= self.balance:
			self.balance -= value
			print(f"Withdrawed {value}, balance is {self.balance}")
		else:
			print(f"Not enough balance, maximum value is {self.balance}!")

# 6
def check_prime(number):
	if number < 2:
		return False
	for divisor in range(2, number):
		if number % divisor == 0:
			return False
	return True

def filter_prime_2(numbers):
	prime_numbers = list(filter(lambda number: check_prime(number), numbers))
	return prime_numbers
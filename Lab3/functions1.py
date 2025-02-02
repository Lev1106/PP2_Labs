import math, random

# 1
def grams_to_ounces(grams):
	ounces = 28.3495231 * grams
	return ounces

# 2
def fahrenheit_to_centigrade(F):
	C = (5 / 9) * (F - 32)
	return C

# 3
def solve(numheads, numlegs):
	for rabbits in range(numheads + 1):
		chickens = numheads - rabbits
		if chickens * 2 + rabbits * 4 == numlegs:
			return (chickens, rabbits)
	#None if no solution

# 4
def check_prime(number):
	if number < 2:
		return False
	for divisor in range(2, number):
		if number % divisor == 0:
			return False
	return True

def filter_prime(numbers):
	prime_numbers = [number for number in numbers if check_prime(number)]
	return prime_numbers

# 5
def all_permutations(string, cur = []):
	if len(cur) == len(string):
		for i in cur:
			print(string[i], end = '')
		print()
		return
	
	for i in range(len(string)):
		if i not in cur:
			cur.append(i)
			all_permutations(string, cur)
			cur.pop()

# 6
def all_words_reverse(string):
	words = string.split(' ')
	for word in words:
		print(word[::-1], end = ' ')
	print()

# 7
def has_33(nums):
	for i in range(len(nums) - 1):
		if nums[i] == 3 and nums[i + 1] == 3:
			return True
	return False

# 8
def spy_game(nums):
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			for k in range(j + 1, len(nums)):
				if nums[i] == 0 and nums[j] == 0 and nums[k] == 7:
					return True
	return False

# 9
def volume(radius):
	return 4 / 3 * math.pi * (radius ** 3)

# 10
def unique_elements(lst):
	unique = []
	for i in lst:
		if i not in unique:
			unique.append(i)
	return unique

# 11
def is_palindrome(string):
	reversed_string = string[::-1]
	return string == reversed_string

# 12
def histogram(lst):
	for length in lst:
		print('*' * length)

# 13
def guess_the_number():
	name = input("Hello! What is your name?\n")

	print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
	number = random.randint(1, 20)
	count = 0

	while True:
		guess_number = int(input("Take a guess.\n"))
		if guess_number < 1 or guess_number > 20:
			print("Incorrect guess, try again!")
			continue
		count += 1
		if guess_number > number:
			print("Your guess is too high.")
		elif guess_number < number:
			print("Your guess is too low.")
		else:
			print(f"Good job, {name}! You guessed my number in {count} guesses!")
			return
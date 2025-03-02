import time, math, functools

# 1
def multiply_all_numbers(lst):
	return functools.reduce(lambda x, y: x * y, lst, 1)

# 2
def upper_lower_case(string):
	return functools.reduce(lambda x, y: (x[0] + y.isupper(), x[1] + y.islower()), string, (0, 0))

# 3
def is_palindrome(string):
	return string == "".join(reversed(string))

# 4
def sqrt_after_time(n, ms):
	time.sleep(ms / 1000)
	return math.sqrt(n)

# 5
def all_true(tup):
	return all(tup)
	#return functools.reduce(lambda x, y: x and y, tup)
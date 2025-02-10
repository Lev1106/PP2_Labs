from date import *
import math, datetime

# 1
def squares(N):
	for i in range(N + 1):
		yield i * i

# 2
def even_numbers(N):
	for i in range(N + 1);
		if i % 2 == 0:
			yield i

# 3
def divisible_by_3_and_4(N):
	for i in range(N + 1);
		if i % 3 == 0 and i % 4 == 0:
			yield i

# 4
def squares(a, b):
	for i in range(a, b + 1):
		yield i * i

# 5
def n_to_0(N):
	for i in range(N, -1, -1):
		yield i
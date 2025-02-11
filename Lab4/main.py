from date import *
from generators import *
from json import *
from Math import *
from Json import *
import math, datetime

def date_examples():
	print("Example 1. Five days before today was", five_days_ago())

	print("\nExample 2")
	three_days()

	print("\nExample 3")
	d = datetime.datetime(2025, 2, 10, 15, 50, 39, 123456)
	print("Datetime is", d)
	print("Datetime with dropped microseconds", drop_microseconds(d))

	print("\nExample 4")
	d = datetime.datetime(2025, 1, 13, 8, 0, 0)
	print(f"Start of spring semester was {date_difference(d, datetime.datetime.now())} seconds ago")


def generators_examples():
	print("Example 1. Squares of numbers from 0 to 12: ", end = '')
	for i in squares1(12):
		print(i, end = ' ')
	
	n = int(input("\nExample 2. Enter integer: "))
	print(f"Even numbers from 0 to {n}: ", end = '')
	lst = list(even_numbers(n))
	for i in lst:
		print(i, end = (', ' if i != lst[-1] else ''))

	print("\nExample 3. Numbers divisible by 3 and 4 from 0 to 45: ", end = '')
	for i in divisible_by_3_and_4(45):
		print(i, end = ' ')

	print("\nExample 4. Squares from 7 to 18: ", end = '')
	for i in squares(7, 18):
		print(i, end = ' ')

	print("\nExample 5. Numbers from 9 to 0: ", end = '')
	for i in n_to_0(9):
		print(i, end = ' ')

	print()


def math_examples():
	deg = float(input("Example 1. Input degree: "))
	print("Output radian:", degree_to_radian(deg))

	h = float(input("Example 2. Height: "))
	a = float(input("Base, first value: "))
	b = float(input("Base, second value: "))
	print("Expected Output (area of trapezoid):", trapezoid_area(h, a, b))

	n = float(input("Example 3. Input number of sides: "))
	l = float(input("Input the length of a side: "))
	print("The area of the polygon is:", area_of_polygon(n, l))

	a = float(input("Example 4. Length of base: "))
	h = float(input("Height of parallelogram: "))
	print("Expected Output (area of parallelogram):", area_of_parallelogram(a, h))


def main():
	print("=== DATES ===")
	date_examples()
	print("\n=== GENERATORS ===")
	generators_examples()
	print("\n=== MATH ===")
	math_examples()
	print("\n=== JSON ===")
	parse()


if __name__ == "__main__":
    main()
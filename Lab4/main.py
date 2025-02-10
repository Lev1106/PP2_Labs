from date import *
import math, datetime

def date_examples():
	print("Example 1")
	print("Five days before today was", five_days_ago())

	print("\nExample 2")
	three_days()

	print("\nExample 3")
	d = datetime.datetime(2025, 2, 10, 15, 50, 39, 1234)
	print("Datetime is", d)
	print("Datetime with dropped microseconds", drop_microseconds(d))

	print("\nExample 4")
	print(f"Start of spring semester was {date_difference(datetime.datetime(2025, 1, 13, 8, 0, 0), datetime.datetime.now())} seconds ago")

def main():
	print("=== DATES ===")
	date_examples()
	print("\n=== GENERATORS ===")
	#functions2()


if __name__ == "__main__":
    main()
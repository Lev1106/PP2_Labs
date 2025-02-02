from functions1 import (
	grams_to_ounces,
	fahrenheit_to_centigrade,
	solve,
	filter_prime,
	all_permutations,
	all_words_reverse,
	has_33,
	spy_game,
	volume,
	unique_elements,
	is_palindrome,
	histogram,
	guess_the_number
)
from functions2 import (
	is_good_movie,
	good_movies,
	movies_by_category,
	average_by_list,
	average_by_category
)
from classes import (
	String,
	Shape,
	Square,
	Rectangle,
	Point,
	Account,
	filter_prime_2
)
import math
from movies import movies

def functions1():
	print("Example 1")
	print("2 grams =", grams_to_ounces(2), "ounces")
	print("0.035273962 grams =", grams_to_ounces(1.0 / 28.3495231), "ounces")

	print("\nExample 2")
	print("41 °F =", fahrenheit_to_centigrade(41), "°C")
	print("81.9 °F =", fahrenheit_to_centigrade(81.9), "°C")

	print("\nExample 3")
	print("(Heads, legs) = ", solve(35, 94))
	print(solve(44, 123))

	print("\nExample 4")
	print("Primes:", filter_prime([1, 2, 3, 4, 5, 6, 7, 13, 15, 234346, 359209, 777777]))

	print("\nExample 5")
	all_permutations("aabc")
	all_permutations("qwe")

	print("\nExample 6")
	all_words_reverse("We are ready")
	all_words_reverse("Good afternoon!")

	print("\nExample 7")
	print(has_33([1, 3, 3]))
	print(has_33([1, 3, 1, 3]))
	print(has_33([3, 1, 3]))

	print("\nExample 8")
	print(spy_game([1,2,4,0,0,7,5]))
	print(spy_game([1,0,2,4,0,5,7]))
	print(spy_game([1,7,2,0,4,5,0]))

	print("\nExample 9")
	for radius in [10, (3.0 / 4) ** (1.0 / 3)]:
		print(f"Volume of sphere with radius {radius} is {volume(radius)}")

	print("\nExample 10")
	print(unique_elements([1, 2, 1, 4, 5, 2, 2, 5, 3]))
	print(unique_elements([3, 1, 4, 1, 5, 9, 2]))

	print("\nExample 11")
	for word in ["madam", "Hello!", "racecar"]:
		print(f"{word} is " + ("" if is_palindrome(word) else "not ") + "palindrome")

	print("\nExample 12")
	for lst in [[4, 9, 7], [5, 6, 7, 8, 9, 1, 0, 2]]:
		print("Histogram for", lst)
		histogram(lst)

	print("\nExample 13")
	guess_the_number()

def functions2():
	print("Example 1")
	for movie in [{"name": "Detective", "imdb": 7.0, "category": "Suspense"}, {"name": "Exam", "imdb": 4.2, "category": "Thriller"}]:
		print(f"\"{movie["name"]}\" is " + ("" if is_good_movie(movie) else "not ") + "good movie")

	print("\nExample 2")
	print(good_movies())

	print("\nExample 3")
	for category in ["Romance", "Adventure"]:
		print(f"{category}:", movies_by_category(category))

	print("\nExample 4")
	print(f"Average IMDB score is {average_by_list(movies)}")

	print("\nExample 5")
	for category in ["Thriller", "Romance", "Suspense"]:
		print(f"Average IMDB score for {category} is {average_by_category(category)}")

def classes():
	print("Example 1")
	s = String()
	s.getString()
	s.printString()

	print("\nExample 2")
	sh = Shape()
	print("Area of shape by default is", sh.area())
	sq = Square(9)
	print("Area of square 9x9 is", sq.area())

	print("\nExample 3")
	rect = Rectangle(10.5, 4)
	print("Area of rectange 10.5x4 is", rect.area())

	print("\nExample 4")
	p1 = Point(5, 2)
	p1.show()
	p1.move(3, 4)
	p1.show()
	p2 = Point(-1, -3)
	p2.show()
	print("Distance is", p1.dist(p2))

	print("\nExample 5")
	ac = Account("Lev", 69)
	ac.deposit(31)
	ac.withdraw(70)
	ac.withdraw(123)

	print("\nExample 6")
	print("Primes:", filter_prime_2([1, 2, 3, 4, 5, 6, 7, 13, 15, 234346, 359209, 777777]))

def main():
	print("=== FUNCTIONS 1 ===")
	functions1()
	print("\n=== FUNCTIONS 2 ===")
	functions2()
	print("\n=== CLASSES ===")
	classes()


if __name__ == "__main__":
    main()
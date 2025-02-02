from movies import movies

# 1
def is_good_movie(movie):
	return movie["imdb"] > 5.5

# 2
def good_movies():
	good_movies_list = [movie for movie in movies if movie["imdb"] > 5.5]
	return good_movies_list

# 3
def movies_by_category(category_name):
	categorized_movies = [movie for movie in movies if movie["category"] == category_name]
	return categorized_movies

# 4
def average_by_list(movies):
	sum = 0.0
	count = len(movies)

	for movie in movies:
		sum += movie["imdb"]
	average = sum / count
	return average


# 5
def average_by_category(category_name):
	categorized_movies = movies_by_category(category_name)
	return average_by_list(categorized_movies)

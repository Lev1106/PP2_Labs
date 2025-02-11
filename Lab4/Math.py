import math

# 1
def degree_to_radian(degree):
	return round(degree * math.pi / 180, 6)

# 2
def trapezoid_area(height, base1, base2):
	return (base1 + base2) / 2 * height

# 3
def area_of_polygon(n, length):
	apothem = length / (2 * math.tan(math.pi / n))
	return round((n * length * apothem) / 2, 6)

# 4
def area_of_parallelogram(base, height):
	return base * height
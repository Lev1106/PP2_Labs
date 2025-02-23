import re

# 1
def task1(s):
	return re.match(r"ab*$", s)

# 2
def task2(s):
	return re.match(r"ab{2,3}$", s)

# 3
def task3(s):
	return re.findall(r"\b[a-z]+(?:_[a-z]+)*\b", s)

# 4
def task4(s):
	return re.findall(r"\b[A-Z][a-z]*", s)

# 5
def task5(s):
	return re.match(r"a.*b$", s)

# 6
def task6(s):
	return re.sub(r"[\s,.]", ":", s)

# 7
def task7(s):
	return re.sub(r"_([a-zA-Z])", lambda match: match.group(1).upper(), s)

# 8
def task8(s):
	return re.split(r"[A-Z]", s)

# 9
def task9(s):
	return re.sub(r"[A-Z]", lambda match: (" " if match.start() != 0 else "") + match.group(0), s)

# 10
def task10(s):
	s = re.sub(r'\b[A-Z]', lambda match: match.group(0).lower(), s)
	return re.sub(r"[A-Z]", lambda match: ("_" if match.start() != 0 else "") + match.group(0).lower(), s)


print("Example 1")
for s in ["a", "aa", "abb", "abbd", "abbb", "bcda", "abbbbbb", "bba", "ab", "adbbb", "cabb"]:
	if task1(s) is None:
		print(s, "doesn't match")
	else:
		print(s, "matches")

print("\nExample 2")
for s in ["a", "aa", "abb", "abbd", "abbb", "bcda", "abbbbbb", "bba", "ab", "adbbb", "cabb"]:
	if task2(s) is None:
		print(s, "doesn't match")
	else:
		print(s, "matches")

print("\nExample 3")
s = "ab_cd Hello_worlD abb h_e_l_l_o a__a"
print("Found sequences:", task3(s))

print("\nExample 4")
s = "Hello World! aBc D e"
print("Found sequences:", task4(s))

print("\nExample 5")
for s in ["ba", "aa", "abb", "abcdeb", "abba", "bcda", "a_q_w_e_r489t^b", "bba", "ab", "Abb"]:
	if task5(s) is None:
		print(s, "doesn't match")
	else:
		print(s, "matches")

print("\nExample 6")
s = "Python program to replace all occurrences of space, comma, or dot with a colon."
print("Replaced string:", task6(s))

print("\nExample 7")
s = "Python_program t_o convert_snake_case_string to CAMEL_CASE str_Ing."
print("Replaced string:", task7(s))

print("\nExample 8")
s = "Python Program To sPlit a STRING at uPPercase letters."
print("Splitted string:", task8(s))

print("\nExample 9")
s = "PythonProgramToInsertSpacesBetweenWordsStartingWithCapitalLetters"
print("Replaced string:", task9(s))

print("\nExample 10")
s = "Python ProgramToConvert aGiven camelcase STRING tO SnAkE CasE."
print("Replaced string:", task10(s))
from builtin_functions import *
from dir_and_files import *

print("Builtin functions. Example 1")
print(multiply_all_numbers([5, 3, 6]))
print(multiply_all_numbers([191, 7]))

print("\nExample 2")
print(upper_lower_case("Hello World!"))

print("\nExample 3")
print(is_palindrome("madam"))
print(is_palindrome("palindrome"))

print("\nExample 4")
print("Square root of 25100 after 2123 miliseconds is", sqrt_after_time(25100, 2123))

print("\nExample 5")
print(all_true((1, 8, True)))
print(all_true((True, False)))





print("\n\nDirectories and files. Example 1")
print(directories("./Lab4"))
print(files("./Lab4"))
print(directories_files("./Lab4"))

print("\nExample 2")
for file in ["./Lab6/dir_and_files.py", "./Lab6/file_tasks/test1.txt", "./Lab6/a.txt"]:
	print(f"{file}. Exists, readable, writable, executable: {access_check(file)}")

print("\nExample 3")
for path in ["./Lab6/dir_and_files.py", "./Lab5/row.txt"]:
	print(f"{path}. File and directory are {exists(path)}")

print("\nExample 4")
for path in ["./Lab6/main.py", "./Lab5/row.txt"]:
	print(f"Number of lines in {path} is {count_lines(path)}")

print("\nExample 5")
for path in [("./Lab6/file_tasks/test.txt", [3, 5, "qwe", True, None])]:
	print(write_list(path[0], path[1]))

print("\nExample 6")
for path in ["./Lab6/file_tasks"]:
	print(generate_files_A_Z(path))

print("\nExample 7")
path1 = "./Lab6/dir_and_files.py"
path2 = "./Lab6/file_tasks/W.txt"
print(copy(path1, path2))
path1 = "./Lab6/main.py"
path2 = "./Lab6/1.txt"
print(copy(path1, path2))

print("\nExample 8")
for path in ["./Lab6/file_tasks/A.txt", "./Lab6/1.txt"]:
	print(delete(path))
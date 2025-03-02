import os

# 1
def directories(path):
	return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def files(path):
	return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def directories_files(path):
	return os.listdir(path)


# 2
def access_check(path):
	return [os.access(path, os.F_OK), os.access(path, os.R_OK),
		 	os.access(path, os.W_OK), os.access(path, os.X_OK)]


# 3
def exists(path):
	if not os.path.exists(path):
		return False
	return [os.path.basename(os.path.abspath(path)), os.path.dirname(os.path.abspath(path))]

# 4
def count_lines(path):
	if not exists(path):
		return "File {path} doesn't exist"
	if not access_check(path)[1]:
		return "Problems with access to {path}"
	with open(path, "r") as f:
		read_data = f.read()
	return read_data.count("\n") + 1

# 5
def write_list(path, lst):
	if not exists(path):
		return "File {path} doesn't exist"
	if not access_check(path)[2]:
		return "Problems with access to {path}"
	with open(path, "w") as f:
		f.write(str(lst))
	print(f"Wrote {path[1]} into {path[0]}")

# 6
def generate_files_A_Z(path):
	for name in range(ord('A'), ord('Z') + 1):
		file_path = os.path.join(path, chr(name) + ".txt")
		with open(file_path, "w+") as f:
			f.write("")
	print(f"Generated 26 files named A.txt, B.txt, ..., Z.txt")

# 7
def copy(path1, path2):
	if not exists(path1):
		return f"File {path1} doesn't exist"
	if not access_check(path1)[1]:
		return f"Problems with access to {path1}"
	with open(path1, "r") as f1, open(path2, "w") as f2:
		f2.write(f1.read())
	return f"Successfully copied content from {path1} to {path2}"

# 8
def delete(path):
	if not exists(path):
		return "File {path} doesn't exist"
	if not access_check(path)[2]:
		return "Problems with access to {path}"
	os.remove(path)
	return f"Successfully deleted {path}"
import os
import sys
import requests

wanted = ["c", "h"]


def Get_Username(argv):
    """"Try to find an author file."""

    print("Author file: ", end="")
    try:
        dire = os.listdir(argv[1])
    except OSError:
        try:
            dire = os.listdir("./")
        except OSError:
            return os.getlogin()
    for x in dire:
        if x.lower() == "author":
            try:
                with open(f"{argv[1]}/{x}", "r") as f:
                    print("\033[32mV\033[0m")
                    return(f.read().split("\n")[0])
            except IOError:
                continue
    print("\033[91mX\033[0m")
    return os.getlogin()


username = Get_Username(sys.argv)
print(f"Username: {username}\n")


def Checker(path):

	try:
		with open(f"{path}", "r") as f:
			reading = f.readlines()
	except OSError:
		return None

	for y, z in zip([reading[5], reading[7], reading[8]], (6, 8, 9)):
		if username not in y:
			print(f"\033[91m{path}: Wrong Username in file!	line {z}\033[0m")
			return None
	print(f"\033[92m{path}: OK!\033[0m")


def Main(argv):

	if len(argv) < 2:
		print("Error. Not enough arguments.\n\nDo 'python3 HC.py \{filepath\} \{filepath2\} ...'")
		return None

	for x in argv[1:]:
		if ".c" not in x and ".h" not in x:
			try:
				dire = os.listdir(f"{x}")

				for y in dire:
					var = y.split(".")
					try:
						if y.split(".")[1] in wanted:
							Checker(f"{x}/{y}")
					except IndexError:
						continue

			except OSError:
				print("Unexpected error.")
				return None
		else:
			Checker(x)
	print("\n--------------------\tNorminette\t--------------------\n")
	os.system(f"norminette {argv[1]}")


Main(sys.argv)


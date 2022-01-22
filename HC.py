import os
import sys

def checker(path):

	try:
		with open(f"{path}", "r") as f:
			reading = f.readlines()
	except OSError:
		return None

	for y in [reading[5], reading[7], reading[8]]:
		if os.getlogin() not in y:
			print(f"\33[91m{path}: Wrong Username in file!\033[0m")
			break
	print(f"\33[92m{path}: OK!\033[0m")



def main(argv):

	if len(argv) < 2:
		print("Error. Not enough arguments.\n\npython3 HC.py \{filepath\} \{filepath2\} ...")
		return None

	for x in argv[1:]:
		if ".c" not in x and ".h" not in x:
			dire = os.listdir(f"{x}")
			for y in dire:

				if "." in y and ".o" not in y and "Makefile" != x:
					checker(f"{x}/{y}")
		else:
			checker(x)

main(sys.argv)

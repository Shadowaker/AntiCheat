import os
import sys

username = os.getlogin()
wanted = [".c", ".h"]

def checker(path):

	try:
		with open(f"{path}", "r") as f:
			reading = f.readlines()
	except OSError:
		return None

	for y, z in zip([reading[5], reading[7], reading[8]], (6, 8, 9)):
		if username not in y:
			print(f"\33[91m{path}: Wrong Username in file!	line {z}\033[0m")
			break
	print(f"\33[92m{path}: OK!\033[0m")


def main(argv):

	if len(argv) < 2:
		print("Error. Not enough arguments.\n\nDo 'python3 HC.py \{filepath\} \{filepath2\} ...'")
		return None

	for x in argv[1:]:
		if ".c" not in x and ".h" not in x:
			try:
				dire = os.listdir(f"{x}")

				for y in dire:
					if [e for e in wanted if e in x]:
						checker(f"{x}/{y}")

			except OSError:
				print("Unexpected error.")
				return None
		else:
			checker(x)

main(sys.argv)

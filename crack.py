#!/usr/bin/env python3

# Prototype program that offers two modes of operation
#   - Make a rainbow table given a wordlist
#   - Crack an input hash using the rainbow table

from hashlib import md5, sha1, sha224, sha256, sha384, sha512
import sys

FUNC = [md5, sha1, sha224, sha256, sha384, sha512]


def make_table(wordlist):
	sorted_pass = list()
	with open(wordlist, "r", encoding="utf-8") as source:
		words = source.readlines()
		for word in words:
			sorted_pass.append(word.strip())
		sorted_pass = sorted(sorted_pass)
		source.close()
	with open("rainbow_table.txt", "a", encoding="utf-8") as sink:
		for passwd in sorted_pass:
			sink.write(passwd)
			for func in FUNC:
				sink.write(",")
				sink.write(func(passwd.encode("utf-8")).hexdigest())
			sink.write("\n")
		sink.close()


def crack(hash: str):
	hash = hash.strip()
	with open("rainbow_table.txt", "r", encoding="utf-8") as source:
		words = source.readlines()
		for word in words:
			if word.count(hash) > 0:
				return word.split(",")[0]
		source.close()
	return "Plaintext not found"


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Error: Missing operation mode.\nUsage: ./crack.py MODE OPERAND")
		sys.exit(0)
	else:
		if len(sys.argv) < 3:
			print("Error: Missing operand.\nUsage: ./crack.py MODE OPERAND")
			sys.exit(0)
		else:
			if sys.argv[1] == "make":
				make_table(sys.argv[2])
			elif sys.argv[1] == "find":
				print(crack(sys.argv[2]))
			else:
				print("Error: Invalid operation mode.")
#!/usr/bin/env python3

# Prototype program that offers two modes of operation
#   - Make a rainbow table given a wordlist
#   - Crack an input hash using the rainbow table

from hashlib import md5, sha1, sha224, sha256, sha384, sha512
import sys
import collections

FUNC = {'md5':md5, 'sha1':sha1, 'sha224':sha224, 'sha256':sha256, 'sha384':sha384, 'sha512':sha512}


def make_table(wordlist, alg):
	d = dict()
	with open(wordlist, "r", encoding="utf-8") as source:
		words = source.readlines()
		for word in words:
			word = word.strip()
			d[FUNC[alg](word.encode("utf-8")).hexdigest()] = word
		od = collections.OrderedDict(sorted(d.items()))
		source.close()
	with open(f"{alg}_table.txt", "a", encoding="utf-8") as sink:
		for key, value in od.items():
			sink.write(f"{key.strip()},{value.strip()}\n")
		sink.close()


def search(needle: str, haystack: list, lb: int, ub: int) -> int:
	if ub >= lb:
		mp = (lb + ub) // 2
		if haystack[mp].split(',')[0] == needle:
			return mp
		elif haystack[mp].split(',')[0] < needle:
			return search(needle, haystack, mp + 1, ub)
		else:
			return search(needle, haystack, lb, mp - 1)
	else:
		return -1


def crack(hash: str, alg: str):
	hash = hash.strip()
	with open(f"{alg.lower()}_table.txt", "r", encoding="utf-8") as source:
		lines = source.readlines()
		index = search(hash, lines, 0, len(lines) - 1)
		if index >= 0:
			return lines[index].split(',')[1].strip()
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
				make_table(sys.argv[2], sys.argv[3])
			elif sys.argv[1] == "find":
				print(crack(sys.argv[2], sys.argv[3]).strip())
			else:
				print("Error: Invalid operation mode.")
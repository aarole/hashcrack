#!/usr/bin/env python3

# Prototype identification function written in Python3

import sys

# Map length to algorithm
# TODO: add support for more algorithms
MAP = {32:"MD5", 40:"SHA1", 56:"SHA224", 64:"SHA256", 96:"SHA384", 128:"SHA512"}


# Create function to identify the hash
def identify(hash: str):
	# First condition is that the input must be alphanumeric
	if hash.isalnum():
		# Use the length of input as the key to determine the algorithm used
		type = MAP[len(hash.strip())]
		# Return the type
		return type
	else:
		return None


if __name__ == "__main__":
	# Ensure that the hash is passed as an argument
	if len(sys.argv) < 2:
		print("Error: Hash missing\nUsage: ./id.py HASH")
		sys.exit(0)
	# Identify the hash type and print the output
	print(identify(sys.argv[1]))

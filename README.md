# Hashcrack
Automated, web-based hash identifier and cracker.  
**URL:** https://hashcrack.itsnotifbutwhen.com 

## Identification
Identifies hashes based on type of characters and length of input.

Supported types:
* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512

## Cracking
Once the hash is identified, the program will perform a rainbow table attack to crack the hash.  
In addition to the hash, the crack function also needs the detected algorithm as one of the inputs.

### Method
The crack function performs a binary search using the appropriate list of precomputed hashes (determined by the identification function).

## TODO
* Implement method to keep the tables updated
* Improve website design

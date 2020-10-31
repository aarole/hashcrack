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

## Setup
To test the program using your local environment, first download apache2 and php:
* Clone the repository to obtain the files
```
git clone https://github.com/aarole/hashcrack.git
```
* Copy the files to the /var/www/html directory and change directories
```
cp ./hashcrack/* /var/www/html
cd /var/www/html/
```
* Make the python files executable
```
chmod +x ./*.py
```
* Make the rainbow tables
```
./crack.py make /path/to/wordlist [md5/sha1/sha224/sha356/sha384/sha512]
```
* Start a web browser and navigate to http://localhost:80/

## TODO
* Implement method to keep the tables updated
* Improve website design

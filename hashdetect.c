#include <stdio.h>
#include <string.h>

#define md5Length 32
#define sha1Length 40
#define sha224Length 56
#define sha256Length 64
#define sha384Length 96
#define sha512Length 128

int main()
{
    char inputHash[250], i;
    char proceed = 'y';
    int hashLength;

    printf("Please enter a hash value: ");
    gets(inputHash);

    hashLength = strlen(inputHash);

    if (hashLength == md5Length)
    {
        printf("The hash entered is MD5");
    }

    if (hashLength == sha1Length)
    {
        printf("The hash entered is SHA1");
    }

    if (hashLength == sha224Length)
    {
        printf("The hash entered is SHA224");
    }

    if (hashLength == sha256Length)
    {
        printf("The hash entered is SHA256");
    }

    if (hashLength == sha384Length)
    {
        printf("The hash entered is SHA384");
    }

    if (hashLength == sha512Length)
    {
        printf("The hash entered is SHA512");
    }
    else 
    {
        printf("Not a hash function");
    }

    return 0;
}
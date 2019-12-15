#!/usr/bin/python3

from hashlib import sha256
import getpass
import sys

''' SECRET_KEY is a personal key to use as an extra salt that should be different for everyone.
Change this to some other sufficiently high-entropy string.
WARNING: Changing the secret key will generate completely different passwords, so do not change
it after you first set it unless you want to reset all of your passwords. '''
SECRET_KEY = "SUPERSECRETSTRING"

LENGTH = 18     # Length of generated password
ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')

''' Returns the raw hex of SHA-256 hash of a salt+password combination'''
def get_hexdigest(salt, password):
    return sha256((salt + password).encode('utf-8')).hexdigest()

''' Adds some extra salt'''
def gen_password(plaintext, service):
    salt = get_hexdigest(SECRET_KEY, service)
    hsh = get_hexdigest(salt, plaintext)
    return ''.join(salt + hsh)

''' Coverts the raw hex into a usable password.'''
def password(plaintext, service, length=LENGTH, alphabet=ALPHABET):
    # Converts the hexdigest into a decimal
    num = int(gen_password(plaintext, service), LENGTH)

    # Determines the base that num will be converted to,
    # Base-74 with the default alphabet
    num_chars = len(alphabet)

    # Generates a password by character
    chars = []
    while len(chars) < length:
        num, rem = divmod(num, num_chars)
        chars.append(alphabet[rem])
    return ''.join(chars)

''' Print usage information.'''
def usage():
    print("Usage: {} [service]".format(sys.argv[0]))
    sys.exit(1)

def main(service):
    service.replace(" ", "")
    master = getpass.getpass()
    pw = password(master, service)
    print(pw)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    main(sys.argv[1])
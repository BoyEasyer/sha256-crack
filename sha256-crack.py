from pwn import *
import sys
import argparse

# Function to perform SHA-256 hash cracking
def sha256_crack(wanted_hash, password_file):
    attempts = 0

    with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
        try:
            with open(password_file, "r", encoding='latin-1') as password_list:
                for password in password_list:
                    password = password.strip("\n").encode('latin-1')
                    password_hash = sha256sumhex(password)
                    p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
                    
                    if password_hash == wanted_hash:
                        p.success("Password found after {} attempts! '{}' hashes to '{}'!".format(attempts, password.decode('latin-1'), password_hash))
                        exit()
                    
                    attempts += 1
            p.failure("Password hash not found!")
        except FileNotFoundError:
            p.failure("Password file '{}' not found!".format(password_file))

# Argument parser for command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SHA-256 Hash Cracker")
    parser.add_argument("hash", help="SHA-256 hash to crack")
    parser.add_argument("-P", "--password-file", default="/usr/share/wordlists/rockyou.txt", help="Path to password file (default: /usr/share/wordlists/rockyou.txt)")

    args = parser.parse_args()

    # Call the SHA-256 hash cracking function with the provided arguments
    sha256_crack(args.hash, args.password_file)

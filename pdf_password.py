#!/usr/bin/env python
"""Brute force a protected PDF using passwords from a list file"""

import argparse
import sys
import pikepdf
from tqdm import tqdm


def load_passwords(password_list):
    """Load list of passwords to try"""

    # Load all passwords into memory so we can show progress against list
    return [line.strip() for line in open(password_list, encoding='utf8')]


def force_password(filename, passwords):
    """Try the list of passwords against the given PDF file"""

    for password in tqdm(passwords, f'Decrypting {filename}'):
        try:
            # open PDF file
            with pikepdf.open(filename, password=password) as _:
                # Password correct and PDF decrypted successfully
                return password
        except pikepdf._qpdf.PasswordError:
            # Wrong password so just carry on
            pass

    return None


def main():
    """Parse arguments and start process"""

    parser = argparse.ArgumentParser(
        description='Find the password for a PDF file.')
    parser.add_argument('-p', '--password-file',
                        default='wordlist.txt', help='Password List File')
    parser.add_argument('pdf_file', nargs='+', help='PDF Files')
    args = parser.parse_args()

    pdf_files = args.pdf_file
    wordlist = args.password_file
    passwords = load_passwords(wordlist)

    for pdf_file in pdf_files:
        try:
            password = force_password(pdf_file, passwords)

            if password is None:
                print(f'Did not find password for {pdf_file}')
            else:
                print(f'Password for {pdf_file} is: {password}')
        except FileNotFoundError:
            print(f'Error: Did not find file {pdf_file}', file=sys.stderr)


if __name__ == "__main__":
    main()

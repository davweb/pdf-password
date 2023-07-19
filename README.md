# pdf-password
Brute Force PDF File passwords

## How to Use
1. Download a password word list file.  For example, [the `rockyou` list](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).
2. Copy the password word list to checkout directory and rename it to `wordlist.txt`.
3. Set up a python virtual environment with:

    ```
    python -m venv --prompt pdf-password .venv
    ```

4. Source the virtual environment with:

    ```
    source .venv/bin/activate
    ```

5. Install required packages using `pip`:

    ```
    pip install pip-tools
    pip-compile requirements.in
    pip-sync
    ```

6. Run the script with:

    ```
    python pdf_password.py protected.pdf
    ```

## References
- [https://www.thepythoncode.com/article/crack-pdf-file-password-in-python](https://www.thepythoncode.com/article/crack-pdf-file-password-in-python)
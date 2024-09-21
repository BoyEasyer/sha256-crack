```markdown
# SHA-256 Hash Cracker

This Python tool is designed to brute-force crack SHA-256 hashes by attempting various passwords from a specified password file. It can either use a user-provided password list or the default password list located at `/usr/share/wordlists/rockyou.txt`.

## Features

- Brute-forces SHA-256 hashes using a password list.
- Allows users to specify a custom password file via command-line arguments.
- Default password file is set to `/usr/share/wordlists/rockyou.txt`.
- Provides real-time feedback on attempts and success/failure.

## Requirements

This tool depends on the `pwntools` library for efficient hashing and logging functionality. You can install the required library using `pip`:

```bash
pip install pwntools
```

## Usage

### Command-Line Arguments

The tool accepts the following command-line arguments:

- `hash`: The SHA-256 hash you wish to crack (required).
- `-P` or `--password-file`: The path to the password file to use (optional). If not provided, it defaults to `/usr/share/wordlists/rockyou.txt`.

### Example Commands

1. **With Custom Password File**:

   ```bash
   python sha256_cracker.py <sha256_hash> -P /path/to/password_file.txt
   ```

   Replace `<sha256_hash>` with the SHA-256 hash you want to crack, and `/path/to/password_file.txt` with your own password file.

2. **With Default Password File**:

   If no password file is specified, the tool will default to using `/usr/share/wordlists/rockyou.txt`:

   ```bash
   python sha256_cracker.py <sha256_hash>
   ```

### Example

```bash
python sha256_cracker.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd31de0dbf4b1da53a4 -P /usr/share/wordlists/custom_passwords.txt
```

### Output

The tool prints each password attempt along with its corresponding SHA-256 hash. When a valid password is found, the script stops and prints the successful match.

Example output:

```bash
[0] Attempting password: '123456'
[1] Attempting password: 'password'
[>] Password found after 1 attempts! 'password' hashes to '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd31de0dbf4b1da53a4'!
```

If no matching password is found after the entire list is exhausted, the tool will notify you that the password hash could not be found.

### Legal Disclaimer

This tool is intended for **educational purposes only**. You are responsible for ensuring that you have legal authorization to attempt cracking passwords or hashes. Unauthorized use of this tool may be illegal in your country or jurisdiction.

## License

This project is licensed under the MIT License.

```

This `README.md` provides clear instructions on how to use the tool, including example commands, expected outputs, and legal disclaimers to ensure ethical use.

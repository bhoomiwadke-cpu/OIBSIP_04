# OIBSIP_04
password_generator<BR>
AUTHOR BHOOMI SANJAY WADKE
# Advanced Password Generator

A simple desktop application built with Python and Tkinter that generates secure, customizable passwords.

## Features

- Generate passwords of any length
- Choose character sets to include:
  - Letters (uppercase and lowercase)
  - Numbers (0–9)
  - Symbols (punctuation characters)
- Copy generated passwords to clipboard with one click

## Requirements

- Python 3.x (Tkinter is included in the standard library)

No additional packages need to be installed.

## Usage

Run the script from the terminal:

```bash
python password_generator.py
```

### Steps

1. Enter your desired password length in the **Password Length** field.
2. Check or uncheck the character set options:
   - **Include Letters** – adds A–Z and a–z
   - **Include Numbers** – adds 0–9
   - **Include Symbols** – adds punctuation characters
3. Click **Generate Password** to create a new password.
4. Click **Copy to Clipboard** to copy it for use elsewhere.

## Notes

- At least one character set must be selected before generating a password.
- The password length must be a positive integer.
- Passwords are generated using Python's `random` module. For cryptographically secure passwords, consider replacing `random.choice` with `secrets.choice` from the `secrets` module.

## File Structure

```
password_generator.py   # Main application file
README.md               # This file
```

## Security Recommendation

The current implementation uses the `random` module, which is suitable for general use. For security-sensitive applications (e.g., generating passwords for accounts or credentials), update the generation line as follows:

```python
import secrets
password = ''.join(secrets.choice(characters) for _ in range(length))
```

## License

This project is open-source and free to use.

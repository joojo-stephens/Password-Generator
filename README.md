# Password Generator

A simple, console-based Python application that generates a random password based on your desired length.

## Description

This script implements a “Password Generator”:

1. Imports the `string` module for predefined character sets:
   - `string.ascii_letters` (a–z, A–Z)  
   - `string.digits`       (0–9)  
   - `string.punctuation`  (e.g. `!@#$%^&*()…`)  

2. Defines `password_generator(length)`:
   - Builds a character pool by concatenating those three constants.  
   - Loops exactly `length` times, each iteration picking a random character with `random.choice(chars)` and appending it.  

3. In `main()`, prompts the user:
Please Enter The Desired length of your password? (eg. 7 or 19 ... )nverts the input to `int`, calls `password_generator()`, and prints: `Your password is <generated_password>`

No external dependencies beyond Python’s standard library.

## Features

- Customizable password length  
- Uses uppercase, lowercase, digits, and symbols  
- Quick and easy console I/O  

## Requirements

- Python 3.x  

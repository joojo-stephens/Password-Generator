
import random
import string

def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def main():
    feedback = int(input("Please Enter The Desired length of your password? (eg. 7 or 19 ... ) "))
    password = password_generator(feedback)
    print("Your password is", password)


if __name__ == "__main__":
    main()
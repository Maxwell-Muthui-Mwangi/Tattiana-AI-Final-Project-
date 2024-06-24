import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1"
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def command_line_password_generator():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Error: Password length must be at least 1")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    command_line_password_generator()

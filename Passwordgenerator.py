import random
import string

def generate_password(length):
    # Define characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()

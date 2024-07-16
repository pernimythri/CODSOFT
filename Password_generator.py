import random
import string

class PasswordGenerator:
    def __init__(self):
        self.capital_letters = string.ascii_uppercase
        self.small_letters = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    def generate_password(self, length):
        if length < 4:
            print("Password length should be at least 4 characters.")
            return None
        
    
        password = [
            random.choice(self.capital_letters),
            random.choice(self.small_letters),
            random.choice(self.digits),
            random.choice(self.symbols)
        ]
        
    
        all_characters = self.capital_letters + self.small_letters + self.digits + self.symbols
        password += random.choices(all_characters, k=length-4)
        
        random.shuffle(password)
        
        
        password = ''.join(password)
        return password

if __name__ == "__main__":
    generator = PasswordGenerator()
    
    try:
        length = int(input("Enter the desired password length: "))
        password = generator.generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

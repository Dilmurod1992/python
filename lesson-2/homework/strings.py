from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

current_year = datetime.now().year

age = current_year - birth_year

print(f"Hello, {name}! You are {age} years old.")




txt = 'LMaasleitbtui'

car_brands = [
    'Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Jeep', 'Kia', 'Mazda',
    'Mercedes', 'Nissan', 'Malibu', 'Peugeot', 'Renault', 'Skoda', 'Subaru',
    'Suzuki', 'Toyota', 'Volkswagen', 'Volvo', 'Tesla', 'Chevrolet',
    'Lexus', 'Jaguar', 'Fiat'
]

txt_lower = txt.lower()

found_brands = []
for brand in car_brands:
    if brand.lower() in txt_lower:
        found_brands.append(brand)

if found_brands:
    print("Car brands found:", found_brands)
else:
    print("No car brands found in the text.")





txt = 'MsaatmiazD'

car_brands = [
    'Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Jeep', 'Kia', 'Mazda',
    'Mercedes', 'Nissan', 'Peugeot', 'Renault', 'Skoda', 'Subaru',
    'Suzuki', 'Toyota', 'Volkswagen', 'Volvo', 'Tesla', 'Chevrolet',
    'Lexus', 'Jaguar', 'Fiat'
]

import re

txt_lower = txt.lower()

found_exact = [brand for brand in car_brands if brand.lower() in txt_lower]

def letters_in_order(brand, text):
    pattern = '.*'.join(brand.lower())  
    return re.search(pattern, text)

found_order = [brand for brand in car_brands if letters_in_order(brand, txt_lower)]

found = list(set(found_exact + found_order))

print("Car brands found:", found if found else "None found")




import re

txt = "I'am John. I am from London"

match = re.search(r"\bI(?:'| a)?m from ([A-Za-z\s]+)", txt)

if match:
    residence = match.group(1).strip()
    print("Residence area:", residence)
else:
    print("No residence area found.")




user_input = input("Istalgan so'zni kiriting: ")

reversed_string = user_input[::-1]

print("Reversed string:", reversed_string)




user_input = input("Istalgan so'zni kiriting: ")

vowels = "aeiouAEIOU"

vowel_count = 0

for char in user_input:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)





numbers_input = input("Raqamlarni bo'sh joy bilan ajratib kiriting: ")

numbers = list(map(float, numbers_input.split()))

max_value = max(numbers)

print("Maximum value:", max_value)





word = input("So'z kiriting: ")

word_lower = word.lower()

if word_lower == word_lower[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")





email = input("Email adresingizni kiriting: ")

if "@" in email:
    domain = email.split("@")[1]
    print("Domain:", domain)
else:
    print("Noto'g'ri email adres. '@' belgisi topilmadi.")





import random
import string

password_length = int(input("Parol uzunligi nechta belgidan iborat bo'lsin: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(password_length))

print("Siz uchun parol:", password)

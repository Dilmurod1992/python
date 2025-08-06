from datetime import date

yil = int(input("Tug'ilgan yilingizni kiriting: "))
oy = int(input("Qaysi oyda tug'ilgansiz (1-12): "))
kun = int(input("Tug'ilgan kuningizni kiriting: "))

today = date.today()
birthdate = date(yil, oy, kun)

age_days = (today - birthdate).days

yil = age_days // 365
oy = (age_days % 365) // 30
kun = (age_days % 365) % 30

print(f"Siz {yil} yosh, {oy} oylik va {kun} kunliksiz.")





from datetime import datetime, date


current_date = date.today()
my_next_birthday = date(year=2025, month=11, day=9)

days_left = my_next_birthday - current_date

print(f"{days_left} left till your birthday.")



from datetime import datetime, timedelta


current_input = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_time = datetime.strptime(current_input, "%Y-%m-%d %H:%M")


hours = int(input("Enter meeting duration - hours: "))
minutes = int(input("Enter meeting duration - minutes: "))


duration = timedelta(hours=hours, minutes=minutes)
end_time = current_time + duration


print("The meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))





from datetime import datetime
import pytz


local = datetime.now()

print("Local: ", local.strftime("%d-%m-%y, %H:%M:%S"))



tz_NY = pytz.timezone("America/New_York")

datetime_NY = datetime.now(tz_NY)

print("New York: ", datetime_NY.strftime('%d-%m-%Y, %H:%M'))


tz_Ln = pytz.timezone("Europe/London")

datetime_Ln = datetime.now(tz_Ln)

print("London: ", datetime_Ln.strftime('%d-%m-%Y, %H:%M'))




from datetime import datetime
import time


target_input = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")

try:
    target_time = datetime.strptime(target_input, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        remaining = target_time - now

        if remaining.total_seconds() <= 0:
            print("Countdown finished!")
            break

    
        print("\rTime remaining:", str(remaining).split('.')[0], end='')
        time.sleep(1)

except ValueError:
    print("Invalid format. Please use YYYY-MM-DD HH:MM:SS")





import re

pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

email = input("Enter an email address to validate: ")


if re.match(pattern, email):
    print("✅ Valid email address.")
else:
    print("❌ Invalid email address.")



import re

text = "My name is Dilmurod. My phone number is 123-456-7890"

print(re.findall('[0-9]{3}-[0-9]{3}-[0-9]{4}', text))




def check_password_strength(password):
    if len(password) < 8:
        return "❌ Password must be at least 8 characters long."

    if not any(char.isupper() for char in password):
        return "❌ Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "❌ Password must contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return "❌ Password must contain at least one digit."

    return "✅ Password is strong!"


password = input("Enter a password to check: ")
result = check_password_strength(password)
print(result)





import re


sample_text = """
Python is a powerful programming language. Python is used in web development, data science, automation, and more.
Learning Python can be fun and rewarding. The Python community is large and supportive.
"""

search_word = input("Enter a word to find: ")

matches = list(re.finditer(rf'\b{re.escape(search_word)}\b', sample_text, re.IGNORECASE))

if matches:
    print(f"\nFound {len(matches)} occurrence(s) of '{search_word}':")
    for i, match in enumerate(matches, 1):
        print(f"{i}. Position: {match.start()} — '{match.group()}'")
else:
    print(f"\nThe word '{search_word}' was not found in the text.")





import re


text = input("Enter text with possible dates: ")


date_pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})\b'


dates = re.findall(date_pattern, text)


if dates:
    print("\nDates found in the text:")
    for date in dates:
        print("-", date)
else:
    print("\nNo dates found in the text.")

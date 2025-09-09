1. Age Calculator
from datetime import datetime

def age_calculator():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (birthdate.replace(year=today.year, month=today.month) - birthdate.replace(year=today.year, month=today.month-1)).days
    if months < 0:
        years -= 1
        months += 12

    print(f"Your age is {years} years, {months} months, and {days} days.")

2. Days Until Next Birthday
def days_until_next_birthday():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()

    this_year_birthday = birthdate.replace(year=today.year)
    if this_year_birthday < today:
        this_year_birthday = this_year_birthday.replace(year=today.year + 1)

    days_left = (this_year_birthday - today).days
    print(f"Days until your next birthday: {days_left}")

3. Meeting Scheduler
from datetime import timedelta

def meeting_scheduler():
    current_dt_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    current_dt = datetime.strptime(current_dt_str, "%Y-%m-%d %H:%M")

    duration_hours = int(input("Enter meeting duration hours: "))
    duration_minutes = int(input("Enter meeting duration minutes: "))

    meeting_end = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)
    print(f"The meeting will end at: {meeting_end.strftime('%Y-%m-%d %H:%M')}")

4. Timezone Converter
from datetime import datetime
import pytz

def timezone_converter():
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz_str = input("Enter your current timezone (e.g., US/Eastern): ")
    to_tz_str = input("Enter the timezone to convert to (e.g., Asia/Tashkent): ")

    naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)

    localized_dt = from_tz.localize(naive_dt)
    converted_dt = localized_dt.astimezone(to_tz)

    print(f"Converted time: {converted_dt.strftime('%Y-%m-%d %H:%M %Z%z')}")


Note: You need to install pytz if not installed:

pip install pytz

5. Countdown Timer
import time

def countdown_timer():
    future_dt_str = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
    future_dt = datetime.strptime(future_dt_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        if now >= future_dt:
            print("Countdown finished!")
            break

        remaining = future_dt - now
        print(f"Time remaining: {remaining}", end='\r')
        time.sleep(1)

6. Email Validator
import re

def email_validator():
    email = input("Enter an email address: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

7. Phone Number Formatter
def phone_formatter():
    phone = input("Enter a 10-digit phone number: ")
    digits = ''.join(filter(str.isdigit, phone))

    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print(f"Formatted phone number: {formatted}")
    else:
        print("Invalid phone number length.")

8. Password Strength Checker
def password_strength_checker():
    import string

    password = input("Enter a password: ")
    length_ok = len(password) >= 8
    upper_ok = any(c.isupper() for c in password)
    lower_ok = any(c.islower() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_ok = any(c in string.punctuation for c in password)

    if all([length_ok, upper_ok, lower_ok, digit_ok, special_ok]):
        print("Strong password.")
    else:
        print("Weak password. Ensure it has at least 8 characters, upper and lower case letters, digits, and special symbols.")

9. Word Finder
def word_finder():
    sample_text = """
    This is a sample text. This text is for testing the word finder program.
    The word 'text' appears multiple times in this text.
    """

    word = input("Enter the word to find: ").lower()
    occurrences = []

    lines = sample_text.split('\n')
    for i, line in enumerate(lines, start=1):
        if word in line.lower():
            occurrences.append((i, line.strip()))

    if occurrences:
        print(f"Occurrences of '{word}':")
        for line_no, line_text in occurrences:
            print(f"Line {line_no}: {line_text}")
    else:
        print(f"'{word}' not found in the sample text.")

10. Date Extractor
import re

def date_extractor():
    text = input("Enter text: ")

    # Simple date regex for formats like YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY, etc.
    date_pattern = r'\b(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})\b'
    dates = re.findall(date_pattern, text)

    if dates:
        print("Dates found in the text:")
        for date in dates:
            print(date)
    else:
        print("No dates found.")

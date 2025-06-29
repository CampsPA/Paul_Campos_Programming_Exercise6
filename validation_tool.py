"""
This program validates user input for U.S. phone numbers, Social Security Numbers (SSNs),
and ZIP codes using regular expressions. It prompts the user to enter each value and
then checks if the format is valid based on commonly accepted patterns.

Supported formats:
- Phone Number: 123-456-7890, (123) 456-7890, 1234567890
- SSN: 123-45-6789
- ZIP Code: 12345 or 12345-6789
"""
import re

# Create a function to validate phone numbers
def validate_phone_number(phone):
     pat = r'^(\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$'
     phone_numbers = re.fullmatch(pat, phone)
     return bool(phone_numbers)

# Create a function to validate SSN's
def validate_ssn(ssn):
     pat = r'^\d{3}-\d{2}-\d{4}$'
     social_security = re.fullmatch(pat, ssn)
     return bool(social_security)

# Create a function to validate zipcodes
def validate_zip_codes(zipcode):
     pat = r'^\d{5}(-\d{4})?$'
     zip_code = re.fullmatch(pat, zipcode)
     return bool(zip_code)

# Create a main function, get user inputs and print the validations.
def main():
     phone_numbers = input('Enter the phone number: ')
     social_security = input('Enter the SSN: ')
     zip_code = input('Enter the zip code: ')

     print("\nValidation Results:")
     print(f"Phone Number Valid: {'Yes' if validate_phone_number(phone_numbers) else 'No'}")
     print(f"SSN Valid: {'Yes' if validate_ssn(social_security) else 'No'}")
     print(f"ZIP Code Valid: {'Yes' if validate_zip_codes(zip_code) else 'No'}")


if __name__ == '__main__':
    main()

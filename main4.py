import re


def normalize_phone(phone_number):
    normalized_number = re.sub(r'\D', '', phone_number)
    if not normalized_number.startswith('+'):
        if normalized_number.startswith('380'):
            normalized_number = '+' + normalized_number
        else:
            normalized_number = '+38' + normalized_number
    
    return normalized_number

print(normalize_phone)

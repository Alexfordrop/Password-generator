import string, random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def get_password_length():
    length = input('Какой длины нужен пароль: ')
    return int(length)

def password_length(cbl, length = 8):
    
    printable = fetch_string_constant(cbl)

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password
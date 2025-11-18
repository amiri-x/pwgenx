from curses.ascii import isdigit
import string
import secrets  

LETTERS = string.ascii_letters
DIGITS = string.digits
SAFE_SYMBOLS = "!@#$%^&*"

ALPHA_NUM = LETTERS + DIGITS
CHARS = LETTERS + DIGITS + SAFE_SYMBOLS

def generate(len: int, no_symbols=False, only_digits=False) -> str:
    """
    Generates a scure random password.

    Args:
        len (int): Lenght of the password 
        use_symbols (bool): Include symbols if true 
        only_digits (bool): Include only digits if true
    return:
        (str): password 

    Note: len should be in: 4 <= len <= 128
    """

    try:
        int(len)
    except:    
        raise TypeError(f"Invalid type for int length: {len} ")
    
    if len < 4  or len > 128 or not len.is_integer(): 
        raise ValueError(f"Invalid value length for int in range 4-128: {len} ")

    # ensure existing at least one of each type
    password_all_chars=[
        secrets.choice(LETTERS), 
        secrets.choice(DIGITS), 
        secrets.choice(SAFE_SYMBOLS) 
    ]
    password_alpha_num=[
        secrets.choice(LETTERS), 
        secrets.choice(DIGITS)
    ]

    if only_digits:
        return "".join(secrets.choice(DIGITS) for _ in range(len))
    
    if no_symbols: 
        password_alpha_num +=[secrets.choice(ALPHA_NUM) for _ in range(len-2)]
        secrets.SystemRandom().shuffle(password_alpha_num)
        return "".join(password_alpha_num)
    else: 
        password_all_chars +=[secrets.choice(CHARS) for _ in range(len-3)]
        secrets.SystemRandom().shuffle(password_alpha_num)
        return "".join(password_all_chars)
        
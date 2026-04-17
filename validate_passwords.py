def validate_passwords(passwords):


    len_check = all(len(password) > 7 for password in passwords)

    content_digit = any(any(c.isdigit() for c in password) for password in passwords)

    content_upper = any(any(c.isupper() for c in password) for password in passwords)

    no_space = all(' ' not in password for password in passwords)



    result = all([len_check, content_digit, content_upper, no_space])

    return result
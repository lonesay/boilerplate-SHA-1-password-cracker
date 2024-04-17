import hashlib


def getlines(path):
    result = []
    with open(path, 'r') as R:
        for line in R.readlines():
            result.append(line[:-1])
    return result


def crack_sha1_hash(hash, use_salts=False):
    passwords = getlines("top-10000-passwords.txt")
    if use_salts:
        salts = getlines("known-salts.txt")
        for salt in salts:
            for password in passwords:
                if hashlib.sha1((password + salt).encode('ascii')).hexdigest() == hash:
                    return password
                elif hashlib.sha1((salt + password).encode('ascii')).hexdigest() == hash:
                    return password
                elif hashlib.sha1((salt + password + salt).encode('ascii')).hexdigest() == hash:
                    return password
    else:
        for password in passwords:
            if hashlib.sha1(password.encode('ascii')).hexdigest() == hash:
                return password

    return "PASSWORD NOT IN DATABASE"


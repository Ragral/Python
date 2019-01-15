import hashlib

sha = hashlib.sha1(b'Hello Python').hexdigest()

print('Результат:',sha)

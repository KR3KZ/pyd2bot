from hashlib import md5

passz = "pass"
r = md5(passz.encode())
print(r.hexdigest())

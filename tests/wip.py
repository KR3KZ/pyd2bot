    

import hashlib


class ByteArray:
    
    def __init__(self, data:bytearray):
        self.data = data
    
    def readUTF(self):
        pass
    
    def __getitem__(self, b):
        return self.data.__getitem__(b)


ba = bytearray([1, 2, 3])
r = hashlib.md5(ba).hexdigest()
print(r)
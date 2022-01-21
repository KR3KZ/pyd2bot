from pyd2bot.utils.binaryIO import ByteArray
from pyd2bot.utils.crypto import IPad, ISymmetricKey, IVMode


class CBCMode(IVMode):
    
    def __init__(self, key:ISymmetricKey, padding:IPad = None):
        super(CBCMode, self).__init__(key, padding)
    
    def encrypt(self, src:ByteArray):
        j = 0
        self.padding.pad(src)
        vector:ByteArray = self.getIV4e()
        for i in range(0, len(src), self.blockSize):
            for j in range(self.blockSize):
                src[i + j] ^= vector[j]
            self.key.encrypt(src, i)
            vector.position = 0
            vector.writeBytes(src, i, self.blockSize)
        
    def decrypt(self, src:ByteArray): 
        j = 0
        vector:ByteArray = self.getIV4d()
        tmp:ByteArray = ByteArray()
        for i in range(0, len(src), self.blockSize):
            tmp.position = 0
            tmp.writeBytes(src, i, self.blockSize)
            self.key.decrypt(src, i)
            for j in range(self.blockSize):
                src[i + j] ^= vector[j]
            vector.position = 0
            vector.writeBytes(tmp, 0, self.blockSize)
        self.padding.unpad(src)
        
    def toString(self): 
        return self.key.toString() + "-cbc"
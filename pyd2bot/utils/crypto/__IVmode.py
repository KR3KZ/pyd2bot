from random import Random
from pyd2bot.utils.binaryIO.customDataWrapper import ByteArray
from pyd2bot.utils.crypto import IPad, ISymmetricKey, PKCS5


class IVMode:
    
    def __init__(self, key:ISymmetricKey, padding:IPad = None):
        self.key = key
        self.blockSize = key.getBlockSize()
        if padding == None:
            padding = PKCS5(self.blockSize)
        else:
            padding.setBlockSize(self.blockSize)
        
        self.padding = padding
        self.prng = Random()
        self.iv = ByteArray()
        self.lastIV = ByteArray()
    
    def getBlockSize(self) : 
        return self.key.getBlockSize
    
    def dispose(self): 
        i = 0
        if self.iv != None:
            for i in range(len(self.iv)):
                self.iv[i] = self.prng.getrandbits(8)
            self.iv.__init__()
            self.iv = None
        
        if self.lastIV != None:
            for i in range(len(self.iv)):
                self.lastIV[i] = self.prng.getrandbits(8)
            self.lastIV.__init__()
            self.lastIV = None
        
        self.key.dispose()
        self.key = None
        self.padding = None
        self.prng = None
    
    def setIV(self, value:ByteArray) : 
        self.iv = value
        self.lastIV.__init__()
        self.lastIV.writeBytes(self.iv)
    
    def getIV(self) -> ByteArray: 
        return self.lastIV
    
    def getIV4e(self) -> ByteArray: 
        vec:ByteArray = ByteArray()
        if self.iv:
            vec.writeBytes(self.iv)
        else:
            vec = self.prng.getrandbits(8 * self.blockSize)
        self.lastIV.__init__()
        self.lastIV.writeBytes(vec)
        return vec
    
    def getIV4d(self) -> ByteArray: 
        vec:ByteArray = ByteArray()
        if self.iv:
            vec.writeBytes(self.iv)
            return vec
        raise Exception("an IV must be set before calling decrypt()")

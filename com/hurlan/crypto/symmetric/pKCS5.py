

from com.ankamagames.jerakine.network.customDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.iPad import IPad


class PKCS5(IPad):
    
    blockSize:int
    
    def __init__(self, blockSize:int = 0):
        super().__init__()
        self.blockSize = blockSize
    
    def pad(self, a:ByteArray):
        c:int = self.blockSize - a.length % self.blockSize
        for i in range(c):
            a[a.length] = c
            
    def unpad(self, a:ByteArray) -> None:
        v:int = 0
        c:int = a.length % self.blockSize
        if c != 0:
            raise Exception("PKCS#5::unpad: ByteArray.length isn\'t a multiple of the blockSize");
        c = a[a.length - 1]
        for _ in range(c, 0, -1):
            v = a[a.length - 1]
            a.length-=1
            if c != v:
                raise Exception("PKCS#5:unpad: Invalid padding value. expected [" + c + "], found [" + v + "]");

    def setBlockSize(self, bs:int) -> None:
        self.blockSize = bs

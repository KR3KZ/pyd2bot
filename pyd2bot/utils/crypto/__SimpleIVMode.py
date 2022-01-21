
from pyd2bot.utils.binaryIO import ByteArray
from . import IMode, IVMode, ICipher
   
   
class SimpleIVMode(IMode, ICipher):
    
    def __init__(self, mode:IVMode):
        self.mode = mode
        self.cipher:ICipher = mode
        
    def getBlockSize(self) : 
        return self.mode.getBlockSize()
    
    def dispose(self):
        self.mode.dispose()
        self.mode = None
        self.cipher = None
    
    def encrypt(self, src:ByteArray):
        self.cipher.encrypt(src)
        tmp:ByteArray = ByteArray()
        tmp.writeBytes(self.mode.IV)
        tmp.writeBytes(src)
        src.position = 0
        src.writeBytes(tmp)
    
    def decrypt(self, src:ByteArray):
        tmp:ByteArray = ByteArray()
        tmp.writeBytes(src, 0, self.getBlockSize())
        self.mode.iv = tmp
        tmp = ByteArray()
        tmp.writeBytes(src, self.getBlockSize())
        self.cipher.decrypt(tmp)
        src.__init__()
        src.writeBytes(tmp)
    
    def toString(self):
        return "simple-" + self.cipher.toString()

from abc import ABC
from pyd2bot.utils.binaryIO import ByteArray


class ICipher(ABC):
    
    def getBlockSize(self) -> int:
        pass
    
    def encrypt(self, param1:ByteArray) -> None:
        pass 
    
    def decrypt(self, param1:ByteArray) -> None:
        pass 
    
    def dispose(self) -> None:
        pass 
    
    def toString(self) -> str:
        pass
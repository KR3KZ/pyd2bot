
from abc import ABC
from pyd2bot.utils.binaryIO.customDataWrapper import ByteArray;


class ISymmetricKey(ABC):
    
    def getBlockSize(self) -> int:
        pass 
    
    def encrypt(self, param1:ByteArray, param2:int = 0) -> None:
        pass
    
    def decrypt(self, param1:ByteArray, param2:int = 0) -> None: 
        pass
    
    def dispose() -> None:
        pass
    
    def toString() -> str:
        pass

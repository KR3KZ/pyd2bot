
from abc import ABC
from pyd2bot.utils.binaryIO.customDataWrapper import ByteArray;


class ISymmetricKey(ABC):
    
    def getBlockSize() -> int:
        pass 
    
    def encrypt(param1:ByteArray, param2:int = 0) -> None:
        pass
    
    def decrypt(param1:ByteArray, param2:int = 0) -> None: 
        pass
    
    def dispose() -> None:
        pass
    
    def toString() -> str:
        pass

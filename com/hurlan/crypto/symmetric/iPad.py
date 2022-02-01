from abc import ABC
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray;


class IPad(ABC):
    
    def pad(self, param1:ByteArray) -> None: 
        pass
    
    def unpad(self, param1:ByteArray) -> None:
        pass

    def setBlockSize(self, param1:int) -> None: 
        pass

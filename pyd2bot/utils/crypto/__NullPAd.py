from pyd2bot.utils.binaryIO import ByteArray
from pyd2bot.utils.crypto import IPad


class NullPad(IPad):
    
    def NullPad(self):
        super().__init__()
    
    def unpad(a:ByteArray) -> None:
        pass
    
    def pad(a:ByteArray) -> None:
        pass
    
    def setBlockSize(bs:int):
        pass

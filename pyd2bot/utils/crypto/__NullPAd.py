from pyd2bot.utils.binaryIO import ByteArray
from pyd2bot.utils.crypto import IPad


class NullPad(IPad):
    
    def NullPad(self):
        super().__init__()
    
    def unpad(self, a:ByteArray) -> None:
        pass
    
    def pad(self, a:ByteArray) -> None:
        pass
    
    def setBlockSize(self, bs:int):
        pass

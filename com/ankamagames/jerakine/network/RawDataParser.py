from types import FunctionType
from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.network.customDataWrapper import ByteArray


class RawDataParser:
      
   
   def parse(self, param1:ByteArray, param2:int, param3:int) -> INetworkMessage:
      pass
   
   def parseAsync(self, param1:ByteArray, param2:int, param3:int, param4:FunctionType) -> INetworkMessage:
      pass
   
   def getUnpackMode(self, param1:int) -> int:
      pass

import importlib
from com.ankamagames.jerakine.logger.Logger import Logger
import sys
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
import com.ankamagames.jerakine.network.NetworkMessageDataField as nmdf
from com.ankamagames.jerakine.network.ProtocolSpec import ProtocolSpec
logger = Logger(__name__)


class NetworkMessageClassDefinition:
   
   def __init__(self, className:str, raw:ByteArray) -> None:
      classSpec = ProtocolSpec.getClassSpecByName(className)
      self._parent = classSpec["parent"]
      self._fields = classSpec["fields"]
      self._boolfields = classSpec["boolfields"]
      self.raw = raw
   
   def deserialize(self) -> object:
      inst = {}

      if self._parent is not None:
         inst.update(NetworkMessageClassDefinition(self._parent, self.raw).deserialize(inst))
         
      for field, value in self.readBooleans(self._boolfields, self.raw).items():
         inst[field] = value

      for field in self._fields:
         attrib = field["name"]
         if field["optional"]:
            if not self.raw.readByte():
                continue
         value = nmdf.NetMsgDataField(field, self.raw).deserialize()
         inst[attrib] = value
      return inst

   def readBooleans(self, boolfields, raw: ByteArray):
      ans = {}
      bfields = iter(boolfields)
      for _ in range(0, len(boolfields), 8):
         bits = format(raw.readByte(), "08b")[::-1]
         for val, var in zip(bits, bfields):
               ans[var["name"]] = val == "1"
      return ans

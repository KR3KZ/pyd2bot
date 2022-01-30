import importlib
import logging
import sys
from com.ankamagames.jerakine.network.customDataWrapper import ByteArray
import pyd2bot.network.NetMsgDataField as nmdf
from pyd2bot.network.protocolSpec import ProtocolSpec
logger = logging.getLogger("bot")


class NetMsgClassDef:
   
   def __init__(self, className:str, raw:ByteArray) -> None:
      logger.debug("Getting spec for {}".format(className))
      classSpec = ProtocolSpec.getClassSpecByName(className)
      self._parent = classSpec["parent"]
      self._fields = classSpec["fields"]
      self._boolfields = classSpec["boolfields"]
      modulePath = classSpec["package"]
      try:
         clsModule = sys.modules[modulePath]
      except:
         clsModule = importlib.import_module(modulePath)
      self._cls = getattr(clsModule, classSpec["name"])
      self.raw = raw
   
   def deserialize(self, childInstance:object=None) -> object:
      if childInstance is None:
         inst = self._cls()
      else:
         inst = childInstance

      logger.debug("------------------ Deserializing {} STARTED-----------------".format(self._cls.__name__))

      if self._parent is not None:
         logger.debug("Class has parent {}".format(self._parent))
         inst = NetMsgClassDef(self._parent, self.raw).deserialize(inst)
         logger.debug("End of parent deserialization")
         logger.debug("BytesArray positon: {}".format(self.raw.position))
         
      for field, value in self.readBooleans(self._boolfields, self.raw).items():
         logger.debug("{} = {}".format(field, value))
         setattr(inst, field, value)

      for field in self._fields:
         attrib = field["name"]
         if field["optional"]:
            if not self.raw.readByte():
                continue
         logger.debug("deserializing field {}".format(attrib))
         try:
            value = nmdf.NetMsgDataField(field, self.raw).deserialize()
         except Exception as e:
            logger.debug(inst.__class__.__name__)
            logger.debug(self._fields)
            logger.error(exec_info=True)
            raise KeyboardInterrupt
         setattr(inst, attrib, value)
      logger.debug("------------------ Deserializing {} ENDED---------------------".format(self._cls.__name__))
      return inst

   def readBooleans(self, boolfields, raw: ByteArray):
      ans = {}
      bfields = iter(boolfields)
      for _ in range(0, len(boolfields), 8):
         bits = format(raw.readByte(), "08b")[::-1]
         for val, var in zip(bits, bfields):
               ans[var["name"]] = val == "1"
      return ans

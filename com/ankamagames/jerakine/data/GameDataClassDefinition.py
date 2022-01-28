import sys
from typing import Any
from dataReader.d2o import GameDataField
from pyd2bot.jerakine.data.IposInit import IPostInit
from com.ankamagames.jerakine.network.Binarystream import BinaryStream


class GameDataClassDefinition:
      
   _class:object
   _fields:list[GameDataField]
   
   def __init__(self, packageName:str, className:str):
      super().__init__()
      self._class = getattr(sys.modules[__name__], packageName + "." + className)
      self._fields = list[GameDataField]()
   
   @property
   def fields(self) -> list[GameDataField]:
      return self._fields
   
   def read(self, module:str, stream:BinaryStream) -> Any:
      field:GameDataField = None
      inst = self._class()
      for field in self._fields:
         inst[field.name] = field.readData(module,stream)
      if isinstance(inst, IPostInit):
         inst.postInit()
      return inst
   
   def addField(self, fieldName:str, stream:BinaryStream) -> None:
      field:GameDataField = GameDataField(fieldName)
      field.readType(stream)
      self._fields.append(field)

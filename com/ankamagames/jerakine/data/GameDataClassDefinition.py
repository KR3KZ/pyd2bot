from struct import pack
import sys
from typing import Any
from com.ankamagames.jerakine.data.IposInit import IPostInit
from .GameDataField import GameDataField
from pyd2bot.utils.binaryIO.binaryStream import BinaryStream


class GameDataClassDefinition:
      
   _class:object
   _fields:list[GameDataField]
   
   def __init__(self, packageName:bytes, className:bytes):
      super().__init__()
      packageName = packageName.decode('utf-8')
      className = className.decode('utf-8')
      self._fields = list()  
      moduleName = packageName + '.' + className[0].lower() + className[1:]    
      print(moduleName, className)
      __import__(moduleName, fromlist=[className])
      module = sys.modules[moduleName]
      self._class = getattr(module, className)
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
   
   def addField(self, fieleName:str, stream:BinaryStream) -> None:
      field:GameDataField = GameDataField(fieleName)
      field.readType(stream)
      self._fields.append(field)

import importlib
import sys
from struct import pack
from typing import Any

import com.ankamagames.jerakine.data.gameDataField as gdf
from com.ankamagames.jerakine.data.iposInit import IPostInit
from pyd2bot.utils.binaryIO.binaryStream import BinaryStream


class GameDataClassDefinition:
      
   _class:object
   _fields:list[gdf.GameDataField]
   
   def __init__(self, packageName:bytes, className:bytes):
      super().__init__()
      packageName = packageName.decode('utf-8')
      className:str = className.decode('utf-8')
      self._fields = list()  
      moduleName = packageName + '.' + className[0].lower() + className[1:]
      print(moduleName)  
      module = importlib.import_module(moduleName)
      self._class = getattr(module, className)
      self._fields = list[gdf.GameDataField]()
   
   @property
   def fields(self) -> list[gdf.GameDataField]:
      return self._fields
   
   def read(self, module:str, stream:BinaryStream) -> Any:
      field = None
      inst = self._class()
      for field in self._fields:
         setattr(inst, field.name.decode('utf-8'), field.readData(module, stream))
      if isinstance(inst, IPostInit):
         inst.postInit()
      return inst
   
   def addField(self, fileName:str, stream:BinaryStream) -> None:
      field = gdf.GameDataField(fileName)
      field.readType(stream)
      self._fields.append(field)

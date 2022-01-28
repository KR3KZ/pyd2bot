import importlib
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
   from com.ankamagames.jerakine.data.moduleReader import ModuleReader
from com.ankamagames.jerakine.data.iposInit import IPostInit
from pyd2bot.utils.binaryIO.binaryStream import BinaryStream
from com.ankamagames.jerakine.data.gameDataField import GameDataField

class GameDataClassDefinition:
   
   def __init__(self, packageName:str, className:str, moduleReader:'ModuleReader') -> None:
      self._fields = list()  
      moduleName = packageName + '.' + className[0].lower() + className[1:]
      module = importlib.import_module(moduleName)
      self._moduleName = moduleName
      self._name = className
      self._class = getattr(module, className)
      self._fields = list[GameDataField]()
      self.moduleReader = moduleReader
   
   @property
   def fields(self) -> list[GameDataField]:
      return self._fields
   
   def getInstance(self, stream:BinaryStream) -> Any:
      inst = self._class()
      for field in self._fields:
         attrib = field.name
         value = field.readData(stream)
         setattr(inst, attrib, value)
      if isinstance(inst, IPostInit):
         inst.postInit()
      return inst
   
   def addField(self, fileName:str, stream:BinaryStream) -> None:
      field = GameDataField(fileName, self.moduleReader)
      field.readType(stream)
      self._fields.append(field)

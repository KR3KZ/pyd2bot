import logging
import re
from types import FunctionType
from typing import Any
from com.ankamagames.jerakine.data.gameDataFileAccessor import GameDataFileAccessor as fm
from com.ankamagames.jerakine.enum.gameDataTypeEnum import GameDataTypeEnum
from pyd2bot.utils.binaryIO.binaryStream import BinaryStream
logger = logging.getLogger("bot")

class GameDataField:
   
   NULL_IDENTIFIER:int = -1431655766
   _classesByName:dict = dict()
   name:bytes = None
   readData:FunctionType = None
   _innerReadMethods = list[FunctionType]()
   _innerTypeNames = list[str]()
   

   def __init__(self, fieldName:str):
      super().__init__()
      self.name = fieldName
   
   def getobjectByName(self, className:str) -> object:
      c:object = self._classesByName[className]
      if c == None:
         c = globals()[className]
         self._classesByName[className] = c
      return c
   
   def readType(self, stream:BinaryStream) -> None:
      type:int = stream.readInt()
      self.readData = self.getReadMethod(type,stream)
   
   def getReadMethod(self, type:int, stream:BinaryStream) -> FunctionType:
      if type == GameDataTypeEnum.INT:
         return self.readInteger

      elif type == GameDataTypeEnum.BOOLEAN:
         return self.readbool

      elif type == GameDataTypeEnum.STRING:
         return self.readstr

      elif type == GameDataTypeEnum.NUMBER:
         return self.readfloat

      elif type == GameDataTypeEnum.I18N:
         return self.readI18n

      elif type == GameDataTypeEnum.UINT:
         return self.readUnsignedInteger

      elif type == GameDataTypeEnum.VECTOR:
         if not self._innerReadMethods:
            self._innerReadMethods = list[FunctionType]()
            self._innerTypeNames = list[str]()
         self._innerTypeNames.append(stream.readUTF())
         self._innerReadMethods.insert(0, self.getReadMethod(stream.readInt(), stream))
         return self.readVector

      else:
         if type > 0:
            return self.readobject
         raise Exception("Unknown type \'" + type + "\'.")
   
   def readVector(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      len:int = stream.readInt()
      vectorTypeName:str = self._innerTypeNames[innerIndex]
      m = re.fullmatch(r"Vector\.<(?P<module>\S+)::(?P<classname>\S+)>", vectorTypeName.decode("utf-8"))
      if m:
         arrayElementModule = m.group("module")
         arrayElementClassName = m.group("classname")
         content = list[arrayElementClassName]([True] * len)
      else:
         raise Exception("Unknown vector type \'" + vectorTypeName + "\'.")
      for i in range(len):
         content.append(self._innerReadMethods[innerIndex](moduleName, stream, innerIndex + 1))
      return content
   
   def readobject(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      classIdentifier:int = stream.readInt()
      if classIdentifier == self.NULL_IDENTIFIER:
         return None
      classDefinition = fm.getInstance().getClassDefinition(moduleName, classIdentifier)
      return classDefinition.read(moduleName, stream)
   
   def readInteger(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      return stream.readInt()
   
   def readbool(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      return stream.readbool()
   
   def readstr(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      result = stream.readUTF()
      if result == "None":
         result = None
      return result
   
   def readfloat(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      return stream.readDouble()
   
   def readI18n(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      return stream.readInt()
   
   def readUnsignedInteger(self, moduleName:str, stream:BinaryStream, innerIndex:int = 0) -> Any:
      return stream.readUnsignedInt()

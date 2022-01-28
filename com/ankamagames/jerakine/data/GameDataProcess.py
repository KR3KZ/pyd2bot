from ast import FunctionType
from com.ankamagames.jerakine.data.i18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.enum.gameDataTypeEnum import GameDataTypeEnum
from com.ankamagames.jerakine.data.binaryStream import BinaryStream


class GameDataProcess:

   def __init__(self, stream:BinaryStream):
      self._stream = stream
      self._sort_index = dict()
      self._queryable_field = list()
      self._search_field_index = dict()
      self._search_field_type = dict()
      self._search_field_count = dict()
      
      self._queryableField = list()
      self._searchFieldType = dict()
      self.parseStream()

   def parseStream(self):
      length = self._stream.readInt()
      off = self._stream.position + length + 4
      while length:
         available = self._stream.remaining()
         string = self._stream.readUTF()
         self._queryable_field.append(string)
         self._search_field_index[string] = self._stream.readInt() + off
         self._search_field_type[string] = self._stream.readInt()
         self._search_field_count[string] = self._stream.readInt()
         length = length - (available - self._stream.remaining())

   def getQueryableField(self) -> list[str]:
      return self._queryableField
   
   def getFieldType(self, fieldName:str) -> int:
      return self._searchFieldType[fieldName]
   
   def query(self, fieldName:str, match:FunctionType) -> list[int]:
      result = list[int]()
      if not self._searchFieldIndex[fieldName]:
         return None
      type = self._searchFieldType[fieldName]
      readFct = self.getReadFunctionType(type)
      itemCount = self._searchFieldCount[fieldName]
      self._stream.position(self._searchFieldIndex[fieldName])
      if readFct == None:
         return None
      for i in range(itemCount):
         if match(readFct()):
            idsCount = self._stream.readInt() * 0.25
            for j in range(idsCount):
               result.append(self._stream.readInt())
         else:
            self._stream.position(self._stream.readInt() + self._stream.position())
      return result
   
   def queryEquals(self, fieldName:str, value) -> list[int]:
      result:list[int] = list[int]()
      if not self._searchFieldIndex[fieldName]:
         return None
      iterable = value not in [int, float, str, bool or value == None]
      if iterable and len(value) == 0:
         return result
      if not iterable:
         value = [value]
      itemCount:int = self._searchFieldCount[fieldName]
      self._stream.position(self._searchFieldIndex[fieldName])
      type:int = self._searchFieldType[fieldName]
      readFct:FunctionType = self.getReadFunctionType(type)
      if readFct == None:
         return None
      valueIndex:int = 0
      value.sort()
      currentValue = value[0]
      for i in range(itemCount):
         readValue = readFct()
         while readValue > currentValue:
            valueIndex += 1
            if valueIndex == len(value):
               return result
            currentValue = value[valueIndex]
         if readValue == currentValue:
            idsCount = self._stream.readInt() * 0.25
            for j in range(idsCount):
               result.append(self._stream.readInt())
            valueIndex += 1
            if valueIndex == len(value):
               return result
            currentValue = value[valueIndex]
         else:
            self._stream.position(self._stream.readInt() + self._stream.position())
      return result
   
   def sort(self, fieldNames, ids:list[int], ascending = True) -> list[int]:
      ids.sort(self.getSortFunctionType(fieldNames,ascending))
      return ids
   
   def getSortFunctionType(self, fieldNames, ascending) -> FunctionType:
      sortWay:list[float] = None
      indexes:list[dict] = None
      maxFieldIndex:int = 0
      fieldName:str = None
      if fieldNames is str:
         fieldNames = [fieldNames]
      if ascending is bool:
         ascending = [ascending]
      sortWay = list[float]()
      indexes = list[dict]()
      for i in range(0, len(fieldNames), 1):
         fieldName = fieldNames[i]
         if self._searchFieldType[fieldName] == GameDataTypeEnum.I18N:
            self.buildI18nSortIndex(fieldName)
         else:
            self.buildSortIndex(fieldName)
         if len(ascending) < len(fieldNames):
            ascending.append(True)
         sortWay.append(1 if not ascending[i] else -1)
         indexes.append(self._sortIndex[fieldName])
      maxFieldIndex = len(fieldNames)
      def sortKey(t1:int, t2:int) ->float:
         for fieldIndex in range(maxFieldIndex):
            if indexes[fieldIndex][t1] < indexes[fieldIndex][t2]:
               return -sortWay[fieldIndex]
            if indexes[fieldIndex][t1] > indexes[fieldIndex][t2]:
               return sortWay[fieldIndex]
         return 0
      return sortKey
   
   def buildSortIndex(self, fieldName:str) -> None:
      if self._sortIndex[fieldName] or not self._searchFieldIndex[fieldName]:
         return
      itemCount:int = self._searchFieldCount[fieldName]
      self._stream.position(self._searchFieldIndex[fieldName])
      ref:dict = dict()
      self._sortIndex[fieldName] = ref
      type:int = self._searchFieldType[fieldName]
      readFct:FunctionType = self.getReadFunctionType(type)
      if readFct == None:
         return
      for i in range(itemCount):
         v = readFct()
         idsCount = self._stream.readInt() * 0.25
         for j in range(idsCount):
            ref[self._stream.readInt()] = v
   
   def buildI18nSortIndex(self, fieldName:str) -> None:
      key:int = 0
      idsCount:float = None
      i18nOrder:int = 0
      j:int = 0
      if self._sortIndex[fieldName] or not self._searchFieldIndex[fieldName]:
         return
      itemCount:int = self._searchFieldCount[fieldName]
      self._stream.position(self._searchFieldIndex[fieldName])
      ref:dict = dict()
      self._sortIndex[fieldName] = ref
      for i in range(itemCount):
         key = self._stream.readInt()
         idsCount = self._stream.readInt() * 0.25
         if idsCount:
            i18nOrder = I18nFileAccessor.getInstance().getOrderIndex(key)
            for j in range(idsCount):
               ref[self._stream.readInt()] = i18nOrder
   
   def readI18n(self) -> str:
      return I18nFileAccessor.getInstance().getUnDiacriticalText(self._currentStream.readInt())
   
   def getReadFunctionType(self, type:int) -> FunctionType:
      if type == GameDataTypeEnum.INT:
            readFct = self._stream.readInt
      elif type == GameDataTypeEnum.BOOLEAN:
            readFct = self._stream.readbool
      elif type == GameDataTypeEnum.STRING:
            readFct = self._stream.readUTF
      elif type ==  GameDataTypeEnum.NUMBER:
            readFct = self._stream.readDouble
      elif GameDataTypeEnum.I18N:
         I18nFileAccessor.getInstance().useDirectBuffer(True)
         readFct = self.readI18n
         if not isinstance(self._stream, BinaryStream):
            directBuffer = BinaryStream()
            # FIXME: Somethis is wrong here
            self._stream.position(0)
            self._stream.readBytes(directBuffer)
            directBuffer.position(0)
            self._stream = directBuffer
            self._currentStream = self._stream
      elif GameDataTypeEnum.UINT:
         readFct = self._stream.readUnsignedInt
      return readFct
   


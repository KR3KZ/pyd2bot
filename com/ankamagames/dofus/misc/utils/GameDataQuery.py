from types import FunctionType
from typing import Any
from com.ankamagames.dofus.misc.lists.GameDataList import GameDataList
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.GameDataField import GameDataField
from com.ankamagames.jerakine.data.GameDataFileAccessor import GameDataFileAccessor
from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.enum.GameDataTypeEnum import GameDataTypeEnum
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.misc.StringUtils import StringUtils
logger = Logger(__name__)


class GameDataQuery():
   
   def __init__(self):
      super().__init__()
   
   def getQueryableFields(self, target:object) -> list[str]:
      target = self.checkPackage(target)
      return GameDataFileAccessor().getDataProcessor(target["MODULE"]).getQueryableField()
   
   def union(self, *idsVectors) -> list[int]:
      result:list[int] = list[int]()
      added:dict = dict()
      for idVector in idsVectors:
         if idVector != None:
            for id in idVector:
               if not added.get(id):
                  result.append(id)
                  added[id] = True
      return result
   
   def intersection(self, *idsVectors) -> list[int]:
      id:int = 0
      ind:int = 0
      newMatch:dict = None
      i:int = 0
      result:list[int] = list[int]()
      ids:list[int] = idsVectors[i]
      match:dict = dict()
      for ind in range(len(idsVectors[0])):
         match[idsVectors[0][ind]] = idsVectors[0][ind]
      for i in range(len(idsVectors)):
         newMatch = dict()
         for ind in range(len(idsVectors[i])):
            id = idsVectors[i][ind]
            if match[id]:
               newMatch[id] = id
         match = newMatch
      for id in match:
         result.append(id)
      return result
   
   def queryEquals(self, target:object, fieldName:str, value) -> list[int]:
      target = self.checkPackage(target)
      fieldName = self.checkField(target,fieldName)
      if not fieldName:
         return list[int]()
      result:list[int] = GameDataFileAccessor().getDataProcessor(target["MODULE"]).queryEquals(fieldName,value)
      iterable = not isinstance(value, (int, float, str, bool)) and value is not None
      if iterable:
         return self.union(result)
      return result
   
   def querystr(self, target:object, fieldName:str, value:str) -> list[int]:
      target = self.checkPackage(target)
      fieldName = self.checkField(target,fieldName)
      if not fieldName:
         return list[int]()
      if not value:
         raise self.ArgumentError("value arg cannot be None")
      return GameDataFileAccessor().getDataProcessor(target["MODULE"]).query(fieldName, self.getMatchStringFct(StringUtils.noAccent(value).toLowerCase()))
   
   def queryGreaterThan(self, target:object, fieldName:str, value) -> list[int]:
      target = self.checkPackage(target)
      fieldName = self.checkField(target,fieldName)
      if not fieldName:
         return list[int]()
      return GameDataFileAccessor().getDataProcessor(target["MODULE"]).query(fieldName, self.getGreaterThanFct(value))
   
   def querySmallerThan(self, target:object, fieldName:str, value) -> list[int]:
      target = self.checkPackage(target)
      fieldName = self.checkField(target,fieldName)
      if not fieldName:
         return list[int]()
      return GameDataFileAccessor().getDataProcessor(target["MODULE"]).query(fieldName, self.getSmallerThanFct(value))
   
   def returnInstance(self, target:object, ids:list[int]) -> list[object]:
      instance = None
      target = self.checkPackage(target)
      result:list[object] = list[object]()
      module:str = target["MODULE"]
      for i in range(len(ids)):
         instance = GameData.getobject(module,ids[i])
         if instance != None:
            result.append(instance)
      return result
   
   def sort(self, target:object, ids:list[int], fieldNames, ascending = True) -> list[int]:
      cleanedFieldNames:list[str] = None
      i:int = 0
      field:str = None
      target = self.checkPackage(target)
      if not isinstance(fieldNames, str):
         cleanedFieldNames = list[str]()
         for i in range(len(fieldNames)):
            field = self.checkField(target,fieldNames[i])
            if field:
               cleanedFieldNames.append(field)
         fieldNames = cleanedFieldNames
      else:
         fieldNames = self.checkField(target,fieldNames)
      if not fieldNames or len(fieldNames) == 0:
         return list[int]()
      return GameDataFileAccessor().getDataProcessor(target["MODULE"]).sort(fieldNames,ids,ascending)
   
   def sortI18n(self, datas, fields, ascending) -> Any:
      datas.sort(self.getSortFunction(datas,fields,ascending))
      return datas
   
   def getSortFunction(self, datas, fieldNames, ascending) -> FunctionType:
      sortWay:list[float] = None
      indexes:list[dict] = None
      maxFieldIndex:int = 0
      fieldName:str = None
      fieldIndex:dict = None
      data = None
      if isinstance(fieldNames, str):
         fieldNames = [fieldNames]
      if ascending is bool:
         ascending = [ascending]
      sortWay = list[float]()
      indexes = list[dict]()
      for i in range(len(fieldNames)):
         fieldName = fieldNames[i]
         fieldIndex = dict()
         for data in datas:
            fieldIndex[data[fieldName]] = I18nFileAccessor().getOrderIndex(data[fieldName])
         if len(ascending) < len(fieldNames):
            ascending.append(True)
         sortWay.append(1 if not ascending[i] else -1)
         indexes.append(fieldIndex)
      maxFieldIndex = len(fieldNames)
      def function(t1, t2) -> float:
         for fieldIndex in range(maxFieldIndex):
            if indexes[fieldIndex][t1[fieldNames[fieldIndex]]] < indexes[fieldIndex][t2[fieldNames[fieldIndex]]]:
               return -sortWay[fieldIndex]
            if indexes[fieldIndex][t1[fieldNames[fieldIndex]]] > indexes[fieldIndex][t2[fieldNames[fieldIndex]]]:
               return sortWay[fieldIndex]
         return 0
      return function
   
   def getMatchStringFct(self, pattern:str) -> FunctionType:
      return lambda s: StringUtils.noAccent(str).toLowerCase().find(pattern) != -1 if s else False
   
   def getGreaterThanFct(self, cmpValue) -> FunctionType:
      return lambda v: v > cmpValue
   
   def getSmallerThanFct(self, cmpValue) -> FunctionType:
      return lambda v: v < cmpValue
   
   def checkField(self, target:object, name:str) -> str:
      module = getattr(target, "MODULE")
      fields:list[str] = GameDataFileAccessor().getDataProcessor(module).getQueryableField()
      if fields.find(name) == -1:
         if fields.find(name + "Id") == -1 or GameDataFileAccessor().getDataProcessor(module).getFieldType(name + "Id") != GameDataTypeEnum.I18N:
            logger.error("Field " + name + " not found in " + target)
            return None
         name += "Id"
      return name
   
   def checkPackage(self, target:object) -> object:
      tmp:list = target.__class__.__name__
      packageName:str = tmp
      if packageName == "d2data":
         className = tmp.split(".")[-1]
         for gameDataobject in GameDataList.CLASSES:
            gameDataobjectName = gameDataobject.__class__.__name__
            classInfo = gameDataobjectName.split(".")
            if classInfo[-1] == className:
               return GameDataField.getobjectByName(gameDataobjectName)
      elif packageName.find("com.ankamagames.dofus.datacenter") != 0:
         raise Exception(target.__class__.__name__+ " is queryable (note found in datacenter package).")
      return target

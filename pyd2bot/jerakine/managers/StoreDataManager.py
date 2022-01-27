import logging
import base64
from typing import Any
from pyd2bot.gameData.enums.dataStoreEnum import DataStoreEnum
from pyd2bot.jerakine import JerakineConstants
from pyd2bot.jerakine.types.CustomSharedObject import CustomSharedObject
from pyd2bot.jerakine.types.DataStoreType import DataStoreType
logger = logging.getLogger("bot")

class IExternalizable:
   pass

class Secure:
   pass

_aData:list = []
_bStoreSequence:bool = False
_nCurrentSequenceNum:int = 0
_aStoreSequence:list = []
_aSharedObjectCache:list = {}
_aRegisteredClassAlias:dict = {}
_bStoreSequence = False
_aData = []
_aSharedObjectCache = []
_aRegisteredClassAlias = dict()

def getSharedObject(sName:str) -> CustomSharedObject:
   if sName in _aSharedObjectCache:
      return _aSharedObjectCache[sName]
   so = CustomSharedObject.getLocal(sName)
   _aSharedObjectCache[sName] = so
   return so

def getData(dataType:DataStoreType, sKey:str) -> Any:
   so:CustomSharedObject = None
   if dataType.persistant:
      if dataType.location == DataStoreEnum.LOCATION_LOCAL:
         so = getSharedObject(dataType.category)
         if so.data:
            return so.data[sKey]
      elif dataType.location == DataStoreEnum.LOCATION_SERVER:
         return None
   if dataType.category in _aData:
      return _aData[dataType.category][sKey]
   return None

aClass:list = getData(JerakineConstants.DATASTORE_CLASS_ALIAS, "classAliasList")
for s in aClass:
   className = base64.decode(s)
   _aRegisteredClassAlias[className] = True

def isComplexType(o) -> bool:
   if type(o) in [int, float, bool, list, str, None.__class__]:
      return False
   else:
      return True

def registerClass(oInstance, deepClassScan:bool = False, keepClassInSo:bool = True) -> None:
   if isinstance(oInstance, IExternalizable):
      raise Exception("Can\'t store a customized IExternalizable in a shared object.")
   if isinstance(oInstance, Secure):
      raise Exception("Can\'t store a Secure class")
   if isComplexType(oInstance):
      className = oInstance.__class__.__name__
      sAlias = className.__hash__()
      if className not in _aRegisteredClassAlias:
         return
      try:
         oClass = oInstance.__class__
         globals().update({sAlias: oClass})
         logger.warn("Register " + className)
      except Exception as e:
         _aRegisteredClassAlias[className] = True
         logger.fatal("Impossible de trouver la classe " + className + " dans l\'application domain courant")
         return
      if keepClassInSo:
         aClassAlias = getSetData(JerakineConstants.DATASTORE_CLASS_ALIAS, "classAliasList",[])
         aClassAlias[base64.encode(className)] = sAlias
         setData(JerakineConstants.DATASTORE_CLASS_ALIAS, "classAliasList", aClassAlias)
      _aRegisteredClassAlias[className] = True
   if deepClassScan:
      if isinstance(oInstance, dict) or isinstance(oInstance, list) or isinstance(oInstance, list[Any]) or isinstance(oInstance is list[int]):
         desc = oInstance
         if isinstance(oInstance, list[Any]):
            tmp = oInstance.__class__.__name__
            leftBracePos = tmp.find("[")
            tmp = tmp[leftBracePos + 1: str(reversed(tmp)).find("]") - leftBracePos - 1]
            registerClass(oInstance.__class__(), True, keepClassInSo)
      else:
         desc = scanType(oInstance)
      for key in desc:
         if isComplexType(oInstance[key]):
            registerClass(oInstance[key], True)
         if desc == oInstance:
            break

def setData(dataType:DataStoreType, sKey:str, oValue, deepClassScan:bool = False) -> bool:
   so:CustomSharedObject = None
   if _aData[dataType.category] == None:
      _aData[dataType.category] = dict(True)
   _aData[dataType.category][sKey] = oValue
   if dataType.persistant:
      if dataType.location == DataStoreEnum.LOCATION_LOCAL:
         registerClass(oValue,deepClassScan)
         so = getSharedObject(dataType.category)
         if not so.data:
            so.data = {}
         so.data[sKey] = oValue
         if not _bStoreSequence:
            if not so.flush():
               return False
         else:
            _aStoreSequence[dataType.category] = dataType
         return True
      if dataType.location == DataStoreEnum.LOCATION_SERVER:
         return False
   return True

def getKeys(dataType:DataStoreType) -> list:
   so:CustomSharedObject = None
   key = None
   result:list = []
   if dataType.persistant:
      if dataType.location == DataStoreEnum.LOCATION_LOCAL:
            so = getSharedObject(dataType.category)
            data = so.datak
      if dataType.location == DataStoreEnum.LOCATION_SERVER:
         pass
   elif dataType.category in _aData:
      data = _aData[dataType.category]
   if data:
      for key in data:
         result.append(key)
   return result

def getSetData(dataType:DataStoreType, sKey:str, oValue) -> Any:
   o = getData(dataType, sKey)
   if o != None:
      return o
   setData(dataType,sKey,oValue)
   return oValue

def startStoreSequence() -> None:
   _bStoreSequence = True
   if not _nCurrentSequenceNum:
      _aStoreSequence = []
   _nCurrentSequenceNum+=1

def stopStoreSequence() -> None:
   dt:DataStoreType = None
   s = None
   _nCurrentSequenceNum -= 1
   _bStoreSequence = _nCurrentSequenceNum != 0
   if _bStoreSequence:
      return
   for s in _aStoreSequence:
      dt = _aStoreSequence[s]
      if dt.location == DataStoreEnum.LOCATION_LOCAL:
            getSharedObject(dt.category).flush()
      elif DataStoreEnum.LOCATION_SERVER:
            break
   _aStoreSequence = None

def clear(dataType:DataStoreType) -> None:
   _aData = []
   so:CustomSharedObject = getSharedObject(dataType.category)
   so.clear()

def reset() -> None:
   s:CustomSharedObject = None
   for s in _aSharedObjectCache:
      try:
         s.clear()
         s.close()
      except Exception as e:
         pass
   _aSharedObjectCache = []

def close(dataType:DataStoreType) -> None:
   if dataType.location == DataStoreEnum.LOCATION_LOCAL:
      _aSharedObjectCache[dataType.category].close()
      del _aSharedObjectCache[dataType.category]

def isComplexTypeFromstr(name:str) -> bool:
   if name in ("int", "float", "str", "bool", "list", "float", None):
      return False
   else:
      return _aRegisteredClassAlias[name]

def scanType(obj) -> object:
   name:str = None
   desc:list[str] = DescribeTypeCache.getVariables(obj, False, True, True, True)
   result = {}
   for name in desc:
      if isComplexTypeFromstr(obj[name].__class__.__name__):
         result[name] = True
   return result

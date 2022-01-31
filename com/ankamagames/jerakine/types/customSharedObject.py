# utf-8
import io
from com.ankamagames.jerakine.logger.Logger import Logger
import os
from com.ankamagames.dofus import Constants as Constants
from com.ankamagames.jerakine.data.ModuleReader import \
    ModuleReader

logger = Logger(__name__)


class CustomSharedObjectFileFormatError(Exception):
   pass


class CustomSharedObject:
   
   DATAFILE_EXTENSION = "dat"
   COMMON_FOLDER = Constants.DOFUS_COMMON_DIR
   directory = "Dofus"
   useDefaultDirectory = False
   clearedCacheAndRebooting = False
   throwException = True
   _cache = list['CustomSharedObject']()
   
   def __init__(self):   
      self.data = object()
      self.objectEncoding:int = None
      self._name:str = None 
      self._fileStream:io.BytesIO = None
      self._file:str = None 

   
   @classmethod
   def getLocal(cls, name:str) -> 'CustomSharedObject':
      if cls._cache[name]:
         return cls._cache[name]
      if not cls.COMMON_FOLDER:
         cls.COMMON_FOLDER = cls.getCustomSharedObjectDirectory()
      cso:CustomSharedObject = CustomSharedObject()
      cso._name = name
      cso.getDataFromFile()
      cls._cache[name] = cso
      return cso
   
   def getCustomSharedObjectDirectory(cls) -> str:
      return cls.COMMON_FOLDER
   
   def closeAll(cls) -> None:
      for cso in cls._cache:
         if cso:
            cso.close()
   
   def resetCache(cls) -> None:
      cls._cache = []
   
   def clearCache(cls, name:str) -> None:
      del cls._cache[name]
   
   def flush(cls) -> None:
      if cls.clearedCacheAndRebooting:
         return
      cls.writeData(cls.data)
   
   def clear(self) -> None:
      self.data = object()
      self.writeData(self.data)
   
   def close(self) -> None:
      if self._fileStream:
         self._fileStream.close()
   
   def writeData(self, data) -> bool:
      try:
         self._fileStream = open(self._file, "wb")
         amfEncoded = miniamf.encode(data).getvalue()
         self._fileStream.write(amfEncoded)
         self._fileStream.close()
      except Exception as e:
         if self._fileStream:
            self._fileStream.close()
         logger.error("Unable to write file : " + self._file)
         return False
      return True
   
   def getDataFromFile(self) -> None:
      if not self._file:
         self._file = os.path.join(self.COMMON_FOLDER, self._name + "." + self.DATAFILE_EXTENSION)
      if os.path.exists(self._file):
         try:
            with open(self._file, "rb") as fp:
               self._fileStream = fp
               fileAccessor = ModuleReader.getInstance()
               fileAccessor.init(self._file)
               self.data = fileAccessor.getObject()
         except Exception as e:
            if self._fileStream:
               self._fileStream.close()
            logger.error("Impossible d\'ouvrir le fichier " + self._file)
            if self.throwException:
               raise CustomSharedObjectFileFormatError("Malformated file : " + self._file)
      if not self.data:
         self.data = object()

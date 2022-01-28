import logging
from pathlib import Path
from typing import Any
import com.ankamagames.jerakine.data.gameDataClassDefinition as gdcd
from com.ankamagames.jerakine.data.gameDataProcess import GameDataProcess
from com.ankamagames.jerakine.utils.errors.singletonError import SingletonError
from com.hurlan.crypto.signature import Signature
from pyd2bot.utils.binaryIO.binaryStream import BinaryStream
logger = logging.getLogger("bot")


class GameDataFileAccessor:
   
   _self:'GameDataFileAccessor' = None
   _streams = dict[str, BinaryStream]()
   _streamStartIndex = dict()
   _indexes = dict()
   _classes = dict()
   _counter = dict()
   _gameDataProcessor = dict()
   
   def __init__(self):
      super().__init__()
      if self._self:
         raise SingletonError()
   
   @classmethod
   def getInstance(cls) -> 'GameDataFileAccessor':
      if not cls._self:
         cls._self = GameDataFileAccessor()
      return cls._self
   
   def init(self, file) -> None:
      nativeFile = Path(file)
      if not nativeFile or not nativeFile.exists():
         raise Exception("Game data file \'" + str(nativeFile) + "\' not readable.")
      moduleName:str = nativeFile.name.split(".d2o")[0]
      if not self._streams:
         self._streams = dict[str, BinaryStream]()
      if not self._streamStartIndex:
         self._streamStartIndex = dict[int]()
      stream = self._streams.get(moduleName)
      if not stream:
         stream = BinaryStream(nativeFile.open("rb"), True)
         self._streams[moduleName] = stream
         self._streamStartIndex[moduleName] = 7
      else:
         stream.position(0)
      self.initFromBinaryStream(stream,moduleName)
   
   def initFromBinaryStream(self, stream:BinaryStream, moduleName:str) -> None:
      len = 0
      count = 0
      if not self._streams:
         self._streams = dict[str, BinaryStream]()

      if not self._indexes:
         self._indexes = dict[str, dict]()

      if not self._classes:
         self._classes = dict()

      if not self._counter:
         self._counter = dict()

      if not self._streamStartIndex:
         self._streamStartIndex = dict()

      if not self._gameDataProcessor:
         self._gameDataProcessor = dict()

      self._streams[moduleName] = stream
      if not self._streamStartIndex[moduleName]:
         self._streamStartIndex[moduleName] = 7

      indexes = dict[int, int]()
      self._indexes[moduleName] = indexes
      contentOffset:int = 0
      # headers:str = stream.readMultiByte(3, "ASCII")
      headers = stream.readBytes(3)
      if headers != b'D2O':
         stream.position(0)
         try:
            headers = stream.readUTF()
         except Exception as e:
            pass
         if headers != Signature.ANKAMA_SIGNED_FILE_HEADER:
            raise Exception("Malformated game data file. (AKSF)")
         formatVersion = stream.readShort()
         len = stream.readInt()
         stream.position(stream.position() + len)
         contentOffset = stream.position()
         self._streamStartIndex[moduleName] = contentOffset + 7
         # headers = stream.readMultiByte(3, "ASCII")
         headers = stream.readBytes(3)
         if headers != b'D2O':
            raise Exception("Malformated game data file. (D2O)")
      
      indexesPointer:int = stream.readInt()
      stream.position(contentOffset + indexesPointer)
      indexesLength:int = stream.readInt()
      for i in range(0, indexesLength, 8):
         key = stream.readInt()
         pointer = stream.readInt()
         indexes[key] = contentOffset + pointer
         count += 1
      self._counter[moduleName] = count
      classes = dict()
      self._classes[moduleName] = classes
      classesCount:int = stream.readInt()
      for _ in range(classesCount):
         classIdentifier = stream.readInt()
         self.readClassDefinition(classIdentifier, stream, classes)
      if stream.remaining() > 0:
         self._gameDataProcessor[moduleName] = GameDataProcess(stream)
   
   def getDataProcessor(self, moduleName:str) -> GameDataProcess:
      return self._gameDataProcessor[moduleName]
   
   def getClassDefinition(self, moduleName:str, classId:int) -> 'gdcd.GameDataClassDefinition':
      return self._classes.get(moduleName, {}).get(classId)
   
   def getCount(self, moduleName:str) -> int:
      return self._counter[moduleName]
   
   def getObject(self, moduleName:str, objectId) -> Any:
      if not self._indexes or not self._indexes[moduleName]:
         return None
      pointer:int = self._indexes[moduleName][objectId]
      if not pointer:
         return None
      self._streams[moduleName].position = pointer
      classId:int = self._streams[moduleName].readInt()
      return self._classes[moduleName][classId].read(moduleName, self._streams[moduleName])
   
   def getObjects(self, moduleName:str) -> list:
      if not self._counter or not self._counter.get(moduleName):
         return None
      len = self._counter[moduleName]
      classes:dict = self._classes[moduleName]
      stream:BinaryStream = self._streams[moduleName]
      stream.position(self._streamStartIndex[moduleName])
      objs:list = list()
      objs = [classes[stream.readInt()].read(moduleName, stream) for _ in range(len)]
      return objs
   
   def close(self) -> None:
      for stream in self._streams:
         try:
            if isinstance(stream, BinaryStream):
               stream._base_stream.close()
         except Exception as e:
            continue
      self._streams = None
      self._indexes = None
      self._classes = None
   
   def readClassDefinition(self, classId:int, stream:BinaryStream, store:dict) -> None:
      fieldName:str = None
      className:str = stream.readUTF()
      packageName:str = stream.readUTF()
      classDef = gdcd.GameDataClassDefinition(packageName, className)
      fieldsCount:int = stream.readInt()
      for i in range(0, fieldsCount, 1):
         fieldName = stream.readUTF()
         classDef.addField(fieldName,stream)
      store[classId] = classDef


if __name__ == '__main__':
   a = GameDataFileAccessor.getInstance()
   f = r"C:\Users\majdoub\AppData\Local\Ankama\Dofus\data\common\Monsters.d2o"
   a.init(f)
   print(a.getObjects("Monsters"))

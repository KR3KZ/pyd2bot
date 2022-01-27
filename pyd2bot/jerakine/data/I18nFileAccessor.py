
import logging
import pathlib
from pyd2bot.utils.binaryIO.customDataWrapper import ByteArray
logger = logging.getLogger("bot")


class I18nFileAccessor:


   def __init__(self, fileUri:pathlib.Path): 
      self.textIndexesOverride:dict = None
      self.startTextIndex:int = 4
      self.directBuffer:ByteArray = ByteArray()
      self.key:int = 0
      self.pointer:int = 0
      self.diacriticalText:bool = False
      self.position:int = 0
      self.textKey = None
      nativeFile = pathlib.Path(fileUri)
      if not nativeFile or not nativeFile.exists():
         raise Exception("I18n file not readable.")
      self.stream = ByteArray(nativeFile.open("rb").read(), big_endian=True)
      self.indexes = dict()
      self.unDiacriticalIndex = dict()
      self.textIndexes = dict()
      self.textIndexesOverride = dict()
      self.textSortIndex = dict()
      self.textCount = 0
      indexesPointer:int = self.stream.readInt()
      keyCount:int = 0
      self.stream.position = indexesPointer
      indexesLength:int = self.stream.readInt()
      for i in range(0, indexesLength, 9):
         key = self.stream.readInt()
         diacriticalText = self.stream.readbool()
         pointer = self.stream.readInt()
         self.indexes[key] = pointer
         keyCount += 1
         if diacriticalText:
            keyCount += 1
            i += 4
            self.unDiacriticalIndex[key] = self.stream.readInt()
         else:
            self.unDiacriticalIndex[key] = pointer
      indexesLength = self.stream.readInt()
      while indexesLength > 0:
         position = self.stream.position
         textKey = self.stream.readUTF()
         pointer = self.stream.readInt()
         self.textCount += 1
         self.textIndexes[textKey] = pointer
         indexesLength -= self.stream.position - position
      indexesLength = self.stream.readInt()
      i = 0
      while indexesLength > 0:
         position = self.stream.position
         i += 1
         self.textSortIndex[self.stream.readInt()] = i
         indexesLength -= self.stream.position - position
      textKeys:list = []
      for textKey in self.textIndexes:
         textKeys.append(textKey)
      # EnterFrameDispatcher.worker.addForeachTreatment(setEntries, [], textKeys)
      # EnterFrameDispatcher.worker.addSingleTreatment(logInit, [])

   def logInit() -> None:
      logger.debug("Initialized !")

   # def setEntries(textKey:str) -> None:
   #    LangManager().setEntry:(textKey, getNamedText(textKey))

   def overrideId(self, oldId:int, newId:int) -> None:
      self.indexes[oldId] = self.indexes[newId]
      self.unDiacriticalIndex[oldId] = self.unDiacriticalIndex[newId]

   def getOrderIndex(self, key:int) -> int:
      return self.textSortIndex[key]

   def getText(self, key:int) -> str:
      if not self.indexes:
         return None
      pointer:int = self.indexes[key]
      if not pointer:
         return None
      if self.directBuffer == None:
         self.stream.position = pointer
         return self.stream.readUTF()
      self.directBuffer.position = pointer
      return self.directBuffer.readUTF()

   def getUnDiacriticalText(self, key:int) -> str:
      if not self.unDiacriticalIndex:
         return None
      pointer:int = self.unDiacriticalIndex[key]
      if not pointer:
         return None
      if self.directBuffer == None:
         self.stream.position = pointer
         return self.stream.readUTF()
      self.directBuffer.position = pointer
      return self.directBuffer.readUTF()

   def hasText(self, key:int) -> bool:
      return self.indexes and key in self.indexes

   def getNamedText(self, textKey:str) -> str:
      if not self.textIndexes:
         return None
      if self.textIndexesOverride[textKey]:
         textKey = self.textIndexesOverride[textKey]
      pointer:int = self.textIndexes[textKey]
      if not pointer:
         return None
      self.stream.position = pointer
      return self.stream.readUTF()

   def hasNamedText(self, textKey:str) -> bool:
      return self.textIndexes and self.textIndexes[textKey]

   def useDirectBuffer(self, bool:bool) -> None:
      if self.directBuffer == bool:
         return
      if not bool:
         self.directBuffer = None
      else:
         self.directBuffer = ByteArray()
         self.stream.position = 0
         self.stream.readBytes(self.directBuffer)

   def close(self) -> None:
      self.stream = None
      self.indexes = None
      self.textIndexes = None
      self.directBuffer = None

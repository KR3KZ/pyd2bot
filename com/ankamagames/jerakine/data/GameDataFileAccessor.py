from pathlib import Path
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from com.ankamagames.jerakine.data.gameDataProcess import GameDataProcess
    from com.ankamagames.jerakine.data.gameDataClassDefinition import GameDataClassDefinition
from com.ankamagames.jerakine.data.moduleReader import ModuleReader
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from pyd2bot.utils.binaryIO.binaryStream import BinaryStream


class GameDataFileAccessor(metaclass=Singleton):

    def __init__(self) -> None:
        self._modules = dict[str, ModuleReader]()
    
    def init(self, file:str) -> None:
        nativeFile = Path(file)
        moduleName:str = nativeFile.name.split(".d2o")[0]
        self._modules[moduleName] = ModuleReader(nativeFile.open('rb'))

    def initFromBinaryStream(self, modulename:str, moduleBinaries:BinaryStream):
        self._modules[modulename] = ModuleReader(moduleBinaries)

    def getDataProcessor(self, moduleName:str) -> 'GameDataProcess':
        return self._modules[moduleName]._gameDataProcessor
    
    def getClassDefinition(self, moduleName:str, classId:int) -> 'GameDataClassDefinition':
        return self._modules[moduleName]._classes[classId]
    
    def getCount(self, moduleName:str) -> int:
        return self._modules[moduleName]._counter[moduleName]
    
    def getObject(self, moduleName:str, objectId) -> Any:
        return self._modules[moduleName].getObject(objectId)
    
    def getObjects(self, moduleName:str) -> list:
        return self._modules[moduleName].getObjects()
    
    def close(self) -> None:
        for module in self._modules:
            self._modules[module].close()
        self._modules = dict[str, ModuleReader]()

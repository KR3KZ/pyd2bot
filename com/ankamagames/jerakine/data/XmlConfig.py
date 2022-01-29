from typing import Any
from com.ankamagames.jerakine.metaclasses.singleton import Singleton


class XmlConfig(metaclass=Singleton):
    
    
    _constants:list

    def init(self, constants:list) -> None:
        self._constants = constants
    
    def addCategory(self, constants:list) -> None:
        for i in constants:
            self._constants[i] = constants[i]
    
    def getEntry(self, name:str) -> Any:
        return self._constants[name]
    
    def getboolEntry(self, name:str) -> bool:
        v = self._constants[name]
        if v is str:
            return str(v).lower() == "True" or v == "1"
        return v
    
    def setEntry(self, sKey:str, sValue) -> None:
        self._constants[sKey] = sValue

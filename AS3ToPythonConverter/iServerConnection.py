from abc import ABC, abstractmethod, abstractproperty

from whistle import EventDispatcher


class IServerConnection(EventDispatcher, ABC):
      
   
   @abstractproperty
   def rawParser(self) -> RawDataParser:
      pass
   
   @rawParser.setter
   def rawParser(self, param1:RawDataParser) -> None:
      pass
   
   @abstractproperty
   def handler(self) -> MessageHandler:
      pass
   
   @handler.setter
   def handler(self, param1:MessageHandler) -> None:
      pass
   
   @abstractproperty
   def pauseBuffer(self) -> list:
      pass
   
   @abstractproperty
   def connected(self) -> bool:
      pass
   
   @abstractproperty
   def connecting(self) -> bool:
      pass
   
   @abstractproperty
   def latencyAvg(self) -> int:
      pass
   
   @abstractproperty
   def latencySamplesCount(self) -> int:
      pass
   
   @abstractproperty
   def latencySamplesMax(self) -> int:
      pass
   
   @abstractproperty
   def lagometer(self) -> ILagometer:
      pass
   
   @lagometer.setter
   def lagometer(self, param1:ILagometer) -> None:
      pass

   @abstractmethod
   def connect(self, param1:str, param2:int) -> None:
      pass
   
   @abstractmethod
   def close(self) -> None:
      pass
   
   @abstractmethod
   def pause(self) -> None:
      pass
   
   @abstractmethod
   def resume(self) -> None:
      pass
   
   @abstractmethod
   def send(self, param1:INetworkMessage, param2:str = "") -> None:
      pass

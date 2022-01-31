from whistle import EventDispatcher
from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.messages.messageHandler import MessageHandler


class IServerConnection(EventDispatcher):
      
   
   def rawParser(self) -> RawDataParser:
      pass
   
   @rawParser.setter
   def rawParser(self, param1:RawDataParser) -> None:
      pass
   
   def handler(self) -> MessageHandler:
      pass
   
   @handler.setter
   def handler(self, param1:MessageHandler) -> None:
      pass
   
   def pauseBuffer(self) -> list:
      pass
   
   def connected(self) -> bool:
      pass
   
   def connecting(self) -> bool:
      pass
   
   def latencyAvg(self) -> int:
      pass
   
   def latencySamplesCount(self) -> int:
      pass
   
   def latencySamplesMax(self) -> int:
      pass
   
   def lagometer(self) -> ILagometer:
      pass
   
   @lagometer.setter
   def lagometer(self, param1:ILagometer) -> None:
      pass

   def connect(self, param1:str, param2:int) -> None:
      pass
   
   def close(self) -> None:
      pass
   
   def pause(self) -> None:
      pass
   
   def resume(self) -> None:
      pass
   
   def send(self, param1:INetworkMessage, param2:str = "") -> None:
      pass

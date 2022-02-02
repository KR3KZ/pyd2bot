from threading import Timer
from com.ankamagames.dofus.kernel.Kernel import Kernel
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.network.messages.common.basic.BasicPingMessage import BasicPingMessage
from com.ankamagames.dofus.network.messages.handshake.ProtocolRequired import ProtocolRequired
from com.ankamagames.jerakine.benchmark.BenchmarkTimer import BenchmarkTimer
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.ConnectedMessage import ConnectedMessage
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.types.enums.Priority import Priority
from scripts.AS3ToPythonConverter.Metadata import Metadata
from com.ankamagames.dofus.kernel.PanicMessages import PanicMessages
logger = Logger(__name__)


class HandshakeFrame(Frame):
   
   TIMEOUT_DELAY:int = 3000
   
   TIMEOUT_REPEAT_COUNT:int = 1
   
   _timeoutTimer:BenchmarkTimer
   
   def __init__(self):
      super().__init__()
   
   def checkProtocolVersions(self, serverVersion:str) -> None:
      logger.info("Server version is " + serverVersion + ". Client version is " + Metadata.PROTOCOL_BUILD + ".")
      if not serverVersion or not Metadata.PROTOCOL_BUILD:
         logger.fatal("A protocol version is empty or None. What happened?")
         Kernel().panic(PanicMessages.MALFORMED_PROTOCOL,[Metadata.PROTOCOL_BUILD,serverVersion])
         return
      clientHash:str = self.extractHashFromProtocolVersion(Metadata.PROTOCOL_BUILD)
      if not clientHash:
         logger.fatal("The client protocol version is malformed: " + Metadata.PROTOCOL_BUILD)
         Kernel().panic(PanicMessages.MALFORMED_PROTOCOL,[Metadata.PROTOCOL_BUILD,serverVersion])
         return
      serverHash:str = self.extractHashFromProtocolVersion(serverVersion)
      if not serverHash:
         logger.fatal("The server protocol version is malformed: " + serverVersion)
         Kernel().panic(PanicMessages.MALFORMED_PROTOCOL,[Metadata.PROTOCOL_BUILD,serverVersion])
         return
      if clientHash is not serverHash:
         logger.fatal("Protocol mismatch between the client and the server.")
         Kernel().panic(PanicMessages.PROTOCOL_MISMATCH,[Metadata.PROTOCOL_BUILD,serverVersion])
   
   def extractHashFromProtocolVersion(self, protocolVersion:str) -> str:
      if not protocolVersion:
         return None
      matches:list = protocolVersion.split("-")
      if matches == None or len(matches) < 2:
         return None
      return matches[1]
   
   @property
   def priority(self) -> int:
      return Priority.HIGHEST
   
   def appended(self) -> bool: 
      connh.ConnectionsHandler.hasReceivedNetworkMsg = False
      return True
   
   def process(self, msg:Message) -> bool:
      prmsg:ProtocolRequired = None
      connh.ConnectionsHandler.hasReceivedMsg = True
      if isinstance(msg, INetworkMessage):
         connh.ConnectionsHandler.hasReceivedNetworkMsg = True
         if self._timeoutTimer is not None:
            self._timeoutTimer.stop()
      if isinstance(msg, ProtocolRequired):
         prmsg = msg
         self.checkProtocolVersions(prmsg.version)
         Kernel.getWorker().removeFrame(self)
         return True
      elif isinstance(msg, ConnectedMessage):
         self._timeoutTimer = Timer(self.TIMEOUT_DELAY, self.onTimeout)
         self._timeoutTimer.start()
         return True
      else:
         return False
   
   def onTimeout(self) -> None:
      pingMsg:BasicPingMessage = BasicPingMessage(quiet=True)
      connh.ConnectionsHandler.getConnection().send(pingMsg)
   
   def pulled(self) -> bool:
      if self._timeoutTimer is not None:
         self._timeoutTimer = None
      return True

from ctypes import ArgumentError
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.iServerConnection import IServerConnection
from com.ankamagames.dofus.kernel.kernel import Kernel
from com.ankamagames.dofus.kernel.net.connectionType import ConnectionType
from com.ankamagames.dofus.kernel.net.disconnectionReason import DisconnectionReason
from com.ankamagames.dofus.kernel.net.disconnectionReasonEnum import DisconnectionReasonEnum
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.network.messages.common.basic.BasicPingMessage import BasicPingMessage
from com.ankamagames.jerakine.network.multiConnection import MultiConnection
logger = Logger(__name__)


class ConnectionHander:

   GAME_SERVER:str = "game_server"

   KOLI_SERVER:str = "koli_server"

   _useSniffer:bool

   _currentConnection:MultiConnection = None

   _currentConnectionType:str= None

   _wantedSocketLost:bool = False

   _wantedSocketLostReason:int = 0

   _hasReceivedMsg:bool = False

   _hasReceivedNetworkMsg:bool = False

   _connectionTimeout = None
      

   @classmethod
   @property
   def useSniffer(cls) -> bool:
      return cls._useSniffer

   @classmethod
   @useSniffer.setter
   def useSniffer(cls, sniffer:bool) -> None:
      cls._useSniffer = sniffer

   @classmethod
   @property
   def connectionType(cls) -> str:
      return cls._currentConnectionType

   @property
   def hasReceivedMsg(cls) -> bool:
      return _hasReceivedMsg

   @hasReceivedMsg.setter
   def hasReceivedMsg(value:bool) -> None:
      _hasReceivedMsg = value

   @property
   def hasReceivedNetworkMsg(cls) -> bool:
      return cls._hasReceivedNetworkMsg

   @classmethod
   @hasReceivedNetworkMsg.setter
   def hasReceivedNetworkMsg(cls, value:bool) -> None:
      cls._hasReceivedNetworkMsg = value

   @classmethod
   def getConnection(cls) -> MultiConnection:
      if not cls._currentConnection:
         cls.createConnection()
      return cls._currentConnection

   @classmethod
   def connectToLoginServer(cls, host:str, port:int) -> None:
      if cls._currentConnection != None:
         cls.closeConnection()
      cls.etablishConnection(host, port, ConnectionType.TO_LOGIN_SERVER, cls._useSniffer)
      cls._currentConnectionType = ConnectionType.TO_LOGIN_SERVER

   classmethod
   def connectToGameServer(cls, gameServerHost:str, gameServerPort:int) -> None:
      cls.startConnectionTimer()
      if cls._currentConnection != None:
         cls.closeConnection()
      cls.etablishConnection(gameServerHost,gameServerPort, ConnectionType.TO_GAME_SERVER, cls._seSniffer)
      cls._currentConnectionType = ConnectionType.TO_GAME_SERVER
      PlayerManager().gameServerPort = gameServerPort

   @classmethod
   def connectToKoliServer(cls, gameServerHost:str, gameServerPort:int) -> None:
      cls.startConnectionTimer()
      if cls._currentConnection != None and cls._currentConnection.getSubConnection(ConnectionType.TO_KOLI_SERVER):
         cls._currentConnection.close(ConnectionType.TO_KOLI_SERVER)
      cls.etablishConnection(gameServerHost,gameServerPort, ConnectionType.TO_KOLI_SERVER, cls._seSniffer)
      cls._currentConnectionType = ConnectionType.TO_KOLI_SERVER
      PlayerManager().kisServerPort = gameServerPort

   @classmethod
   def confirmGameServerConnection(cls) -> None:
      cls.stopConnectionTimer()

   @classmethod
   def onConnectionTimeout(cls) -> None:
      msg:BasicPingMessage = None
      if cls._currentConnection and cls._currentConnection.connected:
         msg = BasicPingMessage()
         msg.initBasicPingMessage(True)
         logger.warn("La connection au serveur de jeu semble longue. On envoit un BasicPingMessage pour essayer de débloquer la situation.")
         cls._currentConnection.send(msg, cls._currentConnectionType)
         cls.stopConnectionTimer()

   @classmethod
   def closeConnection(cls) -> None:
      if Kernel().getWorker().contains(HandshakeFrame):
         Kernel().getWorker().removeFrame(Kernel().getWorker().getFrame(HandshakeFrame))
      if cls._currentConnection and cls._currentConnection.connected:
         cls._currentConnection.close()
      cls._currentConnection = None
      cls._currentConnectionType = ConnectionType.DISCONNECTED

   @classmethod
   def handleDisconnection(cls) -> DisconnectionReason:
      cls.closeConnection()
      reason:DisconnectionReason = DisconnectionReason(cls._antedSocketLost, cls._antedSocketLostReason)
      cls._antedSocketLost = False
      cls._antedSocketLostReason = DisconnectionReasonEnum.UNEXPECTED
      if not reason.expected:
         ChatServiceManager.destroy()
      return reason

   @classmethod
   def connectionGonnaBeClosed(cls, expectedReason:int) -> None:
      cls._antedSocketLostReason = expectedReason
      cls._antedSocketLost = True

   @classmethod
   def pause(cls) -> None:
      logger.info("Pause connection")
      cls._currentConnection.pause()

   @classmethod
   def resume(cls) -> None:
      logger.info("Resume connection")
      if cls._currentConnection:
         cls._currentConnection.resume()
      Kernel().getWorker().process(cls.ConnectionResumedMessage())

   @classmethod
   def startConnectionTimer(cls) -> None:
      if not cls._onnectionTimeout:
         cls._onnectionTimeout = BenchmarkTimer(4000, 1, "ConnectionsHandler._connectionTimeout (connectToKoliServer)")
         cls._onnectionTimeout.add_listener(TimerEvent.TIMER, onConnectionTimeout)
      else:
         cls._onnectionTimeout.reset()
      cls._onnectionTimeout.start()

   @classmethod
   def stopConnectionTimer(cls) -> None:
      if cls._onnectionTimeout:
         cls._onnectionTimeout.stop()
         cls._onnectionTimeout.removeEventListener(TimerEvent.TIMER, cls.onConnectionTimeout)

   @classmethod
   def etablishConnection(cls, host:str, port:int, id:str, useSniffer:bool = False, proxy:IConnectionProxy = None) -> None:
      conn:IServerConnection = None
      if useSniffer:
         if proxy != None:
            raise ArgumentError("Can\'t etablish a connection using a proxy and the sniffer.")
         conn = SnifferServerConnection(None,0,id)
      elif proxy != None:
         conn = ProxyedServerConnection(proxy,None,0,id)
      else:
         conn = ServerConnection(None,0,id)
      if not cls._currentConnection:
         cls.createConnection()
      conn.lagometer = LagometerAck()
      conn.handler = Kernel().getWorker()
      conn.rawParser = MessageReceiver()
      cls._currentConnection.addConnection(conn,id)
      cls._currentConnection.mainConnection = conn
      Kernel().getWorker().addFrame(HandshakeFrame())
      conn.connect(host,port)

   @classmethod
   def createConnection(cls) -> None:
      cls._currentConnection = MultiConnection()

from ctypes import ArgumentError
import logging
from AS3ToPythonConverter.iServerConnection import IServerConnection
from com.ankamagames.dofus.kernel.kernel import Kernel
from com.ankamagames.dofus.kernel.net.connectionType import ConnectionType
from com.ankamagames.dofus.kernel.net.disconnectionReason import DisconnectionReason
from com.ankamagames.dofus.kernel.net.disconnectionReasonEnum import DisconnectionReasonEnum
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.network.messages.common.basic.BasicPingMessage import BasicPingMessage
from com.ankamagames.jerakine.network.multiConnection import MultiConnection
logger = logging.getLogger("bot")

   
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
   

@property
def useSniffer(self) -> bool:
   return _useSniffer

@useSniffer.setter
def useSniffer(sniffer:bool) -> None:
   _useSniffer = sniffer

@property
def connectionType(self) -> str:
   return _currentConnectionType

@property
def hasReceivedMsg(self) -> bool:
   return _hasReceivedMsg

@hasReceivedMsg.setter
def hasReceivedMsg(value:bool) -> None:
   _hasReceivedMsg = value

@property
def hasReceivedNetworkMsg(self) -> bool:
   return _hasReceivedNetworkMsg

@hasReceivedNetworkMsg.setter
def hasReceivedNetworkMsg(value:bool) -> None:
   _hasReceivedNetworkMsg = value

def getConnection(self) -> MultiConnection:
   if not _currentConnection:
      createConnection()
   return _currentConnection

def connectToLoginServer(host:str, port:int) -> None:
   if _currentConnection != None:
      closeConnection()
   etablishConnection(host,port,ConnectionType.TO_LOGIN_SERVER,_useSniffer)
   _currentConnectionType = ConnectionType.TO_LOGIN_SERVER

def connectToGameServer(gameServerHost:str, gameServerPort:int) -> None:
   startConnectionTimer()
   if _currentConnection != None:
      closeConnection()
   etablishConnection(gameServerHost,gameServerPort,ConnectionType.TO_GAME_SERVER,_useSniffer)
   _currentConnectionType = ConnectionType.TO_GAME_SERVER
   PlayerManager().gameServerPort = gameServerPort

def connectToKoliServer(gameServerHost:str, gameServerPort:int) -> None:
   startConnectionTimer()
   if _currentConnection != None and _currentConnection.getSubConnection(ConnectionType.TO_KOLI_SERVER):
      _currentConnection.close(ConnectionType.TO_KOLI_SERVER)
   etablishConnection(gameServerHost,gameServerPort,ConnectionType.TO_KOLI_SERVER,_useSniffer)
   _currentConnectionType = ConnectionType.TO_KOLI_SERVER
   PlayerManager().kisServerPort = gameServerPort

def confirmGameServerConnection(self) -> None:
   stopConnectionTimer()

def onConnectionTimeout() -> None:
   msg:BasicPingMessage = None
   if _currentConnection and _currentConnection.connected:
      msg = BasicPingMessage()
      msg.initBasicPingMessage(True)
      logger.warn("La connection au serveur de jeu semble longue. On envoit un BasicPingMessage pour essayer de débloquer la situation.")
      _currentConnection.send(msg, _currentConnectionType)
      stopConnectionTimer()

def closeConnection(self) -> None:
   if Kernel().getWorker().contains(HandshakeFrame):
      Kernel().getWorker().removeFrame(Kernel().getWorker().getFrame(HandshakeFrame))
   if _currentConnection and _currentConnection.connected:
      _currentConnection.close()
   _currentConnection = None
   _currentConnectionType = ConnectionType.DISCONNECTED

def handleDisconnection(self) -> DisconnectionReason:
   closeConnection()
   reason:DisconnectionReason = DisconnectionReason(_wantedSocketLost,_wantedSocketLostReason)
   _wantedSocketLost = False
   _wantedSocketLostReason = DisconnectionReasonEnum.UNEXPECTED
   if not reason.expected:
      ChatServiceManager.destroy()
   return reason

def connectionGonnaBeClosed(expectedReason:int) -> None:
   _wantedSocketLostReason = expectedReason
   _wantedSocketLost = True

def pause(self) -> None:
   logger.info("Pause connection")
   _currentConnection.pause()

def resume(self) -> None:
   logger.info("Resume connection")
   if _currentConnection:
      _currentConnection.resume()
   Kernel().getWorker().process(ConnectionResumedMessage())

def startConnectionTimer(self) -> None:
   if not _connectionTimeout:
      _connectionTimeout = BenchmarkTimer(4000, 1, "ConnectionsHandler._connectionTimeout (connectToKoliServer)")
      _connectionTimeout.addEventListener(TimerEvent.TIMER,onConnectionTimeout)
   else:
      _connectionTimeout.reset()
   _connectionTimeout.start()

def stopConnectionTimer(self) -> None:
   if _connectionTimeout:
      _connectionTimeout.stop()
      _connectionTimeout.removeEventListener(TimerEvent.TIMER,onConnectionTimeout)

def etablishConnection(host:str, port:int, id:str, useSniffer:bool = False, proxy:IConnectionProxy = None) -> None:
   conn:IServerConnection = None
   if useSniffer:
      if proxy != None:
         raise ArgumentError("Can\'t etablish a connection using a proxy and the sniffer.")
      conn = SnifferServerConnection(None,0,id)
   elif proxy != None:
      conn = ProxyedServerConnection(proxy,None,0,id)
   else:
      conn = ServerConnection(None,0,id)
   if not _currentConnection:
      createConnection()
   conn.lagometer = LagometerAck()
   conn.handler = Kernel().getWorker()
   conn.rawParser = MessageReceiver()
   _currentConnection.addConnection(conn,id)
   _currentConnection.mainConnection = conn
   Kernel().getWorker().addFrame(HandshakeFrame())
   conn.connect(host,port)

def createConnection(self) -> None:
   _currentConnection = MultiConnection()

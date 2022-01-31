import logging
from types import FunctionType
from whistle import Event, EventDispatcher
from com.ankamagames.jerakine.network.iServerConnection import IServerConnection
from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.messages.message import Message
from com.ankamagames.jerakine.messages.messageHandler import MessageHandler
from com.ankamagames.jerakine.network.NetworkSentEvent import NetworkSentEvent
from com.ankamagames.jerakine.network.events.basicEvent import BasicEvent
from com.ankamagames.jerakine.network.events.iOErrorEvent import IOErrorEvent
from com.ankamagames.jerakine.network.events.securityErrorEvent import SecurityErrorEvent
from com.ankamagames.jerakine.network.iMessagerouter import IMessageRouter
logger = logging.getLogger("bot")


class MultiConnection(EventDispatcher):
      
   
   _connectionByMsg:dict
   
   _connectionByEvent:dict
   
   _connectionById:dict
   
   _idByConnection:dict
   
   _connectionCount:int
   
   _mainConnection:IServerConnection

   _messageRouter:IMessageRouter
   
   _connectionConnectedCount:int
   
   def __init__(self):
      self._connectionByMsg = dict()
      self._connectionByEvent = dict()
      self._connectionById = dict()
      self._idByConnection = dict()
      super().__init__()
   
   @property
   def mainConnection(self) -> IServerConnection:
      return self._mainConnection
   
   @mainConnection.setter
   def mainConnection(self, conn:IServerConnection) -> None:
      if not self._idByConnection.get(conn):
         raise Exception("Connection must be added before setted to be the main connection")
      self._mainConnection = conn
   
   @property
   def messageRouter(self) -> IMessageRouter:
      return self._messageRouter
   
   @messageRouter.setter
   def messageRouter(self, mr:IMessageRouter) -> None:
      self._messageRouter = mr
   
   @property
   def connected(self) -> bool:
      return self._connectionConnectedCount != 0
   
   @property
   def connectionCount(self) -> int:
      return self._connectionCount
   
   def addConnection(self, conn:IServerConnection, id:str) -> None:
      if self._connectionById.get(id):
         self.removeConnection(id)
      if self._idByConnection.get(conn):
         self.removeConnection(conn)
      self._connectionById[id] = conn
      self._idByConnection[conn] = id
      self._connectionCount += 1
      logger.warn("Adding connection " + id)
      conn.handler = MessageWatcher(self.proccessMsg, conn.handler, conn)
      conn.add_listener(BasicEvent.CONNECT, self.onSubConnectionEvent)
      conn.add_listener(BasicEvent.CLOSE, self.onSubConnectionEvent)
      conn.add_listener(IOErrorEvent.IO_ERROR, self.onSubConnectionEvent)
      conn.add_listener(SecurityErrorEvent.SECURITY_ERROR, self.onSubConnectionEvent)
      if conn.connected:
         self._connectionConnectedCount += 1
   
   def removeConnection(self, idOrConnection) -> bool:
      if isinstance(idOrConnection, str):
         id = idOrConnection
         conn = self.getSubConnection(idOrConnection)
      if isinstance(idOrConnection, IServerConnection):
         id = self._idByConnection[idOrConnection]
         conn = idOrConnection
      if not conn:
         return False
      conn.remove_listener(BasicEvent.CONNECT, self.onSubConnectionEvent)
      conn.remove_listener(BasicEvent.CLOSE, self.onSubConnectionEvent)
      conn.remove_listener(IOErrorEvent.IO_ERROR, self.onSubConnectionEvent)
      conn.remove_listener(SecurityErrorEvent.SECURITY_ERROR, self.onSubConnectionEvent)
      self._connectionCount -= 1
      if conn.connected:
         self._connectionConnectedCount -= 1
      del self._connectionById[id]
      del self._idByConnection[conn]
      if self._mainConnection == conn:
         for otherConn in self._connectionById:
            self._mainConnection = otherConn
      if isinstance(conn.handler, MessageWatcher):
         conn.handler = MessageWatcher(conn.handler).handler
      return True
   
   def getSubConnection(self, idOrMessageOrEvent = None) -> IServerConnection:
      if isinstance(idOrMessageOrEvent, str):
         return self._connectionById[idOrMessageOrEvent]
      if isinstance(idOrMessageOrEvent, Message):
         return self._connectionByMsg[idOrMessageOrEvent]
      if isinstance(idOrMessageOrEvent, Event):
         return self._connectionByEvent[idOrMessageOrEvent]
      raise TypeError("Can\'t handle " + idOrMessageOrEvent + " class")
   
   def getConnectionId(self, idOrMessageOrEvent = None) -> str:
      conn:IServerConnection = self.getSubConnection(idOrMessageOrEvent)
      return self._idByConnection[conn]
   
   def getPauseBuffer(self, id:str = None) -> list:
      mergedPauseBuffer:list = None
      conn:IServerConnection = None
      if id and self._connectionById.get(id):
         return IServerConnection(self._connectionById[id]).pauseBuffer
      if not id:
         mergedPauseBuffer = []
         for conn in self._connectionById:
            mergedPauseBuffer = mergedPauseBuffer.extend(conn.pauseBuffer)
         return mergedPauseBuffer
      return None
   
   def close(self, id:str = None) -> None:
      if id:
         logger.warn("Connection " + id + " will be closed...")
         if self._connectionById.get(id):
            self._connectionById[id].close()
            if self._connectionCount > 1:
               self.removeConnection(id)
         return
      logger.warn("All connections will be closed...")
      for connection in self._connectionById.values():
         connection.close()
   
   def pause(self, id:str = None) -> None:
      connection:IServerConnection = None
      if id:
         if self._connectionById.get(id):
            IServerConnection(self._connectionById[id]).pause()
         return
      for connection in self._connectionById.values():
         connection.pause()
   
   def resume(self, id:str = None) -> None:
      connection:IServerConnection = None
      if id:
         if self._connectionById.get(id):
            IServerConnection(self._connectionById[id]).resume()
         return
      for connection in self._connectionById.values():
         connection.resume()
   
   def send(self, msg:INetworkMessage, connectionId:str = "") -> None:
      conn:IServerConnection = None
      if self._messageRouter:
         if connectionId == "":
            connectionId = self._messageRouter.getConnectionId(msg)
         if not connectionId or connectionId == "":
            logger.error(msg + " sending impossible : no connection id")
            return
         if connectionId == "all":
            for conn in self._connectionById.values():
               if conn.connected:
                  conn.send(msg)
         else:
            self.getSubConnection(connectionId).send(msg)
      elif self._mainConnection:
         self._mainConnection.send(msg)
      if self.has_listeners(NetworkSentEvent.EVENT_SENT):
         self.dispatch(NetworkSentEvent.EVENT_SENT, NetworkSentEvent(msg))
   
   def proccessMsg(self, msg:Message, conn:IServerConnection) -> None:
      self._connectionByMsg[msg] = conn
   
   def onSubConnectionEvent(self, e:Event) -> None:
      if e.name == BasicEvent.CONNECT:
         self._connectionConnectedCount+=1
      elif e.name == BasicEvent.CLOSE:
         self._connectionConnectedCount-=1
      self._connectionByEvent[e] = e.dispatcher
      if self.has_listeners(e.name):
         self.dispatch(e.name, e)



class MessageWatcher(MessageHandler):
   

   watchFunctionType:FunctionType

   handler:MessageHandler

   conn:IServerConnection

   def __init__(self, watchFunctionType:FunctionType, handler:MessageHandler, conn:IServerConnection):
      super().__init__()
      self.watchFunctionType = watchFunctionType
      self.handler = handler
      self.conn = conn

   def process(self, msg:Message) -> bool:
      self.watchFunctionType(msg, self.conn)
      return self.handler.process(msg)

import math
from multiprocessing.managers import Server
import time
from typing import TYPE_CHECKING
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
if TYPE_CHECKING:
   from com.ankamagames.dofus.internalDatacenter.connection.basicCharacterWrapper import BasicCharacterWrapper
from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
from com.ankamagames.jerakine.interfaces.IDestroyable import IDestroyable
from com.ankamagames.jerakine.utils.errors.SingletonError import SingletonError


class PlayerManager(IDestroyable):
   __metaclasse__ = Singleton
   
   _self:'PlayerManager'
   
   TAG_PREFIX:str = "#"
   
   TAG_ADMINS:str = "OFFI"
      
   accountId:int
   
   communityId:int
   
   hasRights:bool
   
   hasConsoleRight:bool
   
   nickname:str
   
   tag:str
   
   subscriptionEndDate:float
   
   secretQuestion:str
   
   adminStatus:int
   
   passkey:str
   
   accountCreation:float
   
   isSafe:bool = False
   
   canCreateNewCharacter:bool = True
   
   _server:Server
   
   _gameServerPort:int
   
   _kisServerPort:int
   
   serverCommunityId:int = -1
   
   serverLang:str
   
   serverGameType:int = -1
   
   serverIsMonoAccount:bool
   
   serversList:list[int]
   
   charactersList:list['BasicCharacterWrapper']
   
   allowAutoConnectCharacter:bool = False
   
   autoConnectOfASpecificCharacterId:float = -1
   
   wasAlreadyConnected:bool = False
   
   havenbagAvailableRooms:list[HavenBagRoomPreviewInformation]
   
   havenbagAvailableThemes:list[int]
   
   arenaLeaveBanTime:int = -1
   
   hasFreeAutopilot:bool
   
   
   def __init__(self):
      self.havenbagAvailableThemes = list[int]()
      super().__init__()
      self._subscriptionEndDateUpdateTime:float = 0
      self._subscriptionDurationElapsed:float = 0
      self.serversList:list[int] = list[int]()
      if not self._subscriptionEndDateUpdateTime:
         self.refreshSubscriptionEndDateUpdateTime()

   @property
   def server(self) -> Server:
      if self._server:
         if self.serverCommunityId > -1:
            self._server.communityId = self.serverCommunityId
         if self.serverGameType > -1:
            self._server.gameTypeId = self.serverGameType
         self._server.monoAccount = self.serverIsMonoAccount
         if self.serverLang != "":
            self._server.language = self.serverLang
      return self._server

   @server.setter
   def server(self, s:Server) -> None:
      self._server = s

   @property
   def gameServerPort(self) -> int:
      return self._gameServerPort

   @gameServerPort.setter
   def gameServerPort(self, value:int) -> None:
      self._gameServerPort = value
      
   @property
   def kisServerPort(self) -> int:
      return self._kisServerPort

   @kisServerPort.setter
   def kisServerPort(self, value:int) -> None:
      self._kisServerPort = value
   
   @property
   def subscriptionDurationElapsed(self) -> float:
      now:float = None
      subscriptionSinceConnection:float = None
      if self.subscriptionEndDate > self._subscriptionEndDateUpdateTime:
         now = time.time()
         subscriptionSinceConnection = min(self.subscriptionEndDate, now) - self._subscriptionEndDateUpdateTime
         if subscriptionSinceConnection > 0:
            return self._subscriptionDurationElapsed + math.floor(subscriptionSinceConnection / 1000)
      return self._subscriptionDurationElapsed
   
   @subscriptionDurationElapsed.setter
   def subscriptionDurationElapsed(self, n:float) -> None:
      self._subscriptionDurationElapsed = n
   
   def refreshSubscriptionEndDateUpdateTime(self) -> None:
      self._subscriptionEndDateUpdateTime = time.time()
   
   def isBasicAccount(self) -> bool:
      return self.subscriptionEndDate <= 0 and not self.hasRights
   
   def isMapInHavenbag(self, mapId:int) -> bool:
      return HavenbagTheme.isMapIdInHavenbag(mapId)
   
   def formatTagName(self, name:str, tag:str, other:str = None, withStyle:bool = True, forceRealTag:bool = False) -> str:
      displayedTag:str = self.TAG_ADMINS if name.find("[") == 0 and name.find("]") == len(name) - 1 and name != self.nickname and not forceRealTag else tag
      if withStyle:
         return self.addTagStyleToText("nameStyle",name) + (self.addTagStyleToText("tagStyle", self.TAG_PREFIX + displayedTag) if not tag else "") +\
             (self.addTagStyleToText("other"," (" + other + ")") if not other else "")
      return name + (self.TAG_PREFIX + displayedTag if not tag else "") + (" (" + other + ")" if not other else "")
   
   def addTagStyleToText(self, tagStyleName:str, text:str) -> str:
      return "<span class=\"" + tagStyleName + "\">" + text + "</span>"
   
   def destroy(self) -> None:
      self._self = None

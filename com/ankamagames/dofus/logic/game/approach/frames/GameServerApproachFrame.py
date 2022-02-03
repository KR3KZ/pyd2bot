
from threading import Timer
import time
from com.ankamagames.dofus import BuildInfos
from com.ankamagames.dofus.internalDatacenter.connection.basicCharacterWrapper import BasicCharacterWrapper
# from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
import com.ankamagames.dofus.kernel.Kernel as krnl
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import AuthentificationManager
from com.ankamagames.dofus.logic.common.managers.InterClientManager import InterClientManager
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.network.enums.CharacterDeletionErrorEnum import CharacterDeletionErrorEnum
from com.ankamagames.dofus.network.messages.connection.ServerSelectionMessage import ServerSelectionMessage
from com.ankamagames.dofus.network.messages.game.approach.AccountCapabilitiesMessage import AccountCapabilitiesMessage
from com.ankamagames.dofus.network.messages.game.approach.AlreadyConnectedMessage import AlreadyConnectedMessage
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketAcceptedMessage import AuthenticationTicketAcceptedMessage
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketMessage import AuthenticationTicketMessage
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketRefusedMessage import AuthenticationTicketRefusedMessage
from com.ankamagames.dofus.network.messages.game.approach.HelloGameMessage import HelloGameMessage
from com.ankamagames.dofus.network.messages.game.basic.BasicTimeMessage import BasicTimeMessage
from com.ankamagames.dofus.network.messages.game.character.choice.BasicCharactersListMessage import BasicCharactersListMessage
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedForceMessage import CharacterSelectedForceMessage
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedForceReadyMessage import CharacterSelectedForceReadyMessage
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedSuccessMessage import CharacterSelectedSuccessMessage
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListErrorMessage import CharactersListErrorMessage
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListMessage import CharactersListMessage
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListRequestMessage import CharactersListRequestMessage
from com.ankamagames.dofus.network.messages.game.character.creation.CharacterCanBeCreatedRequestMessage import CharacterCanBeCreatedRequestMessage
from com.ankamagames.dofus.network.messages.game.character.creation.CharacterCanBeCreatedResultMessage import CharacterCanBeCreatedResultMessage
from com.ankamagames.dofus.network.messages.game.character.creation.CharacterNameSuggestionFailureMessage import CharacterNameSuggestionFailureMessage
from com.ankamagames.dofus.network.messages.game.character.deletion.CharacterDeletionErrorMessage import CharacterDeletionErrorMessage
from com.ankamagames.dofus.network.messages.game.context.GameContextCreateErrorMessage import GameContextCreateErrorMessage
from com.ankamagames.dofus.network.messages.game.moderation.PopupWarningCloseRequestMessage import PopupWarningCloseRequestMessage
from com.ankamagames.dofus.network.messages.game.moderation.PopupWarningClosedMessage import PopupWarningClosedMessage
from com.ankamagames.dofus.network.messages.game.startup.StartupActionsListMessage import StartupActionsListMessage
from com.ankamagames.dofus.network.messages.security.ClientKeyMessage import ClientKeyMessage
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.messages.ServerConnectionFailedMessage import ServerConnectionFailedMessage
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.Priority import Priority
logger = Logger(__name__)

class GameServerApproachFrame(Frame):
   
      
   authenticationTicketAccepted:bool = False
   
   LOADING_TIMEOUT:int = 60000.0
   
   _charactersList:list[BasicCharacterWrapper]
   
   _charactersToRemodelList:list
      
   _loadingStart:float
   
   _waitingMessages:list[Message]
   
   _cssmsg:CharacterSelectedSuccessMessage
   
   _requestedCharacterId:float
   
   _requestedToRemodelCharacterId:float
   
   _waitingForListRefreshAfterDeletion:bool
      
   commonMod:object
   
   _giftList:list
   
   _charaListMinusDeadPeople:list
   
   _reconnectMsgSend:bool = False
   
   _openCharsList:bool = True
   
   def __init__(self):
      self._charactersList = list[BasicCharacterWrapper]()
      self._charactersToRemodelList = []
      self._giftList = []
      self._charaListMinusDeadPeople = []
      super().__init__()
   
   @property
   def priority(self) -> int:
      return Priority.NORMAL
   
   @property
   def giftList(self) -> list:
      return self._giftList
   
   @property
   def charaListMinusDeadPeople(self) -> list:
      return self._charaListMinusDeadPeople
   
   @property
   def requestedCharaId(self) -> float:
      return self._requestedCharacterId
   
   @requestedCharaId.setter
   def requestedCharaId(self, id:float) -> None:
      self._requestedCharacterId = id
   
   def isCharacterWaitingForChange(self, id:float) -> bool:
      if self._charactersToRemodelList[id]:
         return True
      return False
   
   def process(self, msg:Message) -> bool:

      if isinstance(msg, HelloGameMessage):
         connh.ConnectionsHandler.confirmGameServerConnection()
         self.authenticationTicketAccepted = False
         atmsg = AuthenticationTicketMessage(lang="fr", ticket=AuthentificationManager().gameServerTicket)
         connh.ConnectionsHandler.getConnection().send(atmsg)
         return True

      elif isinstance(msg, AuthenticationTicketAcceptedMessage):
         Timer(0.5, self.requestCharactersList).start
         self.authenticationTicketAccepted = True
         return True

      elif isinstance(msg, AuthenticationTicketRefusedMessage):
         self.authenticationTicketAccepted = False
         return True

      elif isinstance(msg, ServerConnectionFailedMessage):
         scfMsg = ServerConnectionFailedMessage(msg)
         self.authenticationTicketAccepted = False
         if scfMsg.failedConnection == connh.ConnectionsHandler.getConnection().getSubConnection(scfMsg):
            PlayerManager().destroy()
         return True

      elif isinstance(msg, AlreadyConnectedMessage):
         PlayerManager().wasAlreadyConnected = True
         return True

      elif isinstance(msg, CharactersListErrorMessage):
         return False
      
      elif isinstance(msg, AccountCapabilitiesMessage):
         accmsg = msg
         PlayerManager().adminStatus = accmsg.status
         PlayerManager().canCreateNewCharacter = accmsg.canCreateNewCharacter
         return True

      elif isinstance(msg, CharacterSelectedSuccessMessage):
         cssmsg = msg
         self._loadingStart = time.time()
         connh.ConnectionsHandler.pause()
         if krnl.Kernel().getWorker().getFrame(ServerSelectionMessage):
            krnl.Kernel().getWorker().removeFrame(krnl.Kernel().getWorker().getFrame(ServerSelectionFrame))
         PlayedCharacterManager().infos = cssmsg.infos
         DataStoreType.CHARACTER_ID = str(cssmsg.infos.id)
         krnl.Kernel().getWorker().pause()
         self._cssmsg = cssmsg
         if cssmsg.infos.id == self._requestedToRemodelCharacterId:
            for j in range(self.len(self._charactersList)):
               bchar = self._charactersList[j]
               if bchar.id == cssmsg.infos.id:
                  self._charactersList[j] = BasicCharacterWrapper.create(
                     bchar.id,
                     cssmsg.infos.name,
                     cssmsg.infos.level,
                     cssmsg.infos.entityLook,
                     cssmsg.infos.breed,
                     cssmsg.infos.sex,
                     0,
                     0,
                     bchar.bonusXp
                  )
         return True

      elif isinstance(msg, AllModulesLoadedMessage):
         logger.warn("GameServerApproachFrame AllModulesLoaded")
         self._gmaf = None
         krnl.Kernel().getWorker().addFrame(WorldFrame())
         krnl.Kernel().getWorker().addFrame(SynchronisationFrame())
         krnl.Kernel().getWorker().addFrame(PlayedCharacterUpdatesFrame())
         krnl.Kernel().getWorker().addFrame(SpellInventoryManagementFrame())
         krnl.Kernel().getWorker().addFrame(InventoryManagementFrame())
         krnl.Kernel().getWorker().addFrame(ContextChangeFrame())
         krnl.Kernel().getWorker().addFrame(ProgressionFrame())
         krnl.Kernel().getWorker().addFrame(ChatFrame())
         krnl.Kernel().getWorker().addFrame(JobsFrame())
         krnl.Kernel().getWorker().addFrame(QuestFrame())
         krnl.Kernel().getWorker().addFrame(PartyManagementFrame())
         krnl.Kernel().getWorker().addFrame(AveragePricesFrame())
         krnl.Kernel().getWorker().removeFrame(krnl.Kernel().getWorker().getFrame(GameStartingFrame))
         krnl.Kernel().getWorker().resume()
         connh.ConnectionsHandler.resume()
         if krnl.Kernel().beingInReconection and not self._reconnectMsgSend:
            self._reconnectMsgSend = True
            connh.ConnectionsHandler.getConnection().send(CharacterSelectedForceReadyMessage())
         if InterClientManager.flashKey and (not PlayerManager() or PlayerManager().server.id != 129 and PlayerManager().server.id != 130): 
            flashKeyMsg = ClientKeyMessage(key=InterClientManager().flashKey)
            connh.ConnectionsHandler.getConnection().send(flashKeyMsg)
         if self._cssmsg != None:
            PlayedCharacterManager().infos = self._cssmsg.infos
            DataStoreType.CHARACTER_ID = str(self._cssmsg.infos.id)
         krnl.Kernel().getWorker().removeFrame(self)
         gccrmsg = GameContextCreateErrorMessage()
         connh.ConnectionsHandler.getConnection().send(gccrmsg)

         now = time.time()
         delta = now - self._loadingStart
         if delta > self.LOADING_TIMEOUT:
            logger.warn("Client took too long to load (" + tag.duration + "s), reporting.")
         ChatServiceManager().tryToConnect()
         return True

      elif isinstance(msg, ConnectionResumedMessage):
         return True

      elif isinstance(msg, CharacterSelectedForceMessage):
         logger.error("Impossible to select character, server is full.")
         self._requestedCharacterId = 0
         return True

      elif isinstance(msg, BasicTimeMessage):
         btmsg = msg
         date = Date()
         TimeManager().serverTimeLag = btmsg.timestamp + btmsg.timezoneOffset * 60 * 1000 - date.getTime()
         TimeManager().serverUtcTimeLag = btmsg.timestamp - date.getTime()
         TimeManager().timezoneOffset = btmsg.timezoneOffset * 60 * 1000
         TimeManager().dofusTimeYearLag = -1370
         return True
         
      elif isinstance(msg, StartupActionsListMessage):
         salm = msg
         self._giftList = []
         for gift in salm.actions:
            _items = []
            for item in gift.items:
               iw = ItemWrapper.create(0, 0, item.objectGID, item.quantity, item.effects, False)
               _items.append(iw)
               oj = {
                  "uid":gift.uid,
                  "title":gift.title,
                  "text":gift.text,
                  "items":_items
               }
            self._giftList.append(oj)
         if len(self._giftList):
            self._charaListMinusDeadPeople = []
            for perso in self._charactersList:
               if not perso.deathState or perso.deathState == 0:
                  self._charaListMinusDeadPeople.append(perso)
         else:
            krnl.Kernel().getWorker().removeFrame(self)
            logger.warn("Empty Gift List Received")
         return True

      elif isinstance(msg, PopupWarningClosedMessage):
         return True

      elif isinstance(msg, PopupWarningCloseRequestAction):
         pwcrmsg = PopupWarningCloseRequestMessage()
         connh.ConnectionsHandler.getConnection().send(pwcrmsg)
         return True

      return False

   def pulled(self) -> bool:
      return True

   def requestCharactersList(self) -> None:
      clrmsg:CharactersListRequestMessage = CharactersListRequestMessage()
      if connh.ConnectionsHandler.getConnection():
         connh.ConnectionsHandler.getConnection().send(clrmsg)


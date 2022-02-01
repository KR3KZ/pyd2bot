from mailbox import Message
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.kernel.net.DisconnectionReasonEnum import DisconnectionReasonEnum
from com.ankamagames.dofus.logic.common.managers.AuthentificationManager import AuthentificationManager
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.network.messages.connection.HelloConnectMessage import HelloConnectMessage
from com.ankamagames.dofus.network.messages.connection.IdentificationAccountForceMessage import IdentificationAccountForceMessage
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.network.messages.ServerConnectionFailedMessage import ServerConnectionFailedMessage
from com.ankamagames.jerakine.types.enums.Priority import Priority
logger = Logger(__name__)


class AuthentificationFrame(Frame):
   
   
   HIDDEN_PORT:int = 443
   
   CONNEXION_MODULE_NAME:str = "ComputerModule_Ankama_Connection"
   
   _lastTicket:str
   
   _connexionHosts:list = []
   
   _loader:IResourceLoader
   
   _contextLoader:LoaderContext
   
   _dispatchModuleHook:bool
   
   _connexionSequence:list
   
   _lastLoginHash:str
   
   _currentLogIsForced:bool = False
   

   
   def __init__(self, dispatchModuleHook:bool = True):
      super().__init__()
      self._dispatchModuleHook = dispatchModuleHook
      self._contextLoader = LoaderContext()
   
   @property
   def priority(self) -> int:
      return Priority.NORMAL
   
   def handleConnectionOpened(self) -> None:
      pass
   
   def handleConnectionClosed(self) -> None:
      pass
   
   def appended() -> bool:
      if self._dispatchModuleHook:
         dhf = Kernel.getWorker().getFrame(DisconnectionHandlerFrame) 
         KernelEventsManager().processCallback(HookList.AuthentificationStart, dhf.mustShowLoginInterface)
      return True
   
   def process(self, msg:Message) -> bool:

         if isinstance(msg, ServerConnectionFailedMessage):
            scfMsg = msg
            if scfMsg.failedConnection == ConnectionsHandler.getConnection().getSubConnection(scfMsg):
               ConnectionsHandler.getConnection().mainConnection.stopConnectionTimeout()
               if self._connexionSequence:
                  retryConnInfo = self._connexionSequence.pop(0)
                  if retryConnInfo:
                     ConnectionsHandler.connectToLoginServer(retryConnInfo.host, retryConnInfo.port)
                  else:
                     PlayerManager().destroy()
            return True

         elif isinstance(msg, HelloConnectMessage):
            hcmsg = HelloConnectMessage(msg)
            AuthentificationManager().setPublicKey(hcmsg.key)
            AuthentificationManager().setSalt(hcmsg.salt)
            AuthentificationManager().initAESKey()
            iMsg = AuthentificationManager().getIdentificationMessage()
            self._currentLogIsForced = isinstance(iMsg, IdentificationAccountForceMessage)
            logger.info("Current version : " + iMsg.version.major + "." + iMsg.version.minor + "." + iMsg.version.code + "." + iMsg.version.build)
            dhf = Kernel.getWorker().getFrame(DisconnectionHandlerFrame) as DisconnectionHandlerFrame
            time = Math.round(perf_counter()() / 1000)
            elapsedTimesSinceConnectionFail = list[int]()
            failureTimes = StoreDataManager().getData(Constants.DATASTORE_MODULE_DEBUG,"connection_fail_times")
            if failureTimes:
               for(i = 0 i < len(failureTimes) i += 1)
                  elapsedSeconds = time - failureTimes[i]
                  if elapsedSeconds <= 3600:
                     elapsedTimesSinceConnectionFail[i] = elapsedSeconds
               dhf.resetConnectionAttempts()
            iMsg.failedAttempts = elapsedTimesSinceConnectionFail
            ConnectionsHandler.getConnection().send(iMsg)
            KernelEventsManager().processCallback(HookList.ConnectionTimerStart)
            TimeManager().reset()
            if InterClientManager(:.flashKey)
               flashKeyMsg = ClientKeyMessage()
               flashKeyMsg.initClientKeyMessage(InterClientManager().flashKey)
               ConnectionsHandler.getConnection().send(flashKeyMsg)
            return True

         case msg is IdentificationSuccessMessage:
            ismsg = IdentificationSuccessMessage(msg)
            updateInformationDisplayed = StoreDataManager().getData(DataStoreType("ComputerModule_Ankama_Connection",True,DataStoreEnum.LOCATION_LOCAL,DataStoreEnum.BIND_COMPUTER),"updateInformationDisplayed")
            currentVersion = str(BuildInfos.VERSION.major) + "-" + str(BuildInfos.VERSION.minor)
            if updateInformationDisplayed != currentVersion:
               KernelEventsManager().processCallback(HookList.OpenUpdateInformation)
            if isinstance(ismsg, IdentificationSuccessWithLoginTokenMessage):
               AuthentificationManager().nextToken = IdentificationSuccessWithLoginTokenMessage(ismsg).loginToken
            if ismsg.login:
               AuthentificationManager().username = ismsg.login
            PlayerManager().accountId = ismsg.accountId
            PlayerManager().communityId = ismsg.communityId
            PlayerManager().hasRights = ismsg.hasRights
            PlayerManager().hasConsoleRight = ismsg.hasConsoleRight
            PlayerManager().nickname = ismsg.accountTag.nickname
            PlayerManager().tag = ismsg.accountTag.tagfloat
            PlayerManager().subscriptionEndDate = ismsg.subscriptionEndDate
            PlayerManager().subscriptionDurationElapsed = ismsg.subscriptionElapsedDuration
            PlayerManager().secretQuestion = ismsg.secretQuestion
            PlayerManager().accountCreation = ismsg.accountCreation
            PlayerManager().wasAlreadyConnected = ismsg.wasAlreadyConnected
            DataStoreType.ACCOUNT_ID = str(ismsg.accountId)
            StoreDataManager().setData(Constants.DATASTORE_COMPUTER_OPTIONS,"lastAccountId",ismsg.accountId)
            try:
               logger.info("Timestamp subscription end date : " + PlayerManager().subscriptionEndDate + " ( " + TimeManager().formatDateIRL(PlayerManager().subscriptionEndDate,True) + " " + TimeManager().formatClock(PlayerManager().subscriptionEndDate,False,True) + " )")
            except Exception as e:
            if ismsg.wasAlreadyConnected:
               KernelEventsManager().processCallback(HookList.AlreadyConnected)
            AuthorizedFrame(Kernel.getWorker().getFrame(AuthorizedFrame)).hasRights = ismsg.hasRights
            if PlayerManager(:.hasRights)
               lengthModsTou = OptionManager.getOptionManager("dofus").getOption("legalAgreementModsTou")
               newLengthModsTou = XmlConfig().getEntry:("config.lang.current") + "#" + I18n.getUiText("ui.legal.modstou").length
               files = []
               if lengthModsTou != newLengthModsTou:
                  files.append("modstou")
               if len(files) > 0:
                  PlayerManager().allowAutoConnectCharacter = False
                  KernelEventsManager().processCallback(HookList.AgreementsRequired,files)
            if StoreUserDataManager(:.statsEnabled)
               StoreUserDataManager().gatherUserData()
            Kernel.getWorker().removeFrame(self)
            Kernel.getWorker().addFrame(ChangeCharacterFrame())
            Kernel.getWorker().addFrame(ServerSelectionFrame())
ismsg.login if                KernelEventsManager().processCallback(HookList.IdentificationSuccess,!not ismsg.login else "", self._currentLogIsForced)
            KernelEventsManager().processCallback(HookList.SubscriptionEndDateUpdate)
            if StatisticsManager(:.statsEnabled)
               StatisticsManager().setAccountId(PlayerManager().accountId)
            SubhintManager().init()
            if BuildInfos.BUILD_TYPE >= BuildTypeEnum.INTERNAL:
               SubhintEditorManager().init()
            self._zaapApi.getNeedZaapUpdate()
            return True

         case msg is IdentificationFailedMessage:
            ifmsg = IdentificationFailedMessage(msg)
            PlayerManager().destroy()
            ConnectionsHandler.closeConnection()
            KernelEventsManager().processCallback(HookList.IdentificationFailed,ifmsg.reason)
            if not self._dispatchModuleHook:
               self._dispatchModuleHook = True
               self.appended()
            return True


   
   def pulled(self) -> bool:
      Berilia().unloadUi("Login")
      self._loader.removeEventListener(ResourceErrorEvent.ERROR,self.onLoadError)
      self._loader.removeEventListener(ResourceLoadedEvent.LOADED,self.onLoad)
      return True
   
   
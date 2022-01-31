from com.ankamagames.atouin.utils.dataMapProvider import DataMapProvider
from com.ankamagames.dofus.logic.common.managers.statsManager import StatsManager
from com.ankamagames.dofus.logic.common.managers.authentificationManager import AuthentificationManager
from ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import CurrentPlayedFighterManager
from ankamagames.dofus.logic.game.fight.managers.FightersStateManager import FightersStateManager
from ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.network.metadata import Metadata
from com.ankamagames.dofus.types.entities.animatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.managers.Worker import Worker
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.utils.displays.FrameIdManager import FrameIdManager
from com.ankamagames.dofus.kernel.net import ConnectionsHandler
from ankamagames.jerakine.logger.Logger import Logger
logger = Logger('kernel')

class Kernel(metaclass=Singleton):
   

   def __init__(self):
      self._worker:Worker = Worker()
      self.beingInReconection:bool = False

   def getWorker(self) -> Worker:
      return self._worker
   
   def panic(self, errorId:int = 0, panicArgs:list = None) -> None:
      self._worker.clear()
      ConnectionsHandler.closeConnection()
   
   def init(self) -> None:
      FrameIdManager()
      self._worker.clear()
      self.addInitialFrames(True)
      logger.info(f"Using protocole #{Metadata.PROTOCOL_BUILD}, built on {Metadata.PROTOCOL_DATE}")
   
   def postInit(self) -> None:
      DataMapProvider.init(AnimatedCharacter)
      WorldPathFinder.init()
   
   def reset(self, messagesToDispatchAfter:list = None, autoRetry:bool = False, reloadData:bool = False) -> None:
      StatsManager.clear()
      if not autoRetry:
         AuthentificationManager.clear()
      FightersStateManager().endFight()
      CurrentPlayedFighterManager().endFight()
      PlayedCharacterManager.clear()
      self._worker.clear()
      self.addInitialFrames(reloadData)
      self.beingInReconection = False
      if messagesToDispatchAfter is not None and len(messagesToDispatchAfter) > 0:
         for msg in messagesToDispatchAfter:
            self._worker.process(msg)
   
   def addInitialFrames(self, firstLaunch:bool = False) -> None:
      if firstLaunch:
         self._worker.addFrame(InitializationFrame())
      else:
         self._worker.addFrame(LoadingModuleFrame(True))
      if not self._worker.contains(LatencyFrame):
         self._worker.addFrame(LatencyFrame())
      if not self._worker.contains(ServerControlFrame):
         self._worker.addFrame(ServerControlFrame())
      if not self._worker.contains(AuthorizedFrame):
         self._worker.addFrame(AuthorizedFrame())
      self._worker.addFrame(DisconnectionHandlerFrame())
 
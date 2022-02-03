from time import sleep
from com.ankamagames.atouin.utils.DataMapProvider import DataMapProvider
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.common.managers.AuthentificationManager import AuthentificationManager
from com.ankamagames.dofus.logic.frames.DisconnectionHandlerFrame import DisconnectionHandlerFrame
from com.ankamagames.dofus.logic.game.fight.managers.FightersStateManager import FightersStateManager
import com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager as pc
from com.ankamagames.dofus.modules.utils.pathFinding.world.WorldPathFinder import WorldPathFinder
from com.ankamagames.dofus.network.Metadata import Metadata
from com.ankamagames.dofus.types.entities.animatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.managers.Worker import Worker
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.utils.displays.FrameIdManager import FrameIdManager
from com.ankamagames.jerakine.logger.Logger import Logger
import com.ankamagames.dofus.logic.connection.frames.AuthentificationFrame as auth
logger = Logger('kernel')



class Kernel(metaclass=Singleton):
   _worker:Worker = Worker()
   beingInReconection:bool = False

   def getWorker(self) -> Worker:
      return self._worker
   
   def panic(self, errorId:int = 0, panicArgs:list = None) -> None:
      from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
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
      import com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager as cpfm 
      StatsManager.clear()
      if not autoRetry:
         AuthentificationManager.clear()
      FightersStateManager().endFight()
      cpfm.CurrentPlayedFighterManager().endFight()
      pc.PlayedCharacterManager.clear()
      self._worker.clear()
      self.addInitialFrames(reloadData)
      self.beingInReconection = False
      if messagesToDispatchAfter is not None and len(messagesToDispatchAfter) > 0:
         for msg in messagesToDispatchAfter:
            self._worker.process(msg)
   
   def addInitialFrames(self, firstLaunch:bool = False) -> None:
      self.getWorker().addFrame(auth.AuthentificationFrame())
      #Kernel().getWorker().addFrame(QueueFrame())
      #Kernel().getWorker().addFrame(GameStartingFrame())
      # if not self._worker.contains(LatencyFrame):
      #    self._worker.addFrame(LatencyFrame())
      # if not self._worker.contains(ServerControlFrame):
      #    self._worker.addFrame(ServerControlFrame())
      # if not self._worker.contains(AuthorizedFrame):
      #    self._worker.addFrame(AuthorizedFrame())
      self._worker.addFrame(DisconnectionHandlerFrame())
 

if __name__ == '__main__':
   import com.ankamagames.dofus.kernel.Kernel as krnl
   import com.ankamagames.dofus.logic.common.managers.AuthentificationManager as auth

   krnl.Kernel().init()
   PORT = 5555
   AUTH_SERVER = "54.76.16.121" 
   auth.AuthentificationManager().setCredentials("kmajdoub", "rMrTXHA4*")
   connh.ConnectionsHandler.connectToLoginServer(AUTH_SERVER, PORT)
   sleep(20)
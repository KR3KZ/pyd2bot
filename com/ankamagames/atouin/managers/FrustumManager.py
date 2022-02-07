from com.ankamagames.atouin.data.map.map import Map
from com.ankamagames.atouin.managers.MapDisplayManager import MapDisplayManager
from com.ankamagames.atouin.messages.AdjacentMapClickMessage import AdjacentMapClickMessage
from com.ankamagames.atouin.messages.CellClickMessage import CellClickMessage
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.types.enums.DirectionsEnum import DirectionsEnum
logger = Logger(__name__)


class FrustumManager:
   
   @classmethod
   def changeMapToDirection(cls, direction:DirectionsEnum) -> None:
      currentMap:Map = MapDisplayManager().dataMap
      destMapId = currentMap.getNeighborIdFromDirection(direction)
      playedCharacterManager = PlayedCharacterManager()
      playedEntity = DofusEntities.getEntity(playedCharacterManager.id)
      playedEntityCellId:int = playedEntity.position.cellId
      cellId = currentMap.cellOutTowards(playedEntityCellId, direction)
      if cellId is not None:
         logger.debug('FrustumManager.changeMapToDirection: cellId = ' + str(cellId))
         cls.sendClickAdjacentMsg(destMapId, cellId)
      else:
         logger.warn("Impossible to change map to direction " + str(direction))
   
   @classmethod
   def sendClickAdjacentMsg(cls, mapId:float, cellId:int) -> None:
      msg:AdjacentMapClickMessage = AdjacentMapClickMessage()
      msg.cellId = cellId
      msg.adjacentMapId = mapId
      Kernel().getWorker().process(msg)
   
   @classmethod
   def sendCellClickMsg(cls, mapId:float, cellId:int) -> None:
      msg:CellClickMessage = CellClickMessage()
      msg.cellId = cellId
      msg.id = mapId
      Kernel().getWorker().process(msg)
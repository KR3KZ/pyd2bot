from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep
    from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntFlag import TreasureHuntFlag
    


class TreasureHuntMessage(NetworkMessage):
    questType:int
    startMapId:int
    knownStepsList:list['TreasureHuntStep']
    totalStepCount:int
    checkPointCurrent:int
    checkPointTotal:int
    availableRetryCount:int
    flags:list['TreasureHuntFlag']
    

    def init(self, questType:int, startMapId:int, knownStepsList:list['TreasureHuntStep'], totalStepCount:int, checkPointCurrent:int, checkPointTotal:int, availableRetryCount:int, flags:list['TreasureHuntFlag']):
        self.questType = questType
        self.startMapId = startMapId
        self.knownStepsList = knownStepsList
        self.totalStepCount = totalStepCount
        self.checkPointCurrent = checkPointCurrent
        self.checkPointTotal = checkPointTotal
        self.availableRetryCount = availableRetryCount
        self.flags = flags
        
        super().__init__()
    
    
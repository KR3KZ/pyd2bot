from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntFlag import TreasureHuntFlag


@dataclass
class TreasureHuntMessage(NetworkMessage):
    questType:int
    startMapId:int
    knownStepsList:list[TreasureHuntStep]
    totalStepCount:int
    checkPointCurrent:int
    checkPointTotal:int
    availableRetryCount:int
    flags:list[TreasureHuntFlag]
    
    
    def __post_init__(self):
        super().__init__()
    
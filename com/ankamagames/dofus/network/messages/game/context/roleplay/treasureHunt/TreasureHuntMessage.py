from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntFlag import TreasureHuntFlag


class TreasureHuntMessage(NetworkMessage):
    protocolId = 4513
    questType:int
    startMapId:int
    knownStepsList:TreasureHuntStep
    totalStepCount:int
    checkPointCurrent:int
    checkPointTotal:int
    availableRetryCount:int
    flags:TreasureHuntFlag
    
    

from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


class SpawnCompanionInformation(SpawnInformation):
    protocolId = 8892
    modelId:int
    level:int
    summonerId:int
    ownerId:int
    
    

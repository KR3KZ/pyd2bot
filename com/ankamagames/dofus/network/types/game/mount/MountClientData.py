from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class MountClientData(NetworkMessage):
    protocolId = 9874
    id:float
    model:int
    ancestor:list[int]
    behaviors:list[int]
    name:str
    ownerId:int
    experience:float
    experienceForLevel:float
    experienceForNextLevel:float
    level:int
    maxPods:int
    stamina:int
    staminaMax:int
    maturity:int
    maturityForAdult:int
    energy:int
    energyMax:int
    serenity:int
    aggressivityMax:int
    serenityMax:int
    love:int
    loveMax:int
    fecondationTime:int
    boostLimiter:int
    boostMax:float
    reproductionCount:int
    reproductionCountMax:int
    harnessGID:int
    effectList:list[ObjectEffectInteger]
    

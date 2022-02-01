from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class MountClientData(INetworkMessage):
    protocolId = 9874
    id:int
    model:int
    ancestor:int
    behaviors:int
    name:str
    ownerId:int
    experience:int
    experienceForLevel:int
    experienceForNextLevel:int
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
    boostMax:int
    reproductionCount:int
    reproductionCountMax:int
    harnessGID:int
    effectList:ObjectEffectInteger
    sex:bool
    isRideable:bool
    isWild:bool
    isFecondationReady:bool
    useHarnessColors:bool
    
    

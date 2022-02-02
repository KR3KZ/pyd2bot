from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


@dataclass
class MountClientData(NetworkMessage):
    id:int
    model:int
    ancestor:list[int]
    behaviors:list[int]
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
    effectList:list[ObjectEffectInteger]
    sex:bool
    isRideable:bool
    isWild:bool
    isFecondationReady:bool
    useHarnessColors:bool
    
    
    def __post_init__(self):
        super().__init__()
    
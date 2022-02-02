from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ActorRestrictionsInformations(NetworkMessage):
    cantBeAggressed:bool
    cantBeChallenged:bool
    cantTrade:bool
    cantBeAttackedByMutant:bool
    cantRun:bool
    forceSlowWalk:bool
    cantMinimize:bool
    cantMove:bool
    cantAggress:bool
    cantChallenge:bool
    cantExchange:bool
    cantAttack:bool
    cantChat:bool
    cantBeMerchant:bool
    cantUseObject:bool
    cantUseTaxCollector:bool
    cantUseInteractive:bool
    cantSpeakToNPC:bool
    cantChangeZone:bool
    cantAttackMonster:bool
    
    
    def __post_init__(self):
        super().__init__()
    
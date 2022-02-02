from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


@dataclass
class FightDispellableEffectExtendedInformations(NetworkMessage):
    actionId:int
    sourceId:int
    effect:AbstractFightDispellableEffect
    
    
    def __post_init__(self):
        super().__init__()
    
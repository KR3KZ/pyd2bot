from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightDispellableEffectExtendedInformations(NetworkMessage):
    actionId:int
    sourceId:int
    effect:AbstractFightDispellableEffect
    
    

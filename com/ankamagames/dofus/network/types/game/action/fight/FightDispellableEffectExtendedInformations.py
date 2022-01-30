from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightDispellableEffectExtendedInformations(NetworkMessage):
    protocolId = 8005
    actionId:int
    sourceId:int
    effect:AbstractFightDispellableEffect
    
    

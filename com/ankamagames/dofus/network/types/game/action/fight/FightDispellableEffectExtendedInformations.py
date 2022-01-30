from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightDispellableEffectExtendedInformations(INetworkMessage):
    protocolId = 8005
    actionId:int
    sourceId:int
    effect:AbstractFightDispellableEffect
    
    

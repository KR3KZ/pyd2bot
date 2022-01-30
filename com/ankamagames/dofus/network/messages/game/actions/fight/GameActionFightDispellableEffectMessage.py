from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class GameActionFightDispellableEffectMessage(AbstractGameActionMessage):
    protocolId = 9416
    effect:AbstractFightDispellableEffect
    

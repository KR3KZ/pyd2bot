from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameContextSummonsInformation import GameContextSummonsInformation


class GameActionFightMultipleSummonMessage(AbstractGameActionMessage):
    protocolId = 710
    summons:list[GameContextSummonsInformation]
    

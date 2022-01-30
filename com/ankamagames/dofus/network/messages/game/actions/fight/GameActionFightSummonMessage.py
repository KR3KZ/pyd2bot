from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


class GameActionFightSummonMessage(AbstractGameActionMessage):
    protocolId = 2879
    summons:list[GameFightFighterInformations]
    

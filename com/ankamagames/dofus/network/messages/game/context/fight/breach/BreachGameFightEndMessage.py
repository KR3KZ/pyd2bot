from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import GameFightEndMessage


class BreachGameFightEndMessage(GameFightEndMessage):
    protocolId = 7323
    budget:int
    

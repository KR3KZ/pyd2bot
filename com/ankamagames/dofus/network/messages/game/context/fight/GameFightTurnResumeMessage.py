from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import GameFightTurnStartMessage


class GameFightTurnResumeMessage(GameFightTurnStartMessage):
    protocolId = 9827
    remainingTime:int
    

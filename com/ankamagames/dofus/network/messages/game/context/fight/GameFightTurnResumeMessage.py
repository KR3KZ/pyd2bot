from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import GameFightTurnStartMessage


class GameFightTurnResumeMessage(GameFightTurnStartMessage):
    remainingTime:int
    

    def init(self, remainingTime:int, id:int, waitTime:int):
        self.remainingTime = remainingTime
        
        super().__init__(id, waitTime)
    
    
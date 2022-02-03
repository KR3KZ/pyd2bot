from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntDigRequestAnswerMessage import TreasureHuntDigRequestAnswerMessage


class TreasureHuntDigRequestAnswerFailedMessage(TreasureHuntDigRequestAnswerMessage):
    wrongFlagCount:int
    

    def init(self, wrongFlagCount:int, questType:int, result:int):
        self.wrongFlagCount = wrongFlagCount
        
        super().__init__(questType, result)
    
    
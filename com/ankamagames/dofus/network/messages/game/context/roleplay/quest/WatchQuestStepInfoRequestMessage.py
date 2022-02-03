from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepInfoRequestMessage import QuestStepInfoRequestMessage


class WatchQuestStepInfoRequestMessage(QuestStepInfoRequestMessage):
    playerId:int
    

    def init(self, playerId:int, questId:int):
        self.playerId = playerId
        
        super().__init__(questId)
    
    
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepInfoMessage import QuestStepInfoMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
    


class WatchQuestStepInfoMessage(QuestStepInfoMessage):
    playerId:int
    

    def init(self, playerId:int, infos:'QuestActiveInformations'):
        self.playerId = playerId
        
        super().__init__(infos)
    
    
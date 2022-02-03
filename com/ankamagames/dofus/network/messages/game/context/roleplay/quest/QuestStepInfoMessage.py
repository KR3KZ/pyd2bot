from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
    


class QuestStepInfoMessage(NetworkMessage):
    infos:'QuestActiveInformations'
    

    def init(self, infos:'QuestActiveInformations'):
        self.infos = infos
        
        super().__init__()
    
    
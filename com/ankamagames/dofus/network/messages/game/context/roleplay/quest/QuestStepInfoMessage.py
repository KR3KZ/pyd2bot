from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


@dataclass
class QuestStepInfoMessage(NetworkMessage):
    infos:QuestActiveInformations
    
    
    def __post_init__(self):
        super().__init__()
    
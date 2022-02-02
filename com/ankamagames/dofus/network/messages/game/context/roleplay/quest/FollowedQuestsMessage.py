from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveDetailedInformations import QuestActiveDetailedInformations


@dataclass
class FollowedQuestsMessage(NetworkMessage):
    quests:list[QuestActiveDetailedInformations]
    
    
    def __post_init__(self):
        super().__init__()
    
from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class UnfollowQuestObjectiveRequestMessage(NetworkMessage):
    questId:int
    objectiveId:int
    
    
    def __post_init__(self):
        super().__init__()
    
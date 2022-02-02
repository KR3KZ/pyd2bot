from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class QuestObjectiveInformations(NetworkMessage):
    objectiveId:int
    objectiveStatus:bool
    dialogParams:list[str]
    
    
    def __post_init__(self):
        super().__init__()
    
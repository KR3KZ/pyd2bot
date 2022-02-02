from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class NpcDialogQuestionMessage(NetworkMessage):
    messageId:int
    dialogParams:list[str]
    visibleReplies:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    
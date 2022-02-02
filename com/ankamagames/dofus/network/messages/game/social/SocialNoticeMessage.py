from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SocialNoticeMessage(NetworkMessage):
    content:str
    timestamp:int
    memberId:int
    memberName:str
    
    
    def __post_init__(self):
        super().__init__()
    
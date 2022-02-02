from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class NicknameChoiceRequestMessage(NetworkMessage):
    nickname:str
    
    
    def __post_init__(self):
        super().__init__()
    
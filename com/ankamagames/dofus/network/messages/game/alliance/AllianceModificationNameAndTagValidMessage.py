from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AllianceModificationNameAndTagValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    
    
    def __post_init__(self):
        super().__init__()
    
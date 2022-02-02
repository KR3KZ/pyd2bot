from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class CharacterDeletionRequestMessage(NetworkMessage):
    characterId:int
    secretAnswerHash:str
    
    
    def __post_init__(self):
        super().__init__()
    
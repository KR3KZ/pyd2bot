from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class CharacterExperienceGainMessage(NetworkMessage):
    experienceCharacter:int
    experienceMount:int
    experienceGuild:int
    experienceIncarnation:int
    
    
    def __post_init__(self):
        super().__init__()
    
from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


@dataclass
class AcquaintanceOnlineInformation(AcquaintanceInformation):
    playerId:int
    playerName:str
    moodSmileyId:int
    status:PlayerStatus
    
    
    def __post_init__(self):
        super().__init__()
    
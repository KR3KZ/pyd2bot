from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


@dataclass
class PlayerStatusUpdateRequestMessage(NetworkMessage):
    status:PlayerStatus
    
    
    def __post_init__(self):
        super().__init__()
    
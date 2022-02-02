from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


@dataclass
class ApplicationPlayerInformation(NetworkMessage):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    accountId:int
    accountTag:str
    accountNickname:str
    status:PlayerStatus
    
    
    def __post_init__(self):
        super().__init__()
    
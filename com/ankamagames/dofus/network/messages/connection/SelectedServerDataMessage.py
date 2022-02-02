from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SelectedServerDataMessage(NetworkMessage):
    serverId:int
    address:str
    ports:list[int]
    canCreateNewCharacter:bool
    ticket:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    
from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


@dataclass
class ServersListMessage(NetworkMessage):
    servers:list[GameServerInformations]
    alreadyConnectedToServerId:int
    canCreateNewCharacter:bool
    
    
    def __post_init__(self):
        super().__init__()
    
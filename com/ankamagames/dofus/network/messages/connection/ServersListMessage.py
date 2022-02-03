from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
    


class ServersListMessage(NetworkMessage):
    servers:list['GameServerInformations']
    alreadyConnectedToServerId:int
    canCreateNewCharacter:bool
    

    def init(self, servers_:list['GameServerInformations'], alreadyConnectedToServerId_:int, canCreateNewCharacter_:bool):
        self.servers = servers_
        self.alreadyConnectedToServerId = alreadyConnectedToServerId_
        self.canCreateNewCharacter = canCreateNewCharacter_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
    


class ServersListMessage(NetworkMessage):
    servers:list['GameServerInformations']
    alreadyConnectedToServerId:int
    canCreateNewCharacter:bool
    

    def init(self, servers:list['GameServerInformations'], alreadyConnectedToServerId:int, canCreateNewCharacter:bool):
        self.servers = servers
        self.alreadyConnectedToServerId = alreadyConnectedToServerId
        self.canCreateNewCharacter = canCreateNewCharacter
        
        super().__init__()
    
    
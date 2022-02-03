from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
    


class ServerStatusUpdateMessage(NetworkMessage):
    server:'GameServerInformations'
    

    def init(self, server:'GameServerInformations'):
        self.server = server
        
        super().__init__()
    
    
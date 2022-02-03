from com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import SelectedServerDataMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
    


class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
    servers:list['GameServerInformations']
    

    def init(self, servers:list['GameServerInformations'], serverId:int, address:str, ports:list[int], canCreateNewCharacter:bool, ticket:list[int]):
        self.servers = servers
        
        super().__init__(serverId, address, ports, canCreateNewCharacter, ticket)
    
    
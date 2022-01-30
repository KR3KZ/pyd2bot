from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


class ServerStatusUpdateMessage(NetworkMessage):
    protocolId = 1411
    server:GameServerInformations
    

from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


class ServerStatusUpdateMessage(INetworkMessage):
    protocolId = 1411
    server:GameServerInformations
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


class ServerStatusUpdateMessage(NetworkMessage):
    server:GameServerInformations
    
    

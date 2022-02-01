from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


class ServersListMessage(INetworkMessage):
    protocolId = 786
    servers:GameServerInformations
    alreadyConnectedToServerId:int
    canCreateNewCharacter:bool
    
    

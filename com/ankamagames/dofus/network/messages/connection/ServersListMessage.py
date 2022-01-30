from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


class ServersListMessage(NetworkMessage):
    protocolId = 786
    servers:list[GameServerInformations]
    alreadyConnectedToServerId:int
    canCreateNewCharacter:bool
    

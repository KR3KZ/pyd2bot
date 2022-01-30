from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ConsoleCommandsListMessage(NetworkMessage):
    protocolId = 5611
    aliases:str
    args:str
    descriptions:str
    

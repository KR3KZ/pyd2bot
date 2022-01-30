from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ConsoleCommandsListMessage(INetworkMessage):
    protocolId = 5611
    aliases:str
    args:str
    descriptions:str
    
    

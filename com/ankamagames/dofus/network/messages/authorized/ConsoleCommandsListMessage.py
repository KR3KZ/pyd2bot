from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ConsoleCommandsListMessage(INetworkMessage):
    protocolId = 5611
    aliases:str
    args:str
    descriptions:str
    
    

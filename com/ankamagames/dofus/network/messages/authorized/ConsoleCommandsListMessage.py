from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ConsoleCommandsListMessage(NetworkMessage):
    aliases:list[str]
    args:list[str]
    descriptions:list[str]
    
    

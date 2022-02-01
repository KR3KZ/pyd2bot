from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachCharactersMessage(INetworkMessage):
    protocolId = 6300
    characters:int
    
    

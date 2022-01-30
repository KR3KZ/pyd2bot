from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachCharactersMessage(INetworkMessage):
    protocolId = 6300
    characters:int
    
    

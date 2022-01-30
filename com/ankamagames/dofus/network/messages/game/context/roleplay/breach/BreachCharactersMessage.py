from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachCharactersMessage(NetworkMessage):
    protocolId = 6300
    characters:int
    
    

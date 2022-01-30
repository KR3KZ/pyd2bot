from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameActionSpamMessage(NetworkMessage):
    protocolId = 6276
    cells:int
    
    

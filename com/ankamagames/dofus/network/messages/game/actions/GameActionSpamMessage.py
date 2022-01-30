from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameActionSpamMessage(INetworkMessage):
    protocolId = 6276
    cells:int
    
    

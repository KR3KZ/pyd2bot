from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachEnterMessage(INetworkMessage):
    protocolId = 6485
    owner:int
    
    

from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachKickRequestMessage(INetworkMessage):
    protocolId = 2909
    target:int
    
    

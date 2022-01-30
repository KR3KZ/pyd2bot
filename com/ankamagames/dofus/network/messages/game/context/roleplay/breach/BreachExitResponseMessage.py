from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachExitResponseMessage(INetworkMessage):
    protocolId = 7143
    exited:bool
    
    

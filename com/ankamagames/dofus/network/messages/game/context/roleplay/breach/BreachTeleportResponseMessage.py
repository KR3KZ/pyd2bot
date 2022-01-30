from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachTeleportResponseMessage(INetworkMessage):
    protocolId = 4766
    teleported:bool
    
    

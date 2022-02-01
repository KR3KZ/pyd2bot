from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachTeleportResponseMessage(INetworkMessage):
    protocolId = 4766
    teleported:bool
    
    

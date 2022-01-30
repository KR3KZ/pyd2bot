from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismFightStateUpdateMessage(INetworkMessage):
    protocolId = 7379
    state:int
    
    

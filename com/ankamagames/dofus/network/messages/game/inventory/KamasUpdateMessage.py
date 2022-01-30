from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class KamasUpdateMessage(INetworkMessage):
    protocolId = 4370
    kamasTotal:int
    
    

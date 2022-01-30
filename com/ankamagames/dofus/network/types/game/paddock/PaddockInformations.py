from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockInformations(INetworkMessage):
    protocolId = 1965
    maxOutdoorMount:int
    maxItems:int
    
    

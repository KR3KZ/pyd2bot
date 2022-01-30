from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockInformations(NetworkMessage):
    protocolId = 1965
    maxOutdoorMount:int
    maxItems:int
    

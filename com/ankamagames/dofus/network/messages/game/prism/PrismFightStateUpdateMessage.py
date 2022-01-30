from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismFightStateUpdateMessage(NetworkMessage):
    protocolId = 7379
    state:int
    

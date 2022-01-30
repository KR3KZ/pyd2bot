from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismUseRequestMessage(NetworkMessage):
    protocolId = 8164
    moduleToUse:int
    

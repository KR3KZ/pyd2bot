from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismUseRequestMessage(INetworkMessage):
    protocolId = 8164
    moduleToUse:int
    
    

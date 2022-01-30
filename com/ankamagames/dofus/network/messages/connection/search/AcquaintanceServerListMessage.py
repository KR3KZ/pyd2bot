from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AcquaintanceServerListMessage(INetworkMessage):
    protocolId = 8752
    servers:int
    
    

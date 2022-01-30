from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NumericWhoIsRequestMessage(INetworkMessage):
    protocolId = 4159
    playerId:int
    
    

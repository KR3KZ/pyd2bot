from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NumericWhoIsMessage(INetworkMessage):
    protocolId = 7592
    playerId:int
    accountId:int
    
    

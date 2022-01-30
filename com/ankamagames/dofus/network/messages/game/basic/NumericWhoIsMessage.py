from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NumericWhoIsMessage(NetworkMessage):
    protocolId = 7592
    playerId:int
    accountId:int
    

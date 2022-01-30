from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NumericWhoIsRequestMessage(NetworkMessage):
    protocolId = 4159
    playerId:int
    

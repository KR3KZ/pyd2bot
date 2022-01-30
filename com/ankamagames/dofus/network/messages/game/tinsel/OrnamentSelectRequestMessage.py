from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class OrnamentSelectRequestMessage(NetworkMessage):
    protocolId = 4149
    ornamentId:int
    

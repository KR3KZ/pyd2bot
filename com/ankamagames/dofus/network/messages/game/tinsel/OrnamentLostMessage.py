from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class OrnamentLostMessage(NetworkMessage):
    protocolId = 94
    ornamentId:int
    
    

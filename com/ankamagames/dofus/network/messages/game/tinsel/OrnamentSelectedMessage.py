from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class OrnamentSelectedMessage(NetworkMessage):
    protocolId = 7637
    ornamentId:int
    
    

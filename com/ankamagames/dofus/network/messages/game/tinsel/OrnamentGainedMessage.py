from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class OrnamentGainedMessage(NetworkMessage):
    protocolId = 3920
    ornamentId:int
    

from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceKickRequestMessage(NetworkMessage):
    protocolId = 1648
    kickedId:int
    

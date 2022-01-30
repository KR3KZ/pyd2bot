from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildGetInformationsMessage(NetworkMessage):
    protocolId = 5805
    infoType:int
    
    

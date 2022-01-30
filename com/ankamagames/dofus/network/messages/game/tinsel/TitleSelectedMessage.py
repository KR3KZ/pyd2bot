from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TitleSelectedMessage(NetworkMessage):
    protocolId = 8922
    titleId:int
    

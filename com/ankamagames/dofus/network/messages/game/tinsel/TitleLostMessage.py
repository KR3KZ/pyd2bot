from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TitleLostMessage(NetworkMessage):
    protocolId = 1427
    titleId:int
    
    

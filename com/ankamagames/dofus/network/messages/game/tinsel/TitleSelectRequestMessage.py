from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TitleSelectRequestMessage(NetworkMessage):
    protocolId = 8025
    titleId:int
    

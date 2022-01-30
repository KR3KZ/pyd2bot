from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TitleGainedMessage(NetworkMessage):
    protocolId = 3386
    titleId:int
    

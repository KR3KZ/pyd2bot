from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TitleSelectErrorMessage(NetworkMessage):
    protocolId = 2014
    reason:int
    

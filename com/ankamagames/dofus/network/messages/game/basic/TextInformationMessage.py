from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TextInformationMessage(NetworkMessage):
    protocolId = 3712
    msgType:int
    msgId:int
    parameters:list[str]
    

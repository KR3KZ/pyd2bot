from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TextInformationMessage(INetworkMessage):
    protocolId = 3712
    msgType:int
    msgId:int
    parameters:str
    
    

from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TextInformationMessage(INetworkMessage):
    protocolId = 3712
    msgType:int
    msgId:int
    parameters:str
    
    

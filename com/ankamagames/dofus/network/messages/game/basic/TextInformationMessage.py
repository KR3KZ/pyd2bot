from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TextInformationMessage(NetworkMessage):
    msgType:int
    msgId:int
    parameters:list[str]
    
    

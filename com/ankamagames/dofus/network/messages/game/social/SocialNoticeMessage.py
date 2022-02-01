from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SocialNoticeMessage(INetworkMessage):
    protocolId = 8560
    content:str
    timestamp:int
    memberId:int
    memberName:str
    
    

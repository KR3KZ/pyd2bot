from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SocialNoticeMessage(NetworkMessage):
    content:str
    timestamp:int
    memberId:int
    memberName:str
    
    

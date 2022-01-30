from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SocialNoticeMessage(NetworkMessage):
    protocolId = 8560
    content:str
    timestamp:int
    memberId:int
    memberName:str
    
    

from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SocialNoticeMessage(NetworkMessage):
    content:str
    timestamp:int
    memberId:int
    memberName:str
    

    def init(self, content:str, timestamp:int, memberId:int, memberName:str):
        self.content = content
        self.timestamp = timestamp
        self.memberId = memberId
        self.memberName = memberName
        
        super().__init__()
    
    
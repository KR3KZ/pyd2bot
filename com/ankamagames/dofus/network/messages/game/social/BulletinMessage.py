from com.ankamagames.dofus.network.messages.game.social.SocialNoticeMessage import SocialNoticeMessage


class BulletinMessage(SocialNoticeMessage):
    lastNotifiedTimestamp:int
    

    def init(self, lastNotifiedTimestamp:int, content:str, timestamp:int, memberId:int, memberName:str):
        self.lastNotifiedTimestamp = lastNotifiedTimestamp
        
        super().__init__(content, timestamp, memberId, memberName)
    
    
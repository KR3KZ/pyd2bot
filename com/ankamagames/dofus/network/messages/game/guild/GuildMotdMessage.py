from com.ankamagames.dofus.network.messages.game.social.SocialNoticeMessage import SocialNoticeMessage


class GuildMotdMessage(SocialNoticeMessage):
    

    def init(self, content:str, timestamp:int, memberId:int, memberName:str):
        
        super().__init__(content, timestamp, memberId, memberName)
    
    
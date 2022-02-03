from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class GuildBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    content:str
    notifyMembers:bool
    

    def init(self, content:str, notifyMembers:bool):
        self.content = content
        self.notifyMembers = notifyMembers
        
        super().__init__()
    
    
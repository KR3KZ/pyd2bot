from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetErrorMessage import SocialNoticeSetErrorMessage


class AllianceBulletinSetErrorMessage(SocialNoticeSetErrorMessage):
    

    def init(self, reason:int):
        
        super().__init__(reason)
    
    
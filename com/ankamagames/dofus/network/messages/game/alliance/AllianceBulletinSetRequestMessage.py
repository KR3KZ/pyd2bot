from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class AllianceBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    content:str
    notifyMembers:bool
    
    

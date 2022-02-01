from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class GuildBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    content:str
    notifyMembers:bool
    
    

from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class GuildBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    protocolId = 7121
    content:str
    notifyMembers:bool
    

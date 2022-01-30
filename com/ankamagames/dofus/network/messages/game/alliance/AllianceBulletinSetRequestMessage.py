from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class AllianceBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    protocolId = 645
    content:str
    notifyMembers:bool
    

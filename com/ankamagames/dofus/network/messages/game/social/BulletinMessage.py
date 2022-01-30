from com.ankamagames.dofus.network.messages.game.social.SocialNoticeMessage import SocialNoticeMessage


class BulletinMessage(SocialNoticeMessage):
    protocolId = 9541
    lastNotifiedTimestamp:int
    

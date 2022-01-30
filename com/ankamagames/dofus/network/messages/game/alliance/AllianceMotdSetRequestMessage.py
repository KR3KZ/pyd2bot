from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class AllianceMotdSetRequestMessage(SocialNoticeSetRequestMessage):
    protocolId = 3707
    content:str
    

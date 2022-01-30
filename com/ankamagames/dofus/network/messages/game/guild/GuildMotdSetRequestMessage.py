from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class GuildMotdSetRequestMessage(SocialNoticeSetRequestMessage):
    protocolId = 3391
    content:str
    

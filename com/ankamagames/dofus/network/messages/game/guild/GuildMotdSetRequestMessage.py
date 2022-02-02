from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


@dataclass
class GuildMotdSetRequestMessage(SocialNoticeSetRequestMessage):
    content:str
    
    
    def __post_init__(self):
        super().__init__()
    
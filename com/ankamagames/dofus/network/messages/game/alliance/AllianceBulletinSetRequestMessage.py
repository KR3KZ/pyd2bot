from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


@dataclass
class AllianceBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    content:str
    notifyMembers:bool
    
    
    def __post_init__(self):
        super().__init__()
    
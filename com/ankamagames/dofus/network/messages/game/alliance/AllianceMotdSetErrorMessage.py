from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetErrorMessage import SocialNoticeSetErrorMessage


@dataclass
class AllianceMotdSetErrorMessage(SocialNoticeSetErrorMessage):
    
    
    def __post_init__(self):
        super().__init__()
    
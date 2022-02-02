from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.social.BulletinMessage import BulletinMessage


@dataclass
class AllianceBulletinMessage(BulletinMessage):
    
    
    def __post_init__(self):
        super().__init__()
    
from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.social.BulletinMessage import BulletinMessage


@dataclass
class GuildBulletinMessage(BulletinMessage):
    
    
    def __post_init__(self):
        super().__init__()
    
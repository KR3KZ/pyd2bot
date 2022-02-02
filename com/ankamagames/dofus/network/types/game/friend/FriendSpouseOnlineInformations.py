from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations


@dataclass
class FriendSpouseOnlineInformations(FriendSpouseInformations):
    mapId:int
    subAreaId:int
    inFight:bool
    followSpouse:bool
    
    
    def __post_init__(self):
        super().__init__()
    
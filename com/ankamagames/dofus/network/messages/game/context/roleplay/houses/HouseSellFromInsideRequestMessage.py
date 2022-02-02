from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HouseSellRequestMessage import HouseSellRequestMessage


@dataclass
class HouseSellFromInsideRequestMessage(HouseSellRequestMessage):
    
    
    def __post_init__(self):
        super().__init__()
    
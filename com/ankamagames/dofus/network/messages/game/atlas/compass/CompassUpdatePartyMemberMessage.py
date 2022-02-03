from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates
    


class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
    memberId:int
    active:bool
    

    def init(self, memberId:int, active:bool, type:int, coords:'MapCoordinates'):
        self.memberId = memberId
        self.active = active
        
        super().__init__(type, coords)
    
    
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates
    


class CompassUpdatePvpSeekMessage(CompassUpdateMessage):
    memberId:int
    memberName:str
    

    def init(self, memberId:int, memberName:str, type:int, coords:'MapCoordinates'):
        self.memberId = memberId
        self.memberName = memberName
        
        super().__init__(type, coords)
    
    
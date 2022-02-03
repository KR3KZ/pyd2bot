from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations
    


class SetCharacterRestrictionsMessage(NetworkMessage):
    actorId:int
    restrictions:'ActorRestrictionsInformations'
    

    def init(self, actorId:int, restrictions:'ActorRestrictionsInformations'):
        self.actorId = actorId
        self.restrictions = restrictions
        
        super().__init__()
    
    
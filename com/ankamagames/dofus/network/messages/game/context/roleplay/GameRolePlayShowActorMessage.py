from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
    


class GameRolePlayShowActorMessage(NetworkMessage):
    informations:'GameRolePlayActorInformations'
    

    def init(self, informations:'GameRolePlayActorInformations'):
        self.informations = informations
        
        super().__init__()
    
    
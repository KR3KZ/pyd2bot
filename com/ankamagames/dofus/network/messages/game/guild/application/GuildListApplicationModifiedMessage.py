from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation
    


class GuildListApplicationModifiedMessage(NetworkMessage):
    apply:'GuildApplicationInformation'
    state:int
    playerId:int
    

    def init(self, apply:'GuildApplicationInformation', state:int, playerId:int):
        self.apply = apply
        self.state = state
        self.playerId = playerId
        
        super().__init__()
    
    
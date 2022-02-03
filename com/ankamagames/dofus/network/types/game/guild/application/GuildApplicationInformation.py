from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.application.ApplicationPlayerInformation import ApplicationPlayerInformation
    


class GuildApplicationInformation(NetworkMessage):
    playerInfo:'ApplicationPlayerInformation'
    applyText:str
    creationDate:int
    

    def init(self, playerInfo:'ApplicationPlayerInformation', applyText:str, creationDate:int):
        self.playerInfo = playerInfo
        self.applyText = applyText
        self.creationDate = creationDate
        
        super().__init__()
    
    
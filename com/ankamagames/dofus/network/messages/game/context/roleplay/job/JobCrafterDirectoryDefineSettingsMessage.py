from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings
    


class JobCrafterDirectoryDefineSettingsMessage(NetworkMessage):
    settings:'JobCrafterDirectorySettings'
    

    def init(self, settings:'JobCrafterDirectorySettings'):
        self.settings = settings
        
        super().__init__()
    
    
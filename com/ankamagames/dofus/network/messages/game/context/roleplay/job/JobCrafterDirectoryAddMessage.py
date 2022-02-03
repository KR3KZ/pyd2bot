from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry
    


class JobCrafterDirectoryAddMessage(NetworkMessage):
    listEntry:'JobCrafterDirectoryListEntry'
    

    def init(self, listEntry:'JobCrafterDirectoryListEntry'):
        self.listEntry = listEntry
        
        super().__init__()
    
    
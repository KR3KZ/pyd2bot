from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry
    


class JobCrafterDirectoryListMessage(NetworkMessage):
    listEntries:list['JobCrafterDirectoryListEntry']
    

    def init(self, listEntries:list['JobCrafterDirectoryListEntry']):
        self.listEntries = listEntries
        
        super().__init__()
    
    
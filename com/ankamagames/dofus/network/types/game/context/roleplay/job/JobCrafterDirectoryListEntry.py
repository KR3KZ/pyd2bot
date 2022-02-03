from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
    


class JobCrafterDirectoryListEntry(NetworkMessage):
    playerInfo:'JobCrafterDirectoryEntryPlayerInfo'
    jobInfo:'JobCrafterDirectoryEntryJobInfo'
    

    def init(self, playerInfo:'JobCrafterDirectoryEntryPlayerInfo', jobInfo:'JobCrafterDirectoryEntryJobInfo'):
        self.playerInfo = playerInfo
        self.jobInfo = jobInfo
        
        super().__init__()
    
    
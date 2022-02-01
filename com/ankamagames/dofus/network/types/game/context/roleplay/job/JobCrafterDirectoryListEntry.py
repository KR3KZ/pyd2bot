from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo


class JobCrafterDirectoryListEntry(NetworkMessage):
    playerInfo:JobCrafterDirectoryEntryPlayerInfo
    jobInfo:JobCrafterDirectoryEntryJobInfo
    
    

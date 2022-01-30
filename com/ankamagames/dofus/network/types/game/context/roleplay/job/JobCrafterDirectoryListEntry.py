from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo


class JobCrafterDirectoryListEntry(NetworkMessage):
    protocolId = 3897
    playerInfo:JobCrafterDirectoryEntryPlayerInfo
    jobInfo:JobCrafterDirectoryEntryJobInfo
    
    

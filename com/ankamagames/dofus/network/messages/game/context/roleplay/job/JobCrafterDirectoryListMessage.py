from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry


class JobCrafterDirectoryListMessage(NetworkMessage):
    protocolId = 7620
    listEntries:list[JobCrafterDirectoryListEntry]
    

from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry


class JobCrafterDirectoryAddMessage(NetworkMessage):
    protocolId = 1829
    listEntry:JobCrafterDirectoryListEntry
    
    

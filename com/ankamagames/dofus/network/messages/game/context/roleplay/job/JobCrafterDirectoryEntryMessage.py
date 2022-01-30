from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class JobCrafterDirectoryEntryMessage(NetworkMessage):
    protocolId = 3827
    playerInfo:JobCrafterDirectoryEntryPlayerInfo
    jobInfoList:list[JobCrafterDirectoryEntryJobInfo]
    playerLook:EntityLook
    

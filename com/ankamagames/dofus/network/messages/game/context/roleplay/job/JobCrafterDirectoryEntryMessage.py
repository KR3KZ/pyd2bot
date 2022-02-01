from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class JobCrafterDirectoryEntryMessage(NetworkMessage):
    playerInfo:JobCrafterDirectoryEntryPlayerInfo
    jobInfoList:list[JobCrafterDirectoryEntryJobInfo]
    playerLook:EntityLook
    
    

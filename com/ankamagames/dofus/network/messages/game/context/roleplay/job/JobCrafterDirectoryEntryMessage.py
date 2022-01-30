from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class JobCrafterDirectoryEntryMessage(INetworkMessage):
    protocolId = 3827
    playerInfo:JobCrafterDirectoryEntryPlayerInfo
    jobInfoList:JobCrafterDirectoryEntryJobInfo
    playerLook:EntityLook
    
    

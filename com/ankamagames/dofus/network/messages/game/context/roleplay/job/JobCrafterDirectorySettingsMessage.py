from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


class JobCrafterDirectorySettingsMessage(NetworkMessage):
    craftersSettings:list[JobCrafterDirectorySettings]
    
    

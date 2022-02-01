from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


class JobCrafterDirectorySettingsMessage(INetworkMessage):
    protocolId = 8518
    craftersSettings:JobCrafterDirectorySettings
    
    

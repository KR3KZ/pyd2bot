from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


class JobCrafterDirectoryDefineSettingsMessage(INetworkMessage):
    protocolId = 6260
    settings:JobCrafterDirectorySettings
    
    

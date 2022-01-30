from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


class JobCrafterDirectorySettingsMessage(INetworkMessage):
    protocolId = 8518
    craftersSettings:JobCrafterDirectorySettings
    
    

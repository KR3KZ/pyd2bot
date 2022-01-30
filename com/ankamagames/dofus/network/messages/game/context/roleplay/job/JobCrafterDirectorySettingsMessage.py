from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


class JobCrafterDirectorySettingsMessage(NetworkMessage):
    protocolId = 8518
    craftersSettings:JobCrafterDirectorySettings
    

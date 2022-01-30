from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


class JobCrafterDirectoryDefineSettingsMessage(NetworkMessage):
    protocolId = 6260
    settings:JobCrafterDirectorySettings
    

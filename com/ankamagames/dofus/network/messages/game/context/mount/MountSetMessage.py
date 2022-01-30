from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class MountSetMessage(NetworkMessage):
    protocolId = 5922
    mountData:MountClientData
    
    

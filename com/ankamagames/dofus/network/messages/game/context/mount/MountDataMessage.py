from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class MountDataMessage(NetworkMessage):
    protocolId = 5244
    mountData:MountClientData
    

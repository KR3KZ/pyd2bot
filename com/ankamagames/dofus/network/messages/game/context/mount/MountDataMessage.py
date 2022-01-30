from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class MountDataMessage(INetworkMessage):
    protocolId = 5244
    mountData:MountClientData
    
    

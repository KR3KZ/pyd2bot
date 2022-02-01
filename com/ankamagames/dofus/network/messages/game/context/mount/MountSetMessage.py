from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class MountSetMessage(INetworkMessage):
    protocolId = 5922
    mountData:MountClientData
    
    

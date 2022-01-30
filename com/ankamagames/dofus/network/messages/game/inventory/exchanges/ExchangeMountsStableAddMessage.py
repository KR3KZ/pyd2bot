from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeMountsStableAddMessage(NetworkMessage):
    protocolId = 8697
    mountDescription:MountClientData
    
    

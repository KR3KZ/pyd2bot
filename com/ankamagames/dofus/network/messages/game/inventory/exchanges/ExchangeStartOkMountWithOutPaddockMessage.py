from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeStartOkMountWithOutPaddockMessage(NetworkMessage):
    protocolId = 9985
    stabledMountsDescription:MountClientData
    
    

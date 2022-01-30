from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeStartOkMountWithOutPaddockMessage(INetworkMessage):
    protocolId = 9985
    stabledMountsDescription:MountClientData
    
    

from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeMountsStableAddMessage(INetworkMessage):
    protocolId = 8697
    mountDescription:MountClientData
    
    

from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeMountsPaddockAddMessage(INetworkMessage):
    protocolId = 3903
    mountDescription:MountClientData
    
    
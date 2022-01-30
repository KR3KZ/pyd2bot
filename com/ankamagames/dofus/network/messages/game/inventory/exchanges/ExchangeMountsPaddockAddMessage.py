from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeMountsPaddockAddMessage(NetworkMessage):
    protocolId = 3903
    mountDescription:MountClientData
    

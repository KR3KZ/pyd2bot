from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeMountsPaddockAddMessage(NetworkMessage):
    mountDescription:list[MountClientData]
    
    

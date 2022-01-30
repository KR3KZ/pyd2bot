from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountsPaddockRemoveMessage(NetworkMessage):
    protocolId = 2113
    mountsId:int
    
